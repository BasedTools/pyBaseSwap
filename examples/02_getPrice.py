from pyBaseSwap import BaseSwap
BS = BaseSwap()
#Hi Sam!

BS.changeToken(
  "0x4621b7A9c75199271F773Ebd9A499dbd165c3191" #Dola USD Stablecoin (DOLA)
)

symbol = BS.IERC20.get_token_Symbol() # get symbol
usdPrice = BS.getUSDPrice() # get usd price
liquidity = BS.getLiquidityUSD() # get Liquidity in usd


print(
f"""
TokenSymbol: {symbol}
Token Price: {usdPrice} $
Token Liquidity: {liquidity} $
"""
)

# ok, we can print floats better
clean_price = BS.w3U.custom_round(usdPrice)
clean_liquidity = BS.w3U.custom_round(liquidity)

print(
f"""
TokenSymbol: {symbol}
Token Price: {clean_price} $
Token Liquidity: {clean_liquidity} $
"""
)

#Gater some information about the token, its simulate buy and sell transaction to calculate Token Fees/loss
#Check token infos, Tax and simulate a Buy and Sell transaction to check for honeypot
buy_tax, sell_tax, ishoneypot = BS.getTokenInfos() 
print(
f"""
Is Token Scam/Honeypot? : {ishoneypot}
Tax On Buy Transaction:  {buy_tax}%
Tax On Sell Transaction:  {sell_tax}%
""")
if not ishoneypot:
  print("No honeypot, lets check bestPool")
  baseToken = BS.getBestPool()
  print(baseToken)