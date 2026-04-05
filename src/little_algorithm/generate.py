from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
import tomllib

import yaml

from little_algorithm import leetcode
from little_algorithm.models import ArticleInfo, ProblemMetadata, SolutionFile, TableRow
from little_algorithm.readme import render_readme


README_ROW_RE = re.compile(
    r"^\| \[(?P<fid>\d+)\]\((?P<url>[^)]+)\) \| "
    r"(?P<title>.*?)<br />(?P<translated_title>.*?) \| .*? \| .*? \|$"
)


@dataclass
class GeneratorContext:
    root: Path

    @property
    def readme_path(self) -> Path:
        return self.readme_en_path

    @property
    def readme_en_path(self) -> Path:
        return self.root / "README.md"

    @property
    def readme_zh_path(self) -> Path:
        return self.root / "README_zh.md"

    @property
    def problem_cache_path(self) -> Path:
        if self.readme_zh_path.exists():
            return self.readme_zh_path
        return self.readme_en_path

    @property
    def articles_path(self) -> Path:
        return self.root / "meta" / "articles.yaml"

    @property
    def solutions_path(self) -> Path:
        return self.root / "solutions"

    @property
    def template_dir(self) -> Path:
        return self.root / "src" / "little_algorithm" / "templates"

    @property
    def rena_blog_algorithm_course_dir(self) -> Path:
        return (
            self.root.parent / "rena-blog" / "src" / "content" / "courses" / "algorithm"
        )


def load_articles(path: Path) -> list[ArticleInfo]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    return [
        ArticleInfo(
            title=item["title"],
            link=item.get("link"),
            problems=[str(problem) for problem in item.get("problems") or []],
        )
        for item in data
    ]


def load_problem_cache(path: Path) -> dict[str, ProblemMetadata]:
    cache: dict[str, ProblemMetadata] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        match = README_ROW_RE.match(line)
        if not match:
            continue
        cache[match["fid"]] = ProblemMetadata(
            fid=match["fid"],
            url=match["url"],
            title=match["title"],
            translated_title=match["translated_title"],
        )
    return cache


def get_problem_metadata(
    fid: str, cache: dict[str, ProblemMetadata]
) -> ProblemMetadata:
    if fid in cache:
        return cache[fid]
    problem = leetcode.query_by_id(fid)
    return ProblemMetadata(
        fid=fid,
        url=problem.url,
        title=problem.title,
        translated_title=leetcode.query_translated_title_by_slug(problem.slug),
    )


def find_java_solutions(root: Path, fid: str) -> list[SolutionFile]:
    solution_dir = root / fid.zfill(4)
    if not solution_dir.exists():
        return []

    files = [
        path
        for path in solution_dir.iterdir()
        if path.is_file() and path.suffix == ".java"
    ]

    def sort_key(path: Path) -> tuple[int, int | str]:
        try:
            return (0, -int(path.stem))
        except ValueError:
            return (1, path.name)

    files.sort(key=sort_key)
    return [SolutionFile(path=path.relative_to(root.parent)) for path in files]


def render_solution_md(solutions: list[SolutionFile]) -> str:
    if not solutions:
        return ""
    if len(solutions) == 1:
        return f"[Java]({solutions[0].uri()})"
    parts = ", ".join(
        f"[{index}]({solution.uri()})"
        for index, solution in enumerate(solutions, start=1)
    )
    return f"Java({parts})"


def build_course_slug_map(course_dir: Path) -> dict[str, Path]:
    slug_map: dict[str, Path] = {}
    for meta_path in course_dir.glob("*/meta.toml"):
        meta = tomllib.loads(meta_path.read_text(encoding="utf-8"))
        slug = meta.get("slug")
        if isinstance(slug, str):
            slug_map[slug] = meta_path.parent
    return slug_map


def load_markdown_frontmatter_title(path: Path) -> str | None:
    content = path.read_text(encoding="utf-8")
    if not content.startswith("---\n"):
        return None
    _, _, rest = content.partition("---\n")
    frontmatter_text, separator, _ = rest.partition("\n---\n")
    if not separator:
        return None
    frontmatter = yaml.safe_load(frontmatter_text)
    title = frontmatter.get("title") if isinstance(frontmatter, dict) else None
    if isinstance(title, str):
        return title
    return None


def resolve_article_title(
    article: ArticleInfo,
    article_locale: str,
    slug_map: dict[str, Path],
) -> str:
    slug = article.slug()
    if not slug:
        return article.title

    chapter_dir = slug_map.get(slug)
    if chapter_dir is None:
        return article.title

    localized_path = chapter_dir / f"{article_locale}.md"
    fallback_path = chapter_dir / "zh.md"

    for path in (localized_path, fallback_path):
        if path.exists():
            title = load_markdown_frontmatter_title(path)
            if title:
                return title

    return article.title


def build_rows(context: GeneratorContext, article_locale: str) -> list[TableRow]:
    articles = load_articles(context.articles_path)
    cache = load_problem_cache(context.problem_cache_path)
    slug_map = build_course_slug_map(context.rena_blog_algorithm_course_dir)
    rows: list[TableRow] = []
    for article in articles:
        article_title = resolve_article_title(article, article_locale, slug_map)
        for fid in article.problems:
            rows.append(
                TableRow(
                    fid=fid,
                    problem=get_problem_metadata(fid, cache),
                    solution_md=render_solution_md(
                        find_java_solutions(context.solutions_path, fid)
                    ),
                    article_md=article.md_piece(article_locale, title=article_title),
                )
            )
    rows.sort(key=lambda row: int(row.fid))
    return rows


def main() -> None:
    context = GeneratorContext(root=Path(__file__).resolve().parents[2])
    rows_zh = build_rows(context, article_locale="zh")
    rows_en = build_rows(context, article_locale="en")
    render_readme(
        context.template_dir, context.readme_zh_path, "README_zh.md.j2", rows_zh
    )
    render_readme(context.template_dir, context.readme_en_path, "README.md.j2", rows_en)


if __name__ == "__main__":
    main()
