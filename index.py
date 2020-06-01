#!/usr/bin/env python3

import yaml
import sys
from typing import List
from dataclasses import dataclass

from little import render
import leetcode.problems


@dataclass
class Problem:
    fid: str
    title: str
    url: str

    @classmethod
    def from_fid(cls, fid: str):
        problem = leetcode.problems.query_by_id(fid)
        if problem is None:
            print('problem id {} not found'.format(fid))
            return None
        return Problem(fid=fid, title=problem.title, url=problem.url)


@dataclass
class ArticleInfo:
    title: str
    link: str
    problems: List[Problem]

    def __post_init__(self) -> None:
        self.problems = [Problem.from_fid(str(pid)) for pid in self.problems]

    @property
    def escaped_title(self) -> str:
        return self.title.replace('|', '\|')

    def md_piece(self) -> str:
        if self.link is None:
            return self.escaped_title
        else:
            return '[{}]({})'.format(self.escaped_title, self.link)

def build_table(articleInfos: List[ArticleInfo]) -> None:
    # index = {}
    # for article in articleInfos:
    #     for p in article.problems:
    #         index[p.fid] = article

    render.render_readme(articleInfos)
    

if __name__ == '__main__':
    filename = sys.argv[1]
    print(filename)

    with open(filename, 'r') as f:
        articles = yaml.load(f, Loader=yaml.Loader)
    
    articleInfos = [ArticleInfo(**article) for article in articles]
    build_table(articleInfos)
    