from __future__ import annotations

from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from little_algorithm.models import TableRow


def render_readme(
    template_dir: Path,
    output_path: Path,
    template_name: str,
    rows: list[TableRow],
) -> None:
    env = Environment(loader=FileSystemLoader(str(template_dir)))
    template = env.get_template(template_name)
    rendered = template.render(rows=rows)
    output_path.write_text(rendered, encoding="utf-8")
