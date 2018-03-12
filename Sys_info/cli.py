# -*- coding: utf-8 -*-

"""Console script for Sys_info."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for Sys_info."""
    click.echo("Replace this message by putting your code into "
               "Sys_info.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
