from pathlib import Path

from little.model import Solution, SolutionList


def get_lang(suffix: str) -> str:
    if suffix == 'cpp':
        return 'C++'
    elif suffix == 'java':
        return 'Java'
    return 'Java'


def get_solution_from_path(path: Path) -> Solution:
    lang = get_lang(path.suffix)
    try:
        order = int(path.stem)
        return Solution(path=path, lang=lang, order=order)
    except ValueError:
        return Solution(path=path, lang=lang)


def find_solutions(fid: str) -> SolutionList:
    dir_name = fid.zfill(4)

    # TODO assert calling from project root
    project_path = Path('.')
    solution_path = project_path / 'solutions' / dir_name
    if not solution_path.exists():
        print(f'Warning: path for problem {fid} not exists -- No such dir: {solution_path.absolute()}')
        return SolutionList(solutions=list())
    solution_files = list(solution_path.iterdir())
    if len(solution_files) == 0:
        print(f'Warning: no solutions found for problem {fid} -- No files in dir: {solution_path.absolute()}')
        return SolutionList(solutions=list())
    solutions = [get_solution_from_path(path) for path in solution_files]
    solutions.sort(key=lambda s: (s.lang, s.order))
    return SolutionList(solutions=solutions)
