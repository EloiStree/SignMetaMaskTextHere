
# Tested byt creating a private key and add it to MetaMask.
from web3 import Web3
import os
private_key = os.urandom(32).hex()
print(f"Private Key: {private_key}")
w3 = Web3()
account = w3.eth.account.from_key(private_key)
print(f"Public Address: {account.address}")
