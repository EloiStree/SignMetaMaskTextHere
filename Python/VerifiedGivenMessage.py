# pip install web3
from web3 import Web3
import os
from eth_account.messages import encode_defunct
import uuid

# Initialize web3
w3 = Web3()

# Valie: EloiTeaching|0x8d89a85Dc2bC67CfD439D6BFD8b328a5e2A82B95|0f5a788e654e3a6597b0bd684c86d8bf3e73cec6414ed9a29440a534199d7757743be7b0f99824fe9fae19cebc69392d0168835671d3dfe0eefdf107f0eedbef1c
message = "EloiTeaching"
address = "0x8d89a85Dc2bC67CfD439D6BFD8b328a5e2A82B95"
signature = "0f5a788e654e3a6597b0bd684c86d8bf3e73cec6414ed9a29440a534199d7757743be7b0f99824fe9fae19cebc69392d0168835671d3dfe0eefdf107f0eedbef1c"

text = message + "|" + address + "|" + signature


def is_message_signed(given_message):
    
    split_message = given_message.split("|")
    if len(split_message) < 3:
        return False
    message = split_message[0]
    address = split_message[1]
    signature = split_message[2]
    return is_message_signed_from_params(message, address, signature )

def is_message_signed_from_params(message, address, signature):
    # Message to verify

    # Encode the message
    encoded_message = encode_defunct(text=message)

    # Recover the address from the signature
    recovered_address = w3.eth.account.recover_message(encoded_message, signature=signature)
    return  recovered_address.lower() == address.lower()


print(is_message_signed(text))
while True:
    string_input = input("Enter the message to sign: ")
    if is_message_signed(string_input):
        print("The message is valide/sign")
    else:
        print("The message is not valide") 
    
