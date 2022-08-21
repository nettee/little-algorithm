from pathlib import Path
from typing import List, Dict

import yaml

from little.model import Problem

problems : Dict[str, Problem] = None  # fid -> problem
modify_count = 0


def get_problems_path() -> Path:
    # TODO assert calling from project root
    project_path = Path('.')
    return project_path / 'meta' / 'problems.yaml'


def fetch_problems() -> None:
    global problems
    problems = {}

    problems_path = get_problems_path()
    print('Load problem info from {} ...'.format(problems_path.absolute()))
    with open(problems_path, 'r') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    for p in data:
        problem = Problem(**p)
        problems[problem.fid] = problem


def get_problem_by_fid(fid: str) -> Problem:
    if problems is None:
        fetch_problems()
    return problems[fid]


def add_problem_info(problem: Problem) -> None:
    problems[problem.fid] = problem
    global modify_count
    modify_count += 1


def flush_problem_info() -> None:
    if problems is None or modify_count == 0:
        return
    data = [p.as_data() for p in problems.values()]
    problems_path = get_problems_path()
    with open(problems_path, 'w') as f:
        yaml.dump(data, f, allow_unicode=True, encoding='utf-8')
    print('Flushed problem info to {}'.format(problems_path.absolute()))
