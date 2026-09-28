SOLANA_RPC_URL = "https://api.mainnet-beta.solana.com"
ETH_RPC_URL = "https://rpc.ankr.com/eth"


def get_solana_keypair_from_mnemonic(mnemonic_phrase: str):
    from bip_utils import Bip32Slip10Ed25519, Bip39SeedGenerator
    from solders.keypair import Keypair

    seed_bytes = Bip39SeedGenerator(mnemonic_phrase).Generate(passphrase="")[:64]
    bip32_ctx = Bip32Slip10Ed25519.FromSeed(seed_bytes)
    derived = bip32_ctx.DerivePath("m/44'/501'/0'/0'")
    private_key = derived.PrivateKey().Raw().ToBytes()
    keypair = Keypair.from_seed(private_key[:32])
    return keypair

def get_ethereum_address_from_mnemonic(mnemonic_phrase: str) -> str:
    from bip_utils import Bip39SeedGenerator, Bip44, Bip44Coins
    from web3 import Web3

    seed_bytes = Bip39SeedGenerator(mnemonic_phrase).Generate(passphrase="")
    bip44_ctx = Bip44.FromSeed(seed_bytes, Bip44Coins.ETHEREUM).DeriveDefaultPath()
    private_key = bip44_ctx.PrivateKey().Raw().ToBytes()
    eth_account = Web3().eth.account.from_key(private_key)
    return eth_account.address


def get_solana_balance(mnemonic_phrase: str):
    """Return the first Solana account derived from a BIP-39 mnemonic."""
    from solana.rpc.api import Client

    keypair = get_solana_keypair_from_mnemonic(mnemonic_phrase)
    pubkey = keypair.pubkey()
    response = Client(SOLANA_RPC_URL).get_balance(pubkey)
    if hasattr(response, 'value') and response.value is not None:
        return {"Solana Wallet Address": str(pubkey), "SOL Balance": response.value / 1e9}
    return {"error": "Failed to retrieve Solana balance."}


def get_ethereum_balance(mnemonic_phrase: str):
    """Return the first Ethereum account derived from a BIP-39 mnemonic."""
    from web3 import Web3

    eth_address = get_ethereum_address_from_mnemonic(mnemonic_phrase)
    web3 = Web3(Web3.HTTPProvider(ETH_RPC_URL))
    balance_wei = web3.eth.get_balance(eth_address)
    balance_eth = balance_wei / 1e18
    return {"Ethereum Wallet Address": eth_address, "ETH Balance": balance_eth}


def get_wallet_balances(seed_phrase: str):
    """Return Solana and Ethereum balances derived from a BIP-39 mnemonic."""
    sol_balance = get_solana_balance(seed_phrase)
    eth_balance = get_ethereum_balance(seed_phrase)
    return {"solana": sol_balance, "ethereum": eth_balance}