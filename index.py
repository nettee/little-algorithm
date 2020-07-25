#!/usr/bin/env python3

import sys
from dataclasses import dataclass
from typing import List

import yaml

import leetcode.graphql
import leetcode.problems
from little import render
from little.model import SolutionList
from little.solution import find_solutions


@dataclass
class Problem:
    fid: str
    slug: str
    title: str
    translated_title: str
    url: str
    solutions: SolutionList

    @classmethod
    def from_fid(cls, fid: str):
        problem = leetcode.problems.query_by_id(fid)
        # TODO add local cache
        translated_title = leetcode.graphql.query_translated_title_by_slug(problem.slug)
        solutions = find_solutions(problem.fid)
        # print('translated_title: ', problem.translated_title)
        return Problem(fid=fid,
                       slug=problem.slug,
                       title=problem.title,
                       translated_title=translated_title,
                       url=problem.url,
                       solutions=solutions)


@dataclass
class ArticleInfo:
    title: str
    link: str
    problems: List[Problem]

    def __post_init__(self) -> None:
        if self.problems is None:
            self.problems = []
        else:
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
    