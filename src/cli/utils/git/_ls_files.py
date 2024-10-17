from pathlib import Path

import cli
from cli.typing import StrPath


def ls_files(*files: StrPath) -> list[Path]:
    return [
        Path(line.strip())
        for line in cli.utils.run_with_output(["git", "ls-files", *files]).splitlines()
    ]
