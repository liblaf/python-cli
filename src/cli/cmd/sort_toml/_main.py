import os
import shutil
from pathlib import Path
from typing import Annotated

import typer

import cli

try:
    from toml_sort import tomlsort
except ImportError as err:
    msg = "sort-toml"
    raise cli.utils.ExtraNotInstalledError(msg) from err


app: typer.Typer = typer.Typer(name="sort-toml")


@app.command()
def main(
    files: Annotated[list[Path], typer.Argument(exists=True, dir_okay=False)],
) -> None:
    for fpath in files:
        text: str = fpath.read_text()
        schema_comment: str = ""
        if text.startswith("#:schema "):
            # skip schema comment since `toml-sort` will add spaces before comments
            schema_comment = text.split("\n", 1)[0] + "\n"
            text = text.removeprefix(schema_comment)
        ts: tomlsort.TomlSort = tomlsort.TomlSort(
            text,
            sort_config=tomlsort.SortConfiguration(
                table_keys=True, inline_tables=True, inline_arrays=True
            ),
        )
        text: str = schema_comment + ts.sorted()
        if taplo_exe := shutil.which("taplo") or os.getenv("TAPLO"):
            text: str = cli.utils.run_with_output(
                [taplo_exe, "format", "-"], input=text
            )
        else:
            msg = "sort-toml"
            raise cli.utils.ExtraNotInstalledError(msg)
        fpath.write_text(text)
