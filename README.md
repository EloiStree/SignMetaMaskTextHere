# Sign Meta Mask Text Here

Welcome 😁, you want to speak with someone having an Ethereum wallet.

- Go in the [Verify Page](https://eloistree.github.io/SignMetaMaskTextHere/VerifyText/index.html) to generate a link.
- Send him the link.
- Wait him to sign it.
- He send you back a Verify link
- Go in the link and check if he own the account.
- He is validate 👌.
- He is not 🥸 maybe you have some issue.
  - Be carefull.

**Sign a given message**: [https://eloistree.github.io/SignMetaMaskTextHere/index.html?q=guid_to_sign](https://eloistree.github.io/SignMetaMaskTextHere/index.html?q=guid_to_sign)    

**Verify a sent message**:  [https://eloistree.github.io/SignMetaMaskTextHere/VerifyText/index.html?q=message|address|signedMessage](https://eloistree.github.io/SignMetaMaskTextHere/VerifyText/index.html?q=message|address|signedMessage)  



## License: Beerware

If this code helped you, feel free to buy me a beer to pratice the tool 🍻😁.  

On Ethereum:  
- Send a transaction to this wallet: [0xDa3239C8ad5C321A1411F3acC2C1f9F8C9D34ECE](https://etherscan.io/address/0xDa3239C8ad5C321A1411F3acC2C1f9F8C9D34ECE)
- Sign your identify with the hash of the donation 
- Send me the text on [Discord](https://discord.gg/VDQqW2RYVF) with 👋>🍻 to me on Discord.




-----------------


# Sign message on device that can't have access to MetaMask.

## Coaster / Privateer Concept

MetaMask is not available on Quest3, Raspberry Pi, or your TV...

So, you need the ability to delegate actions to another private key while maintaining the association with your MetaMask public address. 

This concept introduces the **Coaster Key**.

Imagine you're at a bar, and you want a trusted friend to perform an important task on your behalf. To authorize them in your name, follow these steps:

1. **Obtain your friend’s public address**: Ask your friend for their public address.  
2. **Sign a message**: Use your private key to sign a message that includes their public address.  
3. **Record the delegation**: Write the following on a "coaster":  
   - `TheirPublicAddress`  
   - `YourPublicAddress`  
   - `TheSignedMessage`  

Now, your friend can prove they are authorized to act on your behalf.

**Example of marque's letter:**  
> 0x73e01Dcf82E50b41be3018F45200231933CAA744|0xFEEAcdE5d735B8b347D9BBF8fBd02FEd153b564A|0x1558f2c9477061382b87b11a7418a944bfa04351bde7099767460d5336949167682c99e4713c4beb1d150b8812b27f4a279ebe4dda7de2cf4405066767f615a91c  


### When Your Friend Takes Action:
1. When your friend reaches the spot where they need to act (e.g., a "guard" or gatekeeper), they initiate a conversation.  
2. The guard asks you to sign a random message frome the public address (on the"coaster") , confirming that you are indeed the original owner of the public address.  
3. The guard verifies that the two signed message are valid and matches the public address recorded on the "coaster."  
4. The guard can trust that, at one point in time, your friend had authorization to act in your name.

This concept is similar to the **Privateer Letter** in pirate lore—a letter from a king or country that authorizes a pirate to act on their behalf.
It is a public non revokable authorization. 

**Example of signed message with marque letter:**
> 2025_01_04_03_20_17_13375|0x73e01Dcf82E50b41be3018F45200231933CAA744|0x989d5d47f220b369b254197d6ba724f92c2d949851b3aa586efb99c5d47b860e059c4adee27b79f2b8168003e55a304a3ed2f847e3eeb2bef47d5b9e00e5c4a91b|0xFEEAcdE5d735B8b347D9BBF8fBd02FEd153b564A|0x1558f2c9477061382b87b11a7418a944bfa04351bde7099767460d5336949167682c99e4713c4beb1d150b8812b27f4a279ebe4dda7de2cf4405066767f615a91c

- `0x1558f2c9477061382b87b11a7418a944bfa04351bde7099767460d5336949167682c99e4713c4beb1d150b8812b27f4a279ebe4dda7de2cf4405066767f615a91c`  
  Prove that `0x73e01Dcf82E50b41be3018F45200231933CAA744` was the message signed by `0xFEEAcdE5d735B8b347D9BBF8fBd02FEd153b564A`.

- `0x989d5d47f220b369b254197d6ba724f92c2d949851b3aa586efb99c5d47b860e059c4adee27b79f2b8168003e55a304a3ed2f847e3eeb2bef47d5b9e00e5c4a91b`  
  Prove that `0x73e01Dcf82E50b41be3018F45200231933CAA744` signed `2025_01_04_03_20_17_13375`.

- If `0xFEEAcdE5d735B8b347D9BBF8fBd02FEd153b564A` is allowed on the server without a whitelist:  
  - `0x73e01Dcf82E50b41be3018F45200231933CAA744` will be logged as `0xFEEAcdE5d735B8b347D9BBF8fBd02FEd153b564A`.

- If `0xFEEAcdE5d735B8b347D9BBF8fBd02FEd153b564A` is allowed on the server with a whitelist:  
  - If `0x73e01Dcf82E50b41be3018F45200231933CAA744` is in the list:  
    - `0x73e01Dcf82E50b41be3018F45200231933CAA744` will be logged as `0xFEEAcdE5d735B8b347D9BBF8fBd02FEd153b564A`.  
  - Otherwise, `0x73e01Dcf82E50b41be3018F45200231933CAA744` is refused access.  
    - Optionally: A log is created for `0xFEEAcdE5d735B8b347D9BBF8fBd02FEd153b564A` with `0x73e01Dcf82E50b41be3018F45200231933CAA744` indicating a failed attempt.


**Whilelist line:**  
`0xFEEAcdE5d735B8b347D9BBF8fBd02FEd153b564A>0x73e01Dcf82E50b41be3018F45200231933CAA744` 

### Server Support for Coasters

If the server supports the **Coaster authentification**, you can enhance it with:  
1. **Whitelist**: Maintain a list of authorized public coaster addresses that are still valid.  
2. **Logging Webhook**: Log actions taken with the coaster. Whenever the coaster is used, notify the master key (your original public address).

--------------------------


## Recall of Why I Am Building These Tools  

As a game developer, I am exploring these solutions to:  
- Allow Quest 3 users to authenticate as a MetaMask account without accidentally leaking their private key.  
- Enable users to play without knowing they own an Ethereum wallet, with the option to link it to MetaMask later for added security.  
- Ensure users use MetaMask when playing ranked games to prevent theft caused by leaked private keys.  
  - Coaster connections allow users to play and interact but do not permit them to recover prizes or perform administrative actions on the server(s).  
- Create tools that do not require a database, making them accessible to young learners who want to build their own servers.  


