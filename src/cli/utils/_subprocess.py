import subprocess as sp

from cli.typing import CMD, StrPath


def run(args: CMD, cwd: StrPath | None = None, input: str | None = None) -> None:  # noqa: A002
    sp.run(args, cwd=cwd, check=True, input=input)


def run_with_output(
    args: CMD,
    cwd: StrPath | None = None,
    input: str | None = None,  # noqa: A002
) -> str:
    proc: sp.CompletedProcess[str] = sp.run(
        args, stdout=sp.PIPE, cwd=cwd, check=True, input=input, text=True
    )
    return proc.stdout
