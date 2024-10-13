import json
import sys
import tempfile

import typer

import cli

app: typer.Typer = typer.Typer(name="cspell-init")


@app.command()
def main() -> None:
    ignore_paths: list[str] = sorted(
        ["**/.cspell.*", "**/.git", "**/*-lock.*", "**/*.lock*"]
    )
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json") as fp:
        json.dump(
            {
                "$schema": "https://raw.githubusercontent.com/streetsidesoftware/cspell/main/packages/cspell-types/cspell.schema.json",
                "version": "0.2",
                "language": "en",
                "words": [],
                "ignorePaths": ignore_paths,
                "allowCompoundWords": True,
            },
            fp,
        )
        fp.flush()
        stdout: str = cli.utils.run_with_output(
            [
                "cspell",
                "lint",
                "--config",
                fp.name,
                "--words-only",
                "--unique",
                "--no-exit-code",
                "--dot",
                "--gitignore",
                "--color",
                ".",
            ]
        )
    words: set[str] = {word.lower() for word in stdout.splitlines()}
    json.dump(
        {
            "$schema": "https://raw.githubusercontent.com/streetsidesoftware/cspell/main/packages/cspell-types/cspell.schema.json",
            "version": "0.2",
            "language": "en",
            "words": sorted(words),
            "ignorePaths": ignore_paths,
            "allowCompoundWords": True,
        },
        sys.stdout,
        ensure_ascii=False,
        sort_keys=False,
    )
