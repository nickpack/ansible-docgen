import nose
from ansibledocgen.cli import Cli
import unittest
import sys

class TestCli(unittest.TestCase):
    def test_help(self):
        sys.argv = ["--help"]
        cli = Cli()
        assert(cli.options is None)