import typer

app: typer.Typer = typer.Typer(name="cspell-init")


@app.command()
def wrapper() -> None:
    from ._main import main

    main()
