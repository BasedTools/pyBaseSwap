from pyBaseSwap import BaseSwap

BS = BaseSwap()


tokens = BS.getWalletAssets(
    wallet_address="0xcf48e4193C50bF9a18BAA02bF7b68bAB6f385948", # Wallet addres to track
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
