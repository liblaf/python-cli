from pathlib import Path
from typing import Any

from ruamel.yaml import YAML

from cli.typing import StrPath


def load_yaml(fpath: StrPath) -> Any:
    fpath: Path = Path(fpath)
    yaml = YAML()
    with fpath.open() as fp:
        return yaml.load(fp)


def save_yaml(data: Any, fpath: StrPath) -> None:
    fpath: Path = Path(fpath)
    yaml = YAML()
    with fpath.open("w") as fp:
        yaml.dump(data, fp)
