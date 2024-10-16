import typer

from cli import cmd
from cli.utils import add_command

app: typer.Typer = typer.Typer(name="q", no_args_is_help=True)
add_command(app, cmd.cat_repo.app)
add_command(app, cmd.cspell_init.app)
add_command(app, cmd.gitignore.app)
add_command(app, cmd.pre_commit.app)
add_command(app, cmd.sort_toml.app)
