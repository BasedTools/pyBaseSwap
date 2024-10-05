from pyBaseSwap.SwapperModul import BaseSwap

BS = BaseSwap()



tokens = BS.getWalletAssets(
    wallet_address="0xcf48e4193C50bF9a18BAA02bF7b68bAB6f385948",
    batch_size=10000,
    blocks_to_check=200000
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
