from pyBaseSwap import BaseSwap
import time

BS = BaseSwap(
    "0x940181a94A35A4569E4529A3CDfB74e38FD98631" # Token Aerodrome (AERO)
)

target_price = 0.90
input_amount = 0.001 # ETH input
#Hardhat Node Account#0
address = "0xf39fd6e51aad88f6f4ce6ab8827279cfffb92266" #never use this in public networks!
private_key = "0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80" #never use this in public networks!

BS.editSettings("address", address )
BS.editSettings("private_key", private_key )


while True:
    time.sleep(1)
    currentTokenPrice = BS.getUSDPrice()
    print("Token Price:",currentTokenPrice, end="\r")
    if currentTokenPrice <= target_price:
        BS.SwapETHtoToken(input_amount)
