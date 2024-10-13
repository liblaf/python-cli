import subprocess as sp

from cli.typing import CMD


def run_with_output(args: CMD, input: str | None = None) -> str:  # noqa: A002
    proc: sp.CompletedProcess[str] = sp.run(
        args, stdout=sp.PIPE, check=True, input=input, text=True
    )
    return proc.stdout
