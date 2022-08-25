from dataclasses import dataclass
from pathlib import Path
from typing import List, Dict, Any
from collections import defaultdict


@dataclass
class Solution:
    path: Path
    lang: str = 'Java'
    order: int = 999

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

        # group by lang
        m = defaultdict(list)
        for s in self.solutions:
            m[s.lang].append(s)
        piece_list = [self.md_piece_lang(lang, ss) for (lang, ss) in m.items()]
        return ', '.join(piece_list)

    @staticmethod
    def md_piece_lang(lang: str, solutions: List[Solution]) -> str:
        if len(solutions) == 1:
            solution = solutions[0]
            return f'[{lang}]({solution.uri()})'
        else:
            parts = ', '.join(f'[{i+1}]({s.uri()})' for (i, s) in enumerate(solutions))
            return f'{lang}({parts})'


@dataclass
class Problem:
    fid: str  # 前端题目 ID
    slug: str  # url 中的 slug
    title: str  # 标题（英文）
    translated_title: str  # 标题（中文）
    url: str  # leetcode-cn 链接
    # solutions: SolutionList

    def as_data(self) -> Dict[str, Any]:
        return {
            'fid': self.fid,
            'slug': self.slug,
            'title': self.title,
            'translated_title': self.translated_title,
            'url': self.url,
        }
