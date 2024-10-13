from pathlib import Path

import cli


def root() -> Path:
    return Path(
        cli.utils.run_with_output(["git", "rev-parse", "--show-toplevel"]).strip()
    )
