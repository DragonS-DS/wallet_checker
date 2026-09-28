import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from wallet_checker import cli


class CliTests(unittest.TestCase):
    def test_main_prints_human_readable_balances(self):
        balances = {
            "solana": {
                "Solana Wallet Address": "sol-address",
                "SOL Balance": 1.5,
            },
            "ethereum": {
                "Ethereum Wallet Address": "eth-address",
                "ETH Balance": 2.5,
            },
        }

        with patch("wallet_checker.cli.getpass.getpass", return_value="test mnemonic"):
            with patch("wallet_checker.cli.get_wallet_balances", return_value=balances):
                output = io.StringIO()
                with redirect_stdout(output):
                    exit_code = cli.main([])

        self.assertEqual(exit_code, 0)
        self.assertIn("Solana\n  Address: sol-address\n  Balance: 1.5", output.getvalue())
        self.assertIn("Ethereum\n  Address: eth-address\n  Balance: 2.5", output.getvalue())

    def test_main_rejects_empty_mnemonic(self):
        with patch("wallet_checker.cli.getpass.getpass", return_value="  "):
            output = io.StringIO()
            with redirect_stdout(output):
                exit_code = cli.main([])

        self.assertEqual(exit_code, 2)
        self.assertEqual(output.getvalue(), "Error: a mnemonic phrase is required.\n")

    def test_main_prints_json(self):
        balances = {"solana": {"SOL Balance": 1.5}}

        with patch("wallet_checker.cli.getpass.getpass", return_value="test mnemonic"):
            with patch("wallet_checker.cli.get_wallet_balances", return_value=balances):
                output = io.StringIO()
                with redirect_stdout(output):
                    exit_code = cli.main(["--json"])

        self.assertEqual(exit_code, 0)
        self.assertEqual(output.getvalue(), '{\n  "solana": {\n    "SOL Balance": 1.5\n  }\n}\n')
