import importlib.resources
import json
from typing import TYPE_CHECKING, Any

import cli

if TYPE_CHECKING:
    from pathlib import Path


def main() -> None:
    cfg: Any = cli.utils.load(importlib.resources.files("cli.assets") / ".cspell.json")  # pyright: ignore [reportArgumentType]
    cfg_fpath: Path = cli.utils.git.root() / ".cspell.json"
    with cfg_fpath.open("w") as fp:
        json.dump(cfg, fp, ensure_ascii=False, sort_keys=False)
    stdout: str = cli.utils.run_with_output(
        [
            "cspell",
            "lint",
            "--words-only",
            "--unique",
            "--no-exit-code",
            "--dot",
            "--gitignore",
            "--color",
            ".",
        ],
        cwd=cli.utils.git.root(),
    )
    words: set[str] = {word.lower() for word in stdout.splitlines()}
    cfg["words"] = sorted(words)
    with cfg_fpath.open("w") as fp:
        json.dump(cfg, fp, ensure_ascii=False, sort_keys=False)
    cli.utils.run(["prettier", "--write", cfg_fpath])
