import typer

from cli.utils import add_command

from . import update

app: typer.Typer = typer.Typer(name="gitignore", no_args_is_help=True)
add_command(app, update.app)
