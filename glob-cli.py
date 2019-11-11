#!/usr/bin/env python
import click
import glob 


@click.command()
@click.option('--path', prompt='Path to search for csv files',
              help='This is the path to search for files: /tmp')
@click.option('--ftype', prompt='Pass in the type of file',
              help="Pass in the file type:  i.e csv")
def search(path, ftype):
    results = glob.glob(f"{path}/*.{ftype}")
    click.echo(f'These are my results: {results}')

if __name__ == '__main__':
    search()


