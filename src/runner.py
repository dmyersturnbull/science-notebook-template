"""
This might be a script that runs all of your code, or parts of it by subcommands.
"""
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Annotated, Self

import typer
from loguru import logger


cli = typer.Typer()


@dataclass(frozen=True, slots=True)
class CliState:
    verbose: bool = False
    quiet: bool = False

    def __post_init__(self: Self) -> None:
        logger.remove()
        if self.verbose:
            logger.add(sys.stderr, level="DEBUG")
        elif self.quiet:
            logger.add(sys.stderr, level="WARNING")
        else:
            logger.add(sys.stderr, level="INFO")


class _Opts:
    verbose = Annotated[bool, typer.Option("Show DEBUG-level logging")]
    quiet = Annotated[bool, typer.Option("Hide INFO-level logging")]


@cli.command()
def train(
    data: Annotated[
        Path, typer.Option(exists=True, help="Directory containing input data")
    ] = Path.cwd(),
    verbose: _Opts.verbose = False,
    quiet: _Opts.quiet = False,
) -> None:
    """
    Trains the model.
    """
    CliState(verbose=verbose, quiet=quiet)


if __name__ == "__main__":
    cli()
