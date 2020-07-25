from pathlib import Path
from typing import List

from little.model import Solution, SolutionList


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
    return SolutionList(solutions=[Solution(path=path) for path in solution_files])
