from pathlib import Path
from typing import Any

import pre_commit
import pre_commit.clientlib
import pre_commit.commands
import pre_commit.commands.run
import pre_commit.git
import pre_commit.hook
import pre_commit.repository
import pre_commit.store


def main(config: Path) -> None:
    """Check hooks apply to the repository.

    Reference:
        1. <https://github.com/pre-commit/pre-commit/blob/cc4a52241565440ce200666799eef70626457488/pre_commit/meta_hooks/check_hooks_apply.py#L14-L28>
    """
    cfg: Any = pre_commit.clientlib.load_config(config)
    classifier: pre_commit.commands.run.Classifier = (
        pre_commit.commands.run.Classifier.from_config(
            pre_commit.git.get_all_files(), cfg["files"], cfg["exclude"]
        )
    )
    include: list[pre_commit.hook.Hook] = []
    exclude: list[pre_commit.hook.Hook] = []
    for hook in pre_commit.repository.all_hooks(cfg, pre_commit.store.Store()):
        if hook.always_run or hook.language == "fail":
            include.append(hook)
        elif not any(classifier.filenames_for_hook(hook)):
            exclude.append(hook)
        else:
            include.append(hook)
    raise NotImplementedError  # TODO: implement
