"""
In this code we generate a random private key form Web3 that is compatible in MetaMask format.
(Replace with yours if you want to try with your private key)
From this key we sign a given messsage that we are able to copy past.
"""


# pip install web3
from web3 import Web3
import os
from eth_account.messages import encode_defunct
import uuid

# Generate a random private key
private_key = os.urandom(32).hex()
# Print the private key
print(f"Private Key: {private_key}")

# Create a Web3 instance
w3 = Web3()

# Generate the corresponding public address
account = w3.eth.account.from_key(private_key)
print(f"Public Address: {account.address}")

# Sign a message with the private key
to_sign = "EloiTeaching"

def sign_message(private_key, to_sign):
    m = to_sign
    message_hash = w3.keccak(text=m)
    m = encode_defunct(text=m)
    signed_message = w3.eth.account.sign_message(m, private_key=private_key)
    # Print the signed message
    print(f"Signed Message: {signed_message.signature.hex()}")
    MESSAGE = to_sign
    PUBLIC_ADDRESS = account.address
    SIGNED_MESSAGE = signed_message.signature.hex()
    print("Clipboardable format: ")
    print(f"{MESSAGE}|{PUBLIC_ADDRESS}|{SIGNED_MESSAGE}")

TWITCH_CLIENT_ID = "EloiTeaching"
sign_message(private_key, TWITCH_CLIENT_ID)

GIVEN_GUID = uuid.uuid4()
sign_message(private_key, str(GIVEN_GUID))

while True:
    console_input = input("Enter a message to sign: ")
    sign_message(private_key, console_input)
