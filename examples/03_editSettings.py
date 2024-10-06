from pyBaseSwap import BaseSwap
BS = BaseSwap(
 settings_file_path="./Settings.json", # set filename and path to config file if you need
 saveSettings=False # if you want to save settings to Settings.json file
)

print("Default Settings Dict:"),BS.printSettings()

settings = BS.getSettings()
#print(settings)

#Hardhat Node Account#0
dummy_address = "0xf39fd6e51aad88f6f4ce6ab8827279cfffb92266" #never use this in public networks!
dummy_private_key = "0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80" #never use this in public networks!

#Manual edit Settings wallet
BS.editSettings(
 key="address",
 newValue=dummy_address,
 skipReload = True # Skip reload of submodules, save time
)
BS.editSettings(key="private_key", newValue=dummy_private_key, skipReload = True)
BS.reload() 

# simple import from private key
BS.loadWalletFromPrivKey(dummy_private_key)
print("Wallet from Priv key imported, new settings:"),BS.printSettings()

BS.loadWalletFromMnomic(
   "witness explain monitor check grid depend music purchase ready title bar federal" # DONT USE in PUBLIC networks!
)
print("Wallet from Mnomic seeds imported, new settings:"), BS.printSettings()

#Lets change the rpc to a faster one like ws or wss
BS.editSettings(
    key="RPC",
    newValue="wss://base-rpc.publicnode.com", # Hardhat and Basechain  currently supported
)

settings = BS.getSettings()
print(settings["RPC"])


#Connect to Localhost Hardhat Node for testing (https://hardhat.org/hardhat-runner/docs/getting-started)
#Hardhat Node BSC fork Example (https://github.com/BasedTools/PancakeSwap_Sniper_Bot_V3andV2/tree/main/hardhat)
#BS.editSettings(
#    key="RPC",
#    newValue="http://127.0.0.1/8545", # Hardhat and BSC is currently supported
#)
