import functools
from pathlib import Path

import cli


def main(
    *,
    brief: bool,
    exclude: list[str],
    exclude_extend: list[str],
    output: Path | None = None,
) -> None:
    exclude += exclude_extend
    files: list[Path] = cli.utils.git.ls_files(*[":!" + x for x in exclude])
    if output is None:
        fprint = print
    else:
        fprint = functools.partial(print, file=output.open("w"))
    fprint("<REPO>")
    for file in files:
        if brief:
            fprint(f'<FILE path="{file}" />')
        else:
            fprint(f'<FILE path="{file}">')
            fprint(file.read_text().strip())
            fprint("</FILE>")
    fprint(f'<META name="{cli.utils.git.repo()}" />')
    fprint(f'<META owner="{cli.utils.git.owner()}" />')
    fprint(f'<META url="{cli.utils.git.repo_url()}" />')
    fprint("</REPO>")
