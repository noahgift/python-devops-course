#!/usr/bin/env python
import click
import glob 


@click.command()
def search():
    results = glob.glob(f"/home/ec2-user/environment/files/*.csv")
    click.echo(f'These are my results: {results}')

if __name__ == '__main__':
    search()


