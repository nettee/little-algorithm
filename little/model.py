from dataclasses import dataclass
from pathlib import Path
from typing import List


@dataclass
class Solution:
    path: Path
    lang: str = 'Java'

    def file_name(self) -> str:
        return self.path.name

    def uri(self) -> str:
        return str(self.path)

    def md_piece(self) -> str:
        text = self.file_name()
        uri = str(self.path)
        return f'[{text}]({uri})'


@dataclass
class SolutionList:
    solutions: List[Solution]

    def md_piece(self) -> str:
        if len(self.solutions) == 0:
            return ''
        elif len(self.solutions) == 1:
            solution = self.solutions[0]
            return f'[{solution.lang}]({solution.uri()})'
        else:
            # TODO assert solutions are all written in Java
            lang = self.solutions[0].lang
            parts = ', '.join(f'[{i+1}]({s.uri()})' for (i, s) in enumerate(self.solutions))
            return f'{lang}({parts})'

