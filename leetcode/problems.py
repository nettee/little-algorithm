from dataclasses import dataclass, field

import requests
import typing


@dataclass(repr=False)
class Difficulty:
    level: int

    def __repr__(self) -> str:
        if self.level == 1:
            return 'Easy'
        elif self.level == 2:
            return 'Medium'
        elif self.level == 3:
            return 'Hard'
        else:
            return 'Unknown'


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
    status: typing.Any = field(repr=False)
    is_favor: bool = field(repr=False)
    frequency: int = field(repr=False)
    progress: int = field(repr=False)

    def __post_init__(self) -> None:
        self.stat = ProblemStat(**self.stat)
        self.difficulty = Difficulty(**self.difficulty)

    @property
    def iid(self) -> int:
        return self.stat.question_id

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
        return 'https://leetcode-cn.com/problems/' + self.stat.question__title_slug


api = 'https://leetcode-cn.com/api/problems/all/'

problems = None


def fetch_problems() -> None:
    global problems
    problems = {}
    r = requests.get(api)
    data = r.json()
    for p in data['stat_status_pairs']:
        problem = Problem(**p)
        problems[problem.fid] = problem


def query_by_id(fid: str) -> Problem:
    if problems is None:
        fetch_problems()
    return problems[fid]
