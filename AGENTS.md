# AGENTS.md

## Repository overview
- This repo is a small Python generator for the root `README.md`.
- Inputs: `meta/articles.yaml`, existing README table rows used as a metadata cache, `solutions/` Java files, and `src/little_algorithm/templates/README.md.j2`.
- Main package: `src/little_algorithm/`
- CLI entrypoint: `generate = little_algorithm.generate:main`
- Build config: `pyproject.toml`

## Tooling snapshot
- Python: `3.14` from `.python-version`
- Runner/package manager: `uv`
- Build backend: `setuptools`
- Runtime deps: `jinja2`, `pyyaml`, `requests`
- No configured linter, formatter, or test runner
- No Cursor rules in `.cursor/rules/`
- No `.cursorrules`
- No `.github/copilot-instructions.md`

## Important paths
- `pyproject.toml` — package metadata and console script
- `Makefile` — `make` runs the generator
- `README.md` — generated output and metadata cache
- `meta/articles.yaml` — article/problem mapping input
- `src/little_algorithm/generate.py` — orchestration logic
- `src/little_algorithm/leetcode.py` — LeetCode HTTP/API code
- `src/little_algorithm/models.py` — domain dataclasses
- `src/little_algorithm/readme.py` — Jinja rendering helper
- `src/little_algorithm/templates/README.md.j2` — README template
- `solutions/` — Java reference solutions used as data input

## Build / run commands
Primary command:

```bash
uv run generate
```

Make shortcuts:

```bash
make
make all
```

- Packaging is managed through `setuptools` in `pyproject.toml`.
- There is no separate repo build script beyond running the generator.

## Lint / format commands
- No lint command is configured.
- No formatter command is configured.
- Do not invent repo-standard lint or format commands in docs or commits.

## Test commands
- No test suite is currently present.
- No `tests/` directory was found.
- No `pytest`, `unittest` config, `tox`, or `nox` config was found.
- Do not claim tests were run unless you actually added and ran them.

### Single-test guidance
- There is currently no project-specific single-test command.
- If `pytest` is added later, the expected single-test form would be:

```bash
uv run pytest path/to/test_file.py::test_name
```

- Only use or document that after `pytest` is actually added.

## Preferred validation workflow
- For generator changes, run:

```bash
uv run generate
```

- Then inspect the resulting diff in `README.md`.
- Confirm ordering, table rows, and links still look correct.
- If you touch `leetcode.py`, validation may require network access.

## Code style guidelines

### General
- Follow the existing code style instead of introducing a new one.
- Prefer minimal, local changes.
- Keep functions small and single-purpose.
- Favor straightforward procedural flow over abstraction-heavy designs.
- Prefer readability over cleverness.

### Imports
- Use `from __future__ import annotations` at the top of Python modules.
- Group imports as: standard library, third-party, local package.
- Separate groups with a blank line.
- Prefer explicit imports; avoid wildcard imports.

### Formatting
- Use 4-space indentation.
- Match the repository's current spacing and blank-line style.
- Split long regexes, comprehensions, and constructor calls across lines when it improves readability.
- Prefer f-strings for interpolation.

### Types and models
- Add explicit type hints for public functions and important helpers.
- Use modern built-in generics like `list[str]` and `dict[str, ProblemMetadata]`.
- Use `X | None` instead of `Optional[X]`.
- Prefer dataclasses for structured data passed through the generator.
- Use `@dataclass(frozen=True)` for immutable value objects when mutation is unnecessary.

### Naming
- Use `snake_case` for functions, variables, and helpers.
- Use `PascalCase` for classes.
- Use leading underscores for module-private globals and helpers.
- Keep names descriptive and domain-specific.
- Avoid unnecessary abbreviations, except established ones like `fid`.

### Error handling
- Keep error handling simple and explicit.
- Preserve `response.raise_for_status()` for HTTP failures.
- Use focused custom exceptions when domain-specific signaling is needed, like `GraphQLError`.
- Do not silently swallow exceptions.
- Avoid broad `except Exception:` unless there is a clear recovery path.

### Data and side effects
- Keep pure transformation logic separate from I/O where practical.
- Read and write text with `encoding="utf-8"`.
- Limit file writes to clear output steps.
- Preserve deterministic output ordering; rows are currently sorted numerically by `fid`.
- Be careful when changing README parsing because it also acts as a metadata cache.

### Templates and generated output
- Treat `src/little_algorithm/templates/README.md.j2` as the source of truth for generated README structure.
- If you change output shape, update both the template and supporting Python logic.
- Avoid manual edits to generated sections of `README.md` unless generator behavior is also updated.
- Keep Markdown output stable to minimize noisy diffs.

### Network behavior
- `src/little_algorithm/leetcode.py` performs live HTTP requests.
- Prefer cached README-derived metadata when available.
- Avoid adding unnecessary API calls.
- Preserve request timeouts and headers if changing network code.

## Repository-specific conventions
- Treat this as a code generator repo, not a general app.
- `README.md` is generated output, not purely handwritten content.
- `solutions/` is primarily data input, not Python application logic.
- Most code changes should stay inside `src/little_algorithm/`.
- Preserve the existing data flow: load YAML, inspect README cache, query LeetCode only when needed, render template.
- Avoid broad refactors unless explicitly requested.

## Typical agent workflow
- Generator logic changes: edit Python under `src/little_algorithm/`, update template/data files only when required, run `uv run generate`, inspect the `README.md` diff.
- Article mapping changes: edit `meta/articles.yaml`, then regenerate README.
- Output-format changes: update `README.md.j2`, update supporting Python logic if needed, then regenerate README.

## What to avoid
- Do not assume JS/TS tooling exists.
- Do not assume pytest, ruff, black, or mypy exist.
- Do not add unrelated infrastructure just to satisfy a generic workflow.
- Do not manually edit generated README content without updating the generator.
- Do not replace simple dataclass-based code with heavier abstractions without a clear reason.
