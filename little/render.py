from dataclasses import dataclass
from pathlib import Path
from typing import List

from jinja2 import Environment, FileSystemLoader

from index import ArticleInfo
from little.model import Problem, ProblemSolutionSet


@dataclass
class ProblemViewItem:
    fid: str
    problem: Problem
    article: ArticleInfo


def render_readme(article_infos: List[ArticleInfo], solutions: List[ProblemSolutionSet]) -> None:
    print('Render README.md ...')

    fid2article = {}
    for article in article_infos:
        for problem in article.problems:
            fid2article[problem.fid] = article

    problem_view = []
    for solution in solutions:
        problem = solution.problem
        fid = problem.fid
        article = fid2article[fid] if fid in fid2article else None
        problem_view.append(ProblemViewItem(fid, problem, article))

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
