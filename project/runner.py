"""
This might be a script that runs all of your code, or parts of it by subcommands.
"""

import typer
from loguru import logger


cli = typer.Typer()


@cli.command()
def train():
    """
    Trains the model.
    """
    pass


if __name__ == "__main__":
    cli()
