#!/usr/bin/env python

import click


@click.command()
@click.option("--name", help="Place the name you want to YELL")
def marco(name):
    """This is a Marco/Polo game."""

    if name == "Marco":
        click.echo("Polo")
    else:
        click.echo("No!")


if __name__ == "__main__":
    marco()
