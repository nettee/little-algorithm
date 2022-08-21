#!/usr/bin/env python3

import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import List

import yaml

import leetcode.graphql
import leetcode.problems
from little import render
from little.model import Problem
from little.problem import get_problem_by_fid, add_problem_info, flush_problem_info
from little.solution import find_solutions


def get_problem_info(fid: str):
    problem = get_problem_by_fid(fid)  # read from cache first
    if problem is None:
        print('Fetch problem {} info from leetcode ...'.format(fid))
        leetcode_problem = leetcode.problems.query_by_id(fid)
        translated_title = leetcode.graphql.query_translated_title_by_slug(leetcode_problem.slug)
        problem = Problem(fid=fid,
                          slug=leetcode_problem.slug,
                          title=leetcode_problem.title,
                          translated_title=translated_title,
                          url=leetcode_problem.url)
        add_problem_info(problem)  # add to cache
    return problem


def build_problem_from_fid(fid: str):
    problem = get_problem_info(fid)
    solutions = find_solutions(problem.fid)
    problem.solutions = solutions
    return problem


@dataclass
class ArticleInfo:
    title: str
    link: str
    problems: List[Problem]

    def __post_init__(self) -> None:
        if self.problems is None:
            self.problems = []
        else:
            self.problems = [build_problem_from_fid(str(pid)) for pid in self.problems]

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


def dump_meta(articleInfos: List[ArticleInfo]) -> None:
    data = [asdict(info) for info in articleInfos]
    yaml_content = yaml.dump(data, Dumper=yaml.Dumper)
    with open('index.yaml', 'w') as of:
        print(yaml_content, file=of)
    print('Saved meta info to index.yaml')


if __name__ == '__main__':
    # TODO assert calling from project root
    project_path = Path('.')
    articles_path = project_path / 'meta' / 'articles.yaml'

    print('Load article info from {} ...'.format(articles_path.absolute()))
    with open(articles_path, 'r') as f:
        articles = yaml.load(f, Loader=yaml.Loader)

    articleInfos = [ArticleInfo(**article) for article in articles]

    dump_meta(articleInfos)
    build_table(articleInfos)

    flush_problem_info()
