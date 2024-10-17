from pathlib import Path
from typing import Annotated

import typer

app: typer.Typer = typer.Typer(name="sort-toml")


@app.command()
def wrapper(
    files: Annotated[list[Path], typer.Argument(exists=True, dir_okay=False)],
) -> None:
    from ._main import main

    main(files)
