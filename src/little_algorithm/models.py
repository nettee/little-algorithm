from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ProblemMetadata:
    fid: str
    url: str
    title: str
    translated_title: str


@dataclass(frozen=True)
class ArticleInfo:
    title: str
    link: str | None
    problems: list[str]

    @property
    def escaped_title(self) -> str:
        return self.title.replace("|", "\\|")

    def md_piece(self) -> str:
        if self.link:
            return f"[{self.escaped_title}]({self.link})"
        return self.escaped_title


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
