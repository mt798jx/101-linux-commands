import typer
from commands import hello, show

# Root CLI app
app = typer.Typer(help="101 Linux Commands CLI 🚀")

# Register subcommands
app.add_typer(hello.app, name="hello")

# register show directly as command
app.command()(show.show)

if __name__ == "__main__":
    app()