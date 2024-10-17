from pathlib import Path
from typing import Annotated

import typer

app: typer.Typer = typer.Typer(name="cat-repo", no_args_is_help=True)
DEFAULT_EXCLUDE: list[str] = [
    ".*ignore",
    ".cspell.*",
    ".env.*",
    ".env",
    ".envrc.*",
    ".envrc",
    ".github/copier/",
    ".github/linters/",
    ".github/release-please/",
    ".github/renovate.json",
    ".vscode/",
    "*-lock.*",
    "*.lock",
    "CHANGELOG.md",
]


@app.command()
def wrapper(
    *,
    brief: Annotated[bool, typer.Option()] = False,
    exclude: Annotated[list[str], typer.Option()] = DEFAULT_EXCLUDE,
    exclude_extend: Annotated[list[str], typer.Option()] = [],  # noqa: B006
    output: Annotated[Path | None, typer.Option("-o", "--output")] = None,
) -> None:
    from ._main import main

    main(brief=brief, exclude=exclude, exclude_extend=exclude_extend, output=output)
