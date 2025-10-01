"""
CLI entry point for the 101 Linux Commands application.
"""

import typer

from commands import hello, show

app = typer.Typer(help="101 Linux Commands CLI 🚀")

# Register subcommands
app.add_typer(hello.app, name="hello")
app.command()(show.show)


def main() -> None:
    """CLI entry point."""
    app()


if __name__ == "__main__":
    app()
