from pyBaseSwap import BaseSwap


BS = BaseSwap()

print(
  BS.get_token_Name() # Token Name
)

#and now here is IAC he do all the work for Automatet marketmakers in the world of Dex
#IAC give us the price from current initalized token
print(
  BS.getUSDPrice()
  )
#BS change the Token!
BS.changeToken(
  "0x65e570b560027F493f2b1907e8e8e3B9546053bD"
)
#What token it is?? 
print(
  BS.get_token_Name()
)
print(
  BS.getUSDPrice()
  )

print(
  BS.getLiquidityUSD()
  )