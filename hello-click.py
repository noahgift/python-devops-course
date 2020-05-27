#!/usr/bin/env python
import click

@click.command()
def hello():
    """This is a hello world cli
    To run it type in ./hello-click.py
    """
    click.echo('Hello World!')

if __name__ == '__main__':
    hello()