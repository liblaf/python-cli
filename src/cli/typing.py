from collections.abc import Sequence
from os import PathLike

StrPath = str | PathLike[str]
CMD = StrPath | Sequence[StrPath]
