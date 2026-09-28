# Wallet Checker

A Python library and command-line program to check Solana and Ethereum balances
derived from a mnemonic phrase.

## Installation
```sh
pip install wallet_checker
```

## Command-line usage
```sh
wallet-checker
```

The program securely prompts for the mnemonic without echoing it to the terminal,
then displays balances for the first standard Solana and Ethereum derivation paths.
Use `wallet-checker --json` for machine-readable output. Avoid passing a mnemonic
on the command line, where it could be retained in shell history or visible to
other local processes.

## Usage
```python
from wallet_checker.balance_checker import get_wallet_balances

seed_phrase = "your 12 or 24-word seed phrase here"
balances = get_wallet_balances(seed_phrase)
print(balances)
```

## Features
- Retrieve **Solana** balance using a seed phrase
- Retrieve **Ethereum** balance using a seed phrase
- Supports **both 12-word and 24-word mnemonics**
- No API key required

## Requirements
- Python 3.7+
- Dependencies (automatically installed via `pip install`):
  - `solana`
  - `solders`
  - `bip_utils`
  - `web3`

## License
MIT License