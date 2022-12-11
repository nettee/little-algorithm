from pathlib import Path
from typing import List

from little.model import SolutionFile, ProblemSolutionSet
from little.problem import get_problem_by_fid


def get_lang(suffix: str) -> str:
    if suffix == '.cpp':
        return 'C++'
    elif suffix == '.java':
        return 'Java'
    return 'Java'


def get_solution_from_path(path: Path) -> SolutionFile:
    lang = get_lang(path.suffix)
    try:
        order = int(path.stem)
        return SolutionFile(path=path, lang=lang, order=order)
    except ValueError:
        return SolutionFile(path=path, lang=lang)


def find_problem_solutions(fid: str) -> ProblemSolutionSet:
    problem = get_problem_by_fid(fid)  # TODO use cache
    dir_name = fid.zfill(4)

    # TODO assert calling from project root
    project_path = Path('.')
    solution_path = project_path / 'solutions' / dir_name
    if not solution_path.exists():
        print(f'Warning: path for problem {fid} not exists -- No such dir: {solution_path.absolute()}')
        return ProblemSolutionSet(problem, solutions=list())
    solution_files = list(solution_path.iterdir())
    if len(solution_files) == 0:
        print(f'Warning: no solutions found for problem {fid} -- No files in dir: {solution_path.absolute()}')
        return ProblemSolutionSet(problem, solutions=list())
    solutions = [get_solution_from_path(path) for path in solution_files]
    solutions.sort(key=lambda s: (s.lang, s.order))
    return ProblemSolutionSet(problem, solutions=solutions)


def find_all_problem_solutions() -> List[ProblemSolutionSet]:
    # TODO assert calling from project root
    project_path = Path('.')
    fids = [str(int(x.name)) for x in (project_path / 'solutions').iterdir() if x.is_dir()]
    return [find_problem_solutions(fid) for fid in fids]
