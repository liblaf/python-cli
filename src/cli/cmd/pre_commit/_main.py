import typer

from cli.cmd.pre_commit import ensure_hooks_apply
from cli.utils import add_command

app: typer.Typer = typer.Typer(name="pre-commit-utils")
add_command(app, ensure_hooks_apply.app)
