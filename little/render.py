from dataclasses import dataclass
from pathlib import Path
from typing import List

from jinja2 import Environment, FileSystemLoader

from index import ArticleInfo
from little.model import Problem


@dataclass
class ProblemViewItem:
    fid: str
    problem: Problem
    article: ArticleInfo


def render_readme(article_infos: List[ArticleInfo]) -> None:
    print('Render README.md ...')
    problem_view = []
    for article in article_infos:
        for problem in article.problems:
            problem_view.append(ProblemViewItem(problem.fid, problem, article))

    problem_view.sort(key=lambda item: '{:>6}'.format(item.fid))

    # TODO assert calling from project root
    project_path = Path('.')
    template_path = project_path / 'little/templates'
    env = Environment(loader=FileSystemLoader(str(template_path.absolute())))
    template = env.get_template('README.md')
    rendered = template.render(problem_view=problem_view)

    with open('README.md', 'w') as f:
        print(rendered, file=f)
        print('Render README.md done.')
