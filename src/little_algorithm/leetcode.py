from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import requests


@dataclass(repr=False)
class Difficulty:
    level: int


@dataclass
class ProblemStat:
    question_id: int
    frontend_question_id: str
    question__title: str
    question__title_slug: str
    question__hide: bool = field(repr=False)
    total_acs: int = field(repr=False)
    total_submitted: int = field(repr=False)
    total_column_articles: int = field(repr=False)
    is_new_question: bool = field(repr=False)


@dataclass
class Problem:
    stat: ProblemStat
    difficulty: Difficulty
    paid_only: bool = field(repr=False)
    status: Any = field(repr=False)
    is_favor: bool = field(repr=False)
    frequency: int = field(repr=False)
    progress: int = field(repr=False)

    def __post_init__(self) -> None:
        self.stat = ProblemStat(**self.stat)
        self.difficulty = Difficulty(**self.difficulty)

    @property
    def fid(self) -> str:
        return self.stat.frontend_question_id

    @property
    def slug(self) -> str:
        return self.stat.question__title_slug

    @property
    def title(self) -> str:
        return self.stat.question__title

    @property
    def url(self) -> str:
        return "https://leetcode-cn.com/problems/" + self.stat.question__title_slug


_api = "https://leetcode-cn.com/api/problems/all/"
_problem_url = "https://leetcode-cn.com/problems/two-sum/description/"
_problems: dict[str, Problem] | None = None


class GraphQLError(RuntimeError):
    pass


def _fetch_problems() -> None:
    global _problems
    _problems = {}
    response = requests.get(_api, timeout=30)
    response.raise_for_status()
    data = response.json()
    for item in data["stat_status_pairs"]:
        problem = Problem(**item)
        _problems[problem.fid] = problem


def query_by_id(fid: str) -> Problem:
    if _problems is None:
        _fetch_problems()
    return _problems[fid]


def _execute_graphql(payload: dict[str, object]) -> dict[str, object]:
    response = requests.post(
        "https://leetcode-cn.com/graphql",
        json=payload,
        headers={
            "user-agent": "Mozilla/5.0",
            "referer": _problem_url,
            "content-type": "application/json",
        },
        timeout=30,
    )
    response.raise_for_status()
    data = response.json()
    if "errors" in data:
        messages = [error["message"] for error in data["errors"]]
        raise GraphQLError(messages)
    return data["data"]


def query_translated_title_by_slug(title_slug: str) -> str:
    payload = {
        "operationName": "questionData",
        "variables": {"titleSlug": title_slug},
        "query": """query questionData($titleSlug: String!) {
          question(titleSlug: $titleSlug) {
            translatedTitle
          }
        }
        """,
    }
    data = _execute_graphql(payload)
    return data["question"]["translatedTitle"]
