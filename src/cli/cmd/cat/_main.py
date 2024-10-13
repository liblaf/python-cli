from collections.abc import Generator
from pathlib import Path
from typing import Annotated, Optional

import typer
from pathspec import GitIgnoreSpec, PathSpec

import cli

app: typer.Typer = typer.Typer(name="cat")

# ref: [mpoon/gpt-repository-loader](https://github.com/mpoon/gpt-repository-loader)
SYSTEM_PROMPT: str = """\
The following text is a Git repository with code.
The structure of the text are sections that starts with `>>> filename >>>`, followed by the file's content, and ends with `<<< filename <<<`.
The text representing the Git repository ends when the symbols `--- END ---` are encountered.
Any further text beyond `--- END ---` are meant to be interpreted as instructions using the aforementioned Git repository as context.
"""


@app.command()
def main(
    *,
    brief: Annotated[
        bool, typer.Option("-b", "--brief", help="Show only the file names")
    ] = False,
    exclude: Annotated[
        list[str], typer.Option("-E", "--exclude", default_factory=list)
    ],
    pattern: Annotated[Optional[str], typer.Argument()] = None,  # noqa: UP007
) -> None:
    exclude += [".git/", "*-lock.*", "*.lock"]
    args: list[str] = ["fd"]
    for e in exclude:
        args += ["--exclude", e]
    if pattern:
        args.append(pattern)
    args.append(".")
    output: str = cli.utils.run_with_output(args)
    files: list[Path] = [Path(line) for line in output.splitlines()]
    if brief:
        for file in files:
            print(file)
        return
    print(SYSTEM_PROMPT)
    for file in files:
        if file.is_dir():
            continue
        print(f">>> {file} >>>")
        text: str = file.read_text()
        if not text.endswith("\n"):
            text += "\n"
        print(text, end="")
        print(f"<<< {file} <<<")
    print("--- END ---")


def walk(directory: Path, exclude_from: list[str]) -> Generator[Path, None, None]:
    patterns: list[str] = []
    for filename in exclude_from:
        ignore_fpath: Path = directory / filename
        if ignore_fpath.exists():
            patterns += ignore_fpath.read_text().splitlines()
    spec: PathSpec = GitIgnoreSpec.from_lines(patterns)
    for child in directory.iterdir():
        if child.is_dir():
            for p in spec.match_files(walk(child, exclude_from), negate=True):
                yield Path(p)
        elif not spec.match_file(child):
            yield child
