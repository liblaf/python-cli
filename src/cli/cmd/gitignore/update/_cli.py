from pathlib import Path
from typing import Annotated

import typer

import cli

app: typer.Typer = typer.Typer(name="update")


@app.command()
def wrapper(
    gitignore: Annotated[
        Path,
        typer.Argument(default_factory=lambda: cli.utils.git.root() / ".gitignore"),
    ],
) -> None:
    from ._main import main

    main(gitignore=gitignore)
