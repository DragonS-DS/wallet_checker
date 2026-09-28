"""Command-line interface for wallet_checker."""

import argparse
import getpass
import json
from typing import Optional, Sequence

from .balance_checker import get_wallet_balances


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line argument parser."""
    parser = argparse.ArgumentParser(
        description="Check Solana and Ethereum balances derived from a mnemonic."
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="print the balances as JSON instead of human-readable text",
    )
    return parser


def _format_balances(balances: dict) -> str:
    sections = []
    for network, values in balances.items():
        if "error" in values:
            sections.append("{}: {}".format(network.title(), values["error"]))
            continue
        sections.append(
            "{}\n  Address: {}\n  Balance: {}".format(
                network.title(),
                values["{} Wallet Address".format(network.title())],
                values["{} Balance".format("SOL" if network == "solana" else "ETH")],
            )
        )
    return "\n\n".join(sections)


def main(argv: Optional[Sequence[str]] = None) -> int:
    """Run the wallet-checker command."""
    args = build_parser().parse_args(argv)
    mnemonic = getpass.getpass("Mnemonic phrase (input hidden): ").strip()
    if not mnemonic:
        print("Error: a mnemonic phrase is required.")
        return 2

    try:
        balances = get_wallet_balances(mnemonic)
    except ValueError as error:
        print("Error: invalid mnemonic phrase: {}".format(error))
        return 2

    if args.json:
        print(json.dumps(balances, indent=2, sort_keys=True))
    else:
        print(_format_balances(balances))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
