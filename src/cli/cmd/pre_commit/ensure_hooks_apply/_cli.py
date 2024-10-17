from pathlib import Path
from typing import Annotated

import typer

app: typer.Typer = typer.Typer(name="ensure-hooks-apply")


@app.command()
def wrapper(
    config: Annotated[Path, typer.Argument(exists=True, dir_okay=False, writable=True)],
) -> None:
    from ._main import main

    main(config=config)
