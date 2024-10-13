import json
from pathlib import Path
from typing import Any

from cli.typing import StrPath


def load_json(fpath: StrPath, **kwargs: Any) -> Any:
    fpath: Path = Path(fpath)
    with fpath.open() as fp:
        return json.load(fp, **kwargs)


def save_json(data: Any, fpath: StrPath, **kwargs: Any) -> None:
    fpath: Path = Path(fpath)
    with fpath.open("w") as fp:
        json.dump(data, fp, **kwargs)
