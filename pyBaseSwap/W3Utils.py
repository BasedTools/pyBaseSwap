from decimal import Decimal, ROUND_DOWN
from web3 import Web3 
from .core_abis import IERC20_ABI, MULTICALL_ABI


class W3Utils:
    """
    A utility class for interacting with the Ethereum blockchain using Web3.
    Provides helper methods for common operations like obtaining the current block number, 
    converting mnemonics to private keys, estimating gas costs, and managing token amounts 
    in different formats.
    """

    def __init__(self, settings, w3):
        """
        Initializes the W3Utils class.

        Parameters:
        -----------
        settings : object
            Configuration object containing gas-related settings like GWEI offset and max transaction fees.
        w3 : Web3 instance
            Instance of Web3 used to interact with the Ethereum blockchain.
        """
        self.settings, self.w3 = settings, w3

    def block(self):
        """
        Returns the current Ethereum block number.

        Returns:
        --------
        int
            The current block number.
        """
        return self.w3.eth.blockNumber
    
    def isPrivateKey(self, secret):
        if self.isValidPrivatKey(secret):
            return True
        else:
            return False
    
    def isValidPrivatKey(self, secret):
        if len(secret) in [64, 66] and all(c in '0123456789abcdefABCDEF' for c in secret[2:]) if secret.startswith('0x') else len(secret) == 64 and all(c in '0123456789abcdefABCDEF' for c in secret):
            return True
        return False
        
    def isValidMnomic(self, secret):
        if len(secret) in [12, 15, 18, 21, 24]:
            return True
        return False
        
    
    def getMnemonicToPrivKey(self, mnemonic, account_path: str = "m/44'/60'/0'/0/0"):
        """
        Converts a mnemonic phrase to a private key and corresponding Ethereum address.

        Parameters:
        -----------
        mnemonic : str
            The mnemonic phrase to convert to a private key.
        account_path : str, optional
            The derivation path for the HD wallet, by default "m/44'/60'/0'/0/0".

        Returns:
        --------
        tuple
            A tuple containing the Ethereum address and the private key (in hex format).
        """
        self.w3.eth.account.enable_unaudited_hdwallet_features()
        account = self.w3.eth.account.from_mnemonic(mnemonic, account_path)
        return account.address, self.w3.to_hex(account.key)
    
    def getAddresFromPrivKey(self, private_key):
        """
        Retrieves the Ethereum address associated with the provided private key.

        Parameters:
        -----------
        private_key : str
            The private key to derive the Ethereum address from.

        Returns:
        --------
        str
            The Ethereum address corresponding to the private key.
        """
        return self.w3.eth.account.from_key(str(private_key)).address

    def estimateGas(self, txn):
        """
        Estimates gas required for a transaction and checks if the gas cost is within the allowed limit.

        Parameters:
        -----------
        txn : dict
            A dictionary representing the transaction object (e.g., to, from, value, etc.).

        Returns:
        --------
        tuple
            A tuple containing:
            - int: Estimated gas amount (with 10% overhead).
            - str: Estimated gas cost in Ether.
            - bool: Whether the gas cost is within the maximum allowed transaction fee.
        """
        gas = self.w3.eth.estimate_gas(txn)
        gas_wei = gas + (gas / 10)  # Adding 10% overhead to gas
        gas_cost = self.custom_round(
            Web3.from_wei( 
                          gas * ( self.w3.eth.gas_price * (10**9)),
                          "ether"
                          )
            )
        if float(gas_cost) > float(self.settings.settings["MaxTXFeeETH"]):
            return int(gas_wei), gas_cost, False
        return int(gas_wei), gas_cost, True

    def custom_round(self, num):
        """
        Rounds a given decimal number according to specified rules based on its size.

        Parameters:
        -----------
        num : Decimal
            The number to round.

        Returns:
        --------
        Decimal
            The rounded number based on specific formatting rules.
        """
        num_str = str(self.get_human_amount(num))
        try:
            integer_part, fractional_part = num_str.split('.')
            if integer_part != '0':
                if len(integer_part) >= 4:
                    return Decimal(num).quantize(Decimal('0'), rounding=ROUND_DOWN)
                else:
                    return Decimal(num).quantize(Decimal('0.00'), rounding=ROUND_DOWN)    
            else:
                first_non_zero_idx = next((idx for idx, char in enumerate(fractional_part) if char != '0'), None)
                if len(fractional_part[first_non_zero_idx:]) >= 3:
                    total_digits = first_non_zero_idx + 4
                else:
                    total_digits = first_non_zero_idx + 2
                idx_str = "0." + "0" * (total_digits)
                return self.get_human_amount(Decimal(num).quantize(Decimal(idx_str), rounding=ROUND_DOWN))
        except Exception as e:
            return num

    def to_wei(self, token_amount: Decimal, decimals: int) -> int:
        """
        Converts a token amount from its human-readable form to the smallest unit (wei).

        Parameters:
        -----------
        token_amount : Decimal
            The amount of the token in its human-readable form.
        decimals : int
            The number of decimal places the token supports.

        Returns:
        --------
        int
            The token amount in its smallest unit (wei).
        """
        token_amount_decimal = Decimal(token_amount)
        smallest_amount = int(token_amount_decimal * (10 ** decimals))
        return smallest_amount

    def from_wei(self, token_amount: int, decimals: int) -> Decimal:
        """
        Converts a token amount from its smallest unit (wei) to its human-readable form.

        Parameters:
        -----------
        token_amount : int
            The amount of the token in its smallest unit (wei).
        decimals : int
            The number of decimal places the token supports.

        Returns:
        --------
        Decimal
            The token amount in its human-readable form.
        """
        amount_decimal = Decimal(token_amount) / (10 ** decimals)
        return amount_decimal
    
    def get_decimal_places(self, number):
        """
        Determines the number of decimal places in a given number.

        Parameters:
        -----------
        number : float or Decimal
            The number to evaluate.

        Returns:
        --------
        int
            The number of decimal places.
        """
        decimal_number = Decimal(str(number))
        decimal_places = -decimal_number.as_tuple().exponent
        return decimal_places
    
    def get_human_amount(self, number):
        """
        Formats a number with the appropriate number of decimal places for human-readable display.

        Parameters:
        -----------
        number : float or Decimal
            The number to format.

        Returns:
        --------
        str
            The formatted number as a string.
        """
        format = "{:." + f"{self.get_decimal_places(number)}" + "f}"
        decimal_number = format.format(number)
        return decimal_number
    

        

    def is_erc20_token(self, contract_address):
        """
        Check if a contract is an ERC-20 token by verifying the presence of decimals function.
        """
        try:
            self.w3.eth.call({'to': contract_address,'data': '0x313ce567'})
            return True
        except Exception as e:
            return False 
        
        
    def multicall_is_erc20_token(self, token_addresses):
        """
        Check if a list of contract addresses are ERC-20 tokens by verifying the presence of the decimals function using Multicall v3.
    
        Args:
            token_addresses (list): A list of token contract addresses to check.
    
        Returns:
            list: A list of token contract addresses that are ERC-20 tokens.
        """
        multicall_contract = self.w3.eth.contract(address="0xcA11bde05977b3631167028862bE2a173976CA11", abi=MULTICALL_ABI)
        erc20_tokens = []
        batch_size = 28
        for i in range(0, len(token_addresses), batch_size):
            current_batch = token_addresses[i:i + batch_size]
            multicall_data = [{
                'target': token_address,
                'callData': "0x313ce567"  # Function selector for decimals()
            } for token_address in current_batch]
            try:
                response = multicall_contract.functions.tryAggregate(False, multicall_data).call()
                for j, token_address in enumerate(current_batch):
                    success, return_data = response[j]
                    if success and return_data != "0x":
                        erc20_tokens.append(token_address)
            except Exception as e:
                print(f"Multicall error: {e}")
        return erc20_tokens

    def getWalletTokens(self, wallet_address: str, batch_size: int=10000, blocks_to_check: int = 150000 ):
        """
        Fetches a list of unique token addresses that have been transferred to a specified wallet address 
        within a defined range of Ethereum blocks.
        Args:
            wallet_address (str): The Ethereum address of the wallet to check for token transfers.
            batch_size (int, optional): The number of blocks to process in each batch when querying logs. Defaults to 10,000.
            blocks_to_check (int, optional): The number of past blocks to check for transfers, starting from the latest block. Defaults to 150,000.
            
        Returns:
            set: A set of token contract addresses that have transferred tokens to the specified wallet.
            
        Methodology:
            1. Retrieves the latest block number from the Ethereum blockchain.
            2. Computes the starting block based on the number of `blocks_to_check`.
            3. Creates a filter for Transfer events, looking specifically for logs where the wallet_address is the recipient.
            4. Iterates over the blocks in batches, fetching logs and extracting token addresses from the logs.
            5. Returns a set of unique token contract addresses associated with transfers to the wallet.
            
        Notes:
            - This method only checks for ERC-20 token transfer events (using the "Transfer" event signature).
            - Logs are retrieved in batches to avoid timeouts for large ranges.
            - If an error occurs during log retrieval, it will return an empty list for that batch of logs.
        """
        latest_block = self.w3.eth.block_number
        start_block = max(0, latest_block - blocks_to_check)
        transfer_event_signature = self.w3.keccak(text="Transfer(address,address,uint256)")
        wallet_address_padded = '0x' + wallet_address[2:].rjust(64, '0')
        def fetch_token_transfer_logs(start_block, end_block):
            try:
                filter_params = {
                    'fromBlock': Web3.to_hex(start_block),
                    'toBlock': Web3.to_hex(end_block),
                    'topics': [transfer_event_signature, None, wallet_address_padded]
                }
                return self.w3.eth.get_logs(filter_params)
            except Exception as e:
                print(f"Error fetching logs: {e}")
                return []
        token_addresses = []
        while start_block <= latest_block:
            end_block = min(start_block + batch_size - 1, latest_block)
            logs = fetch_token_transfer_logs(start_block, end_block)
            for log in logs:
                token_address = log['address']
                #if self.is_erc20_token(token_address):
                token_addresses.append(token_address)       
            
            start_block = end_block +1
        return list(set(self.multicall_is_erc20_token(token_addresses)))
    
    

        
        