from setuptools import setup, find_packages

setup(
    name="wallet_checker",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "solana",
        "solders",
        "bip_utils",
        "web3"
    ],
    author="Your Name",
    description="A Python library to check Solana and Ethereum balances using a seed phrase.",
    url="https://github.com/DragonS-DS/wallet_checker",  # Update with your repo URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
