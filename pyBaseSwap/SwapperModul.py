from .W3Utils import W3Utils
from .core_settings import CoreSettings
from .core_chains import chains
from .IERC20 import IERC20
from .ISwapperContract import InterfaceSwapperContract  
from web3 import Web3
import  json

class BaseSwap(InterfaceSwapperContract, W3Utils, IERC20):
    """
    A module for interacting with decentralized exchanges (DEX) and managing token swaps on the blockchain.

    Attributes:
        token (str): The address of the token to interact with.
        settings (CoreSettings): Settings for the swapper, loaded from a configuration file.
        w3 (Web3): The Web3 connection to the blockchain.
        w3U (W3Utils): Utility class for Web3 interactions.
        IERC20 (IERC20): Contract interface for the ERC-20 token being swapped.
        IAC (InterfaceSwapperContract): Interface for interacting with the swapper contract.

    Args:
        token (str): The token address to initialize. If not provided, falls back to BasedTools Governance Token.
        settings_file_path (str): The path to the settings file (default is "./Settings.json").
        saveSettings (bool): Flag to save settings changes back to the file (default is False).
    """
    def __init__(self, token:str=None, settings_file_path:str="./Settings.json", saveSettings:bool=False):
        """
        Initialize the swapper module, set up the Web3 connection, and load token and contract interfaces.

        Args:
            token (str, optional): The token address for interactions (in checksum format).
            settings_file_path (str, optional): Path to the settings JSON file. Defaults to "./Settings.json".
            saveSettings (bool, optional): Whether to save changes to the settings file. Defaults to False.
        """
        self.settings = CoreSettings(settings_file_path,  saveSettings)
        self.w3 = self.connect()
        W3Utils.__init__(self, self.settings, self.w3)
        if Web3.is_address(token):
            self.token = Web3.to_checksum_address(token)
            pass
        else:
            print("No Token Addresss Provided fallback to USDC")
            self.token = chains(self.w3.eth.chain_id).BTT
            
        IERC20.__init__(self, self.settings, self.w3, Web3.to_checksum_address(self.token), self)
        InterfaceSwapperContract.__init__(self, self.settings, self.w3, self, self)

    def reload(self):
        """
        Reload the Web3 connection, utilities, and contract interfaces after a settings change.
        """
        self.w3 = self.connect()
        IERC20.__init__(self, self.settings, self.w3, Web3.to_checksum_address(self.token), self)
        InterfaceSwapperContract.__init__(self, self.settings, self.w3, self, self)
        W3Utils.__init__(self, self.settings, self.w3)

    def connect(self):
        """
        Establish a Web3 connection using the RPC endpoint specified in settings.

        Returns:
            Web3: The Web3 instance connected to the specified RPC endpoint.
        """
        keys = self.settings.settings
        if keys["RPC"][:2].lower() == "ws":
            w3 = Web3(Web3.LegacyWebSocketProvider(keys["RPC"],websocket_timeout=keys["timeout"]))
        else:
            w3 = Web3(Web3.HTTPProvider(keys["RPC"], request_kwargs={'timeout': int(keys["timeout"])}))
        return w3
    
    def check_settings(self) -> str:
        """
        Validate the critical settings such as address and private key.

        Returns:
            str: Message indicating the validation result of settings.
        """
        if self.settings.settings.get("address") and not Web3.is_address(self.settings.settings["address"]):
            return "Invalid address in settings!"
        if len(self.settings.settings.get("private_key")) and len(self.settings.settings["private_key"]) not in [64, 66]:
            return"Invalid private_key in settings!"
        return "Address Setup is done"
    
    def printSettings(self):
        """
        Print the current settings in a formatted JSON style.
        """
        print(json.dumps(self.settings.settings, indent=4))
        
    def loadWalletFromMnomic(self, mnemoic):
        """
        Load a wallet from a mnemonic phrase and update the address and private key in the settings.

        Args:
            mnemoic (str): The mnemonic phrase to derive the wallet from.
        """
        mne_address, private_key = self.w3U.getMnemonicToPrivKey(mnemoic)
        self.editSettings("address", mne_address, skipReload=True)
        self.editSettings("private_key", private_key)

    def loadWalletFromPrivKey(self, private_key):
        """
        Load a wallet from a private key and update the address in the settings.

        Args:
            private_key (str): The private key for the wallet.
        """
        address = self.w3U.getAddresFromPrivKey(private_key)
        self.editSettings("address", address, skipReload=True)
        self.editSettings("private_key", private_key)

    def changeRPC(self, newRPC):
        """
        Change the RPC endpoint in the settings and reload the connection.

        Args:
            newRPC (str): The new RPC endpoint to use.
        """
        self.editSettings("RPC", newRPC)

    def editSettings(self, key, newValue, skipReload:bool = False):
        """
        Edit a setting in the configuration and optionally reload the connection.

        Args:
            key (str): The key of the setting to change.
            newValue (any): The new value for the setting.
            skipReload (bool, optional): Whether to skip reloading the connection after changing the setting. Defaults to False.
        """
        self.settings.change_settings(key, newValue)
        if not skipReload:
            self.reload()

    def getSettings(self):
        """
        Retrieve the current settings.

        Returns:
            dict: The settings dictionary.
        """
        return self.settings.settings
        
    def changeToken(self, token:str):
        """
        Change the token being swapped and reload the token and contract interfaces.

        Args:
            token (str): The new token address (in checksum format).
        """
        self.token = Web3.to_checksum_address(token)
        IERC20.__init__(self, self.settings, self.w3, token, self)
        InterfaceSwapperContract.__init__(self, self.settings, self.w3, self, self)