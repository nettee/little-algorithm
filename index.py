#!/usr/bin/env python3

import sys
from dataclasses import dataclass, asdict
from typing import List

import yaml

import leetcode.graphql
import leetcode.problems
from little import render
from little.model import Problem
from little.solution import find_solutions


def build_problem_from_fid(fid: str):
    # TODO add local cache
    problem = leetcode.problems.query_by_id(fid)
    translated_title = leetcode.graphql.query_translated_title_by_slug(problem.slug)
    solutions = find_solutions(problem.fid)
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
            self.problems = [build_problem_from_fid(str(pid)) for pid in self.problems]

    @property
    def escaped_title(self) -> str:
        return self.title.replace('|', '\|')

    def md_piece(self) -> str:
        if self.link is None:
            return self.escaped_title
        else:
            return '[{}]({})'.format(self.escaped_title, self.link)


def build_table(articleInfos: List[ArticleInfo], template_path: str) -> None:
    # index = {}
    # for article in articleInfos:
    #     for p in article.problems:
    #         index[p.fid] = article

    render.render_readme(articleInfos, template_path)


def dump_meta(articleInfos: List[ArticleInfo]) -> None:
    data = [asdict(info) for info in articleInfos]
    yaml_content = yaml.dump(data, Dumper=yaml.Dumper)
    with open('index.yaml', 'w') as of:
        print(yaml_content, file=of)
    print('Saved meta info to index.yaml')


if __name__ == '__main__':
    filename = sys.argv[1]
    template_path = sys.argv[2]
    print('Load article info from {} ...'.format(filename))

    with open(filename, 'r') as f:
        articles = yaml.load(f, Loader=yaml.Loader)
    
    articleInfos = [ArticleInfo(**article) for article in articles]

    dump_meta(articleInfos)
    build_table(articleInfos, template_path)
