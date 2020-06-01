#!/usr/bin/env python3

import yaml
import sys
from typing import List
from dataclasses import dataclass

from little import render

@dataclass
class ArticleInfo:
    title: str
    link: str
    problems: List[int]

    @property
    def escaped_title(self) -> str:
        return self.title.replace('|', '\|')

    def md_piece(self) -> str:
        if self.link is None:
            return self.escaped_title
        else:
            return '[{}]({})'.format(self.escaped_title, self.link)

def build_table(articleInfos: List[ArticleInfo]) -> None:
    index = {}
    for article in articleInfos:
        for p in article.problems:
            index[p] = article

    render.render_readme(index)
    

if __name__ == '__main__':
    filename = sys.argv[1]
    print(filename)

    with open(filename, 'r') as f:
        articles = yaml.load(f, Loader=yaml.Loader)
    
    articleInfos = [ArticleInfo(**article) for article in articles]
    build_table(articleInfos)
    