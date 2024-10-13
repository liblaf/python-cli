import typer

from cli.utils import add_command

from . import update

app: typer.Typer = typer.Typer(name="gitignore")
add_command(app, update.app)
