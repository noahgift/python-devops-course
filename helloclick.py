import click

#var=

@click.command()
@click.option("--phrase", prompt="Enter a phrase", 
    help="Phase in a phrase to tokenize: i.e. The Whale is large")
def tokenize(phrase):
    """This is a commandline tool that tokenizes phrases"""

    click.echo(f"tokenized phrase: {phrase.split()}")

if __name__ == "__main__":
    tokenize()

