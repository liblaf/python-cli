from pathlib import Path
from typing import Annotated

import httpx
import typer

import cli

app: typer.Typer = typer.Typer(name="gitignore")


@app.command()
def main(
    gitignore: Annotated[
        Path,
        typer.Argument(default_factory=lambda: cli.utils.git.root() / ".gitignore"),
    ],
) -> None:
    lines: list[str] = gitignore.read_text().splitlines()
    result: list[str] = []
    between_markers: bool = False
    for line in lines:
        if line.startswith("# Created by"):
            between_markers = True
            url: str = line.removeprefix("# Created by ").strip()
            resp: httpx.Response = httpx.get(url)
            result += resp.text.splitlines()
        elif line.startswith("# End of"):
            between_markers = False
        elif not between_markers:
            result.append(line)
    gitignore.write_text("\n".join(result) + "\n")
