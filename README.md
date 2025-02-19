# Wallet Checker

A Python library to check Solana and Ethereum balances using a seed phrase.

## Installation
```sh
pip install wallet_checker
```

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