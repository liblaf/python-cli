import functools
import re

import cli


@functools.cache
def config_get(name: str) -> str:
    return cli.utils.run_with_output(["git", "config", "get", name]).strip()


@functools.cache
def repo_url() -> str:
    url: str = config_get("remote.origin.url")
    url = url.removesuffix(".git")
    return url


@functools.cache
def owner_repo() -> tuple[str, str]:
    url: str = repo_url()
    matched = re.search(r"github.com/(?P<owner>[^/]+)/(?P<repo>[^/]+)", url)
    if not matched:
        msg = "no git remotes found"
        raise RuntimeError(msg)
    owner: str = matched.group("owner")
    repo: str = matched.group("repo").removesuffix(".git")
    return owner, repo


@functools.cache
def owner() -> str:
    owner: str
    owner, _ = owner_repo()
    return owner


@functools.cache
def repo() -> str:
    repo: str
    _, repo = owner_repo()
    return repo
