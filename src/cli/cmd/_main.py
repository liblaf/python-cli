import typer

from cli import cmd
from cli.utils import add_command

app: typer.Typer = typer.Typer(name="q")
add_command(app, cmd.gitignore.app)
add_command(app, cmd.pre_commit.app)
add_command(app, cmd.sort_toml.app)
