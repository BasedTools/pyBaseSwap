from pyBaseSwap import BaseSwap

BS = BaseSwap()


tokens = BS.getWalletAssets(
    wallet_address="0x304eC59cad4060856D6796Ff948fA3f5Adb322fa", # Wallet addres to check
    batch_size=10000, # Keep batch size reasonable; logs may restrict to processing only 1024+ blocks at a time
    blocks_to_check=100000 #  be cautious of long processing times and potential RPC rate limits
    )

# Initialize WalletTokenBalance
WalletTokenBalance = 0.0
print(type(tokens)) 
#Iterate through the tokens
for i, token in enumerate(tokens):
    # Print details of each token
    print()
    print(f"Name: {token['Name']}, Symbol: {token['Symbol']}")
    print(f"USD Price: {BS.get_human_amount(float(token['USDPrice']))}")
    print(f"Balance USD: {BS.get_human_amount(float(token['BalanceUSD']))}")
    # Add the token's BalanceUSD to the WalletTokenBalance
    WalletTokenBalance += float(token["BalanceUSD"])

#Print the total Wallet Token Balance in USD
print(f"\nTotal Wallet Balance: {round(WalletTokenBalance,2)}$")
