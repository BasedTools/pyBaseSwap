from pyBaseSwap import BaseSwap

# The `BaseSwap`(BS) is a class that provides submoduls and functions to interact with ERC20 Smart Contracts and AMM (DEXs) from version 2 to 3.
BS = BaseSwap()
#BS have kids that priovide good work to him.
#Here is IERC20, sams kid to do work with Token Contract Functions, you can call him like so 
#BS.IERC20
#Lets give IERC20 a Job: Print token name
print(
  BS.IERC20.get_token_Name() # Token Name
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
#What token it is?? IERC20!!
print(
  BS.IERC20.get_token_Name()
)
print(
  BS.getUSDPrice()
  )

print(
  BS.getLiquidityUSD()
  )