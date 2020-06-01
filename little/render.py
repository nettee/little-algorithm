from jinja2 import Environment, PackageLoader, FileSystemLoader
from typing import List

from index import ArticleInfo


def render_readme(articleInfos: List[ArticleInfo]) -> None:
    items = []
    for article in articleInfos:
        for problem in article.problems:
            items.append((problem.fid, problem, article))

    items.sort(key=lambda item: '{:>6}'.format(item[0]))
                
    env = Environment(loader=FileSystemLoader('/Users/william/projects/little-algorithm/little/templates'))
    template = env.get_template('README.md')
    rendered = template.render(items=items)

    with open('README.md', 'w') as f:
        print(rendered, file=f)

