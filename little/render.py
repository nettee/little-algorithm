from typing import List

from jinja2 import Environment, FileSystemLoader

from index import ArticleInfo


def render_readme(article_infos: List[ArticleInfo], template_path: str) -> None:
    print('Render README.md ...')
    items = []
    for article in article_infos:
        for problem in article.problems:
            items.append((problem.fid, problem, article))

    items.sort(key=lambda item: '{:>6}'.format(item[0]))
                
    env = Environment(loader=FileSystemLoader(template_path))
    template = env.get_template('README.md')
    rendered = template.render(items=items)

    with open('README.md', 'w') as f:
        print(rendered, file=f)
        print('Render README.md done.')

