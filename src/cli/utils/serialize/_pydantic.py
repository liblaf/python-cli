from typing import Any, TypeVar

import pydantic

from cli.typing import StrPath
from cli.utils import serialize

_C = TypeVar("_C", bound=pydantic.BaseModel)


def load_pydantic(
    cls: type[_C], fpath: StrPath, ext: str | None = None, **kwargs: Any
) -> _C:
    data: Any = serialize.load(fpath, ext, **kwargs)
    return cls.model_validate(data)


def save_pydantic(
    data: pydantic.BaseModel,
    fpath: StrPath,
    *,
    ext: str | None = None,
    exclude_defaults: bool = False,
    **kwargs: Any,
) -> None:
    serialize.save(
        data.model_dump(exclude_defaults=exclude_defaults), fpath, ext, **kwargs
    )
