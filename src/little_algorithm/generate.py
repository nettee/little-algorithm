from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re

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
        return self.root / "README.md"

    @property
    def articles_path(self) -> Path:
        return self.root / "meta" / "articles.yaml"

    @property
    def solutions_path(self) -> Path:
        return self.root / "solutions"

    @property
    def template_dir(self) -> Path:
        return self.root / "src" / "little_algorithm" / "templates"


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


def build_rows(context: GeneratorContext) -> list[TableRow]:
    articles = load_articles(context.articles_path)
    cache = load_problem_cache(context.readme_path)
    rows: list[TableRow] = []
    for article in articles:
        for fid in article.problems:
            rows.append(
                TableRow(
                    fid=fid,
                    problem=get_problem_metadata(fid, cache),
                    solution_md=render_solution_md(
                        find_java_solutions(context.solutions_path, fid)
                    ),
                    article_md=article.md_piece(),
                )
            )
    rows.sort(key=lambda row: int(row.fid))
    return rows


def main() -> None:
    context = GeneratorContext(root=Path(__file__).resolve().parents[2])
    rows = build_rows(context)
    render_readme(context.template_dir, context.readme_path, rows)


if __name__ == "__main__":
    main()
