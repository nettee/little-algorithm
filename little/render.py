from pathlib import Path
from typing import List

from jinja2 import Environment, FileSystemLoader

from index import ArticleInfo


def render_readme(article_infos: List[ArticleInfo]) -> None:
    print('Render README.md ...')
    items = []
    for article in article_infos:
        for problem in article.problems:
            items.append((problem.fid, problem, article))

    items.sort(key=lambda item: '{:>6}'.format(item[0]))

    # TODO assert calling from project root
    project_path = Path('.')
    template_path = project_path / 'little/templates'
    env = Environment(loader=FileSystemLoader(template_path.absolute()))
    template = env.get_template('README.md')
    rendered = template.render(items=items)

    with open('README.md', 'w') as f:
        print(rendered, file=f)
        print('Render README.md done.')
