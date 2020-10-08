import click

@click.command()
@click.option("--phrase", prompt="Enter a phrase", help="")
def tokenize(phrase):
    """tokenize phrase"""

    click.echo(f"tokenized phrase: {phrase.split()}")


if __name__ == "__main__":
    tokenize()

