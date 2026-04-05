from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re


NETTEE_COURSE_LINK_RE = re.compile(
    r"^(?P<base>https://nettee\.io)/(?P<locale>zh|en)/courses/algorithm/(?P<slug>[^/]+)/?$"
)


@dataclass(frozen=True)
class ProblemMetadata:
    fid: str
    url: str
    title: str
    translated_title: str


@dataclass(frozen=True)
class ArticleInfo:
    title: str
    title_en: str | None
    link: str | None
    problems: list[str]

    @property
    def escaped_title(self) -> str:
        return self.title.replace("|", "\\|")

    def localized_link(self, locale: str) -> str | None:
        if not self.link:
            return None
        match = NETTEE_COURSE_LINK_RE.match(self.link)
        if not match:
            return self.link
        return f"{match['base']}/{locale}/courses/algorithm/{match['slug']}"

    def slug(self) -> str | None:
        if not self.link:
            return None
        match = NETTEE_COURSE_LINK_RE.match(self.link)
        if not match:
            return None
        return match["slug"]

    def localized_title(self, locale: str) -> str:
        if locale == "en" and self.title_en:
            return self.title_en
        return self.title

    def md_piece(self, locale: str) -> str:
        display_title = self.localized_title(locale).replace("|", "\\|")
        link = self.localized_link(locale)
        if link:
            return f"[{display_title}]({link})"
        return display_title


@dataclass(frozen=True)
class SolutionFile:
    path: Path

    def uri(self) -> str:
        return self.path.as_posix()


@dataclass(frozen=True)
class TableRow:
    fid: str
    problem: ProblemMetadata
    solution_md: str
    article_md: str
