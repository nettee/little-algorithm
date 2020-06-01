from jinja2 import Environment, PackageLoader, FileSystemLoader


def render_readme(index) -> None:
    items = sorted(index.items(), key=lambda item: item[0])

    env = Environment(loader=FileSystemLoader('/Users/william/projects/little-algorithm/little/templates'))
    template = env.get_template('README.md')
    rendered = template.render(items=items)

    with open('README.md', 'w') as f:
        print(rendered, file=f)

