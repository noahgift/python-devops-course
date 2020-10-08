from click.testing import CliRunner
from helloclick import tokenize


def test_helloclick():
    runner = CliRunner()
    result = runner.invoke(tokenize, ["--phrase", "The Whale is large"])
    assert result.exit_code == 0
    assert "Whale" in result.output
