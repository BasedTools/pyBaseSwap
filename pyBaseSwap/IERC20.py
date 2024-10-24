from web3 import Web3
from .core_abis import IERC20_ABI  # Import the ERC-20 ABI, adjust the import path as necessary
from .core_chains import chains  # Import the chains class, adjust the import path as necessary

class IERC20:
    """
    A class to interact with ERC-20 token contracts on the Ethereum blockchain.

    This class provides methods to retrieve token balances, approve spending,
    and manage allowances for ERC-20 tokens. It leverages the Web3.py library 
    to communicate with the Ethereum network and requires the ERC-20 ABI to 
    function correctly.

    Attributes:
        settings: Core settings for managing RPC connection and user account.
        user_address (str): User's wallet address from settings.
        priv_key (str): User's private key for signing transactions.
        w3 (Web3): Web3 instance for blockchain interaction.
        token (str): ERC-20 token contract address.
        w3U: Utility object for helper functions.
        chain: Chain instance associated with the current network.
        token_Instance: Contract instance of the ERC-20 token.
    """
    
    def __init__(self, settings, w3, token, w3U):
        """
        Initializes the IERC20 class for interacting with ERC-20 tokens.
        - `settings`: Core settings for managing RPC connection and user account.
        - `w3`: Web3 instance for blockchain interaction.
        - `token`: ERC-20 token address.
        - `w3U`: Utility class for helper functions like converting Wei.
        """
        self.settings = settings  # Store settings object
        self.user_address = settings.settings["address"]  # User's wallet address from settings
        self.priv_key = settings.settings["private_key"]  # User's private key for signing transactions
        self.w3 = w3  # Web3 instance for blockchain connection
        self.token = token  # ERC-20 token contract address
        self.w3U = w3U  # Utility object for helper functions
        self.chain = chains(self.w3.eth.chain_id)  # Chain setup using the chain ID from Web3 instance
        self.token_Instance = self.init_token_instance()  # Initialize the ERC-20 contract instance
        
    def init_token_instance(self):
        """
        Initializes and returns the ERC-20 contract instance.
        """
        token_Instance = self.w3.eth.contract(
            address=Web3.to_checksum_address(self.token), abi=IERC20_ABI)  # Create contract instance with token address and ABI
        return token_Instance
    
    
    def get_token_balance_Of_Owner_(self, token_address, owner_address):
        """
        Returns the balance of the token_address from owner_address  in  Wei.
        - `token_address`: Token Address to check the balance for.
        - `owner_address`: Address to check the balance for.
        """
        token_Instance = self.w3.eth.contract(
            address=Web3.to_checksum_address(token_address), abi=IERC20_ABI)
        
        return token_Instance.functions.balanceOf(owner_address).call()
    
    
    def get_token_balance_Of_Owner(self, token_address, owner_address):
        """
        Returns the balance of the token_address from owner_address in a human-readable format (converted from Wei).
        - `token_address`: Token Address to check the balance for.
        - `owner_address`: Address to check the balance for.
        """
        token_Instance = self.w3.eth.contract(
            address=Web3.to_checksum_address(token_address), abi=IERC20_ABI)
        
        return self.w3U.from_wei(token_Instance.functions.balanceOf(owner_address).call(), token_Instance.functions.decimals().call())  # Convert from Wei based on token decimals
    
    def get_token_balanceOf(self, address):
        """
        Returns the balance of the token in a human-readable format (converted from Wei).
        - `address`: Address to check the balance for.
        """
        return self.w3U.from_wei(self.get_token_balance_(address), self.get_token_decimals())  # Convert from Wei based on token decimals
    
    def get_token_balanceOf_(self, address):
        """
        Returns the balance of the token in Wei.
        - `address`: Address to check the balance for.
        """
        return self.get_token_balance_(address)
    
    def get_token_balance_(self):
        """
        Returns the user's token balance in Wei.
        """
        return self.get_token_balance_(self.user_address)  # Use the user's own address for balance lookup
    
    def get_token_balance(self):
        """
        Returns the user's token balance in a human-readable format (converted from Wei).
        """
        return self.w3U.from_wei(self.get_token_balance_(self.user_address), self.get_token_decimals())  # Convert from Wei
    
    def get_token_allowance(self, spender):
        """
        Returns the token allowance for a specific spender in a human-readable format (converted from Wei).
        - `spender`: Address of the spender to check allowance for.
        """
        return self.w3U.from_wei(self.get_token_allowance_(spender), self.get_token_decimals())
    
    def get_token_address(self):
        """
        Returns the token's contract address.
        """
        return Web3.to_checksum_address(self.token_Instance.address)  # Convert to checksum address format
    

    def get_token_decimals(self):
        """
        Returns the number of decimals for the token (used for conversion from Wei).
        """
        return self.token_Instance.functions.decimals().call()  # Calls the `decimals` function on the ERC-20 token contract

    def get_token_Name(self):
        """
        Returns the name of the token.
        """
        return self.token_Instance.functions.name().call()  # Calls the `name` function on the ERC-20 token contract

    def get_token_Symbol(self):
        """
        Returns the symbol of the token.
        """
        return self.token_Instance.functions.symbol().call()  # Calls the `symbol` function on the ERC-20 token contract
    
    def get_token_balance_(self, address):
        """
        Returns the token balance in Wei for a specific address.
        - `address`: Address to check the balance for.
        """
        return self.token_Instance.functions.balanceOf(Web3.to_checksum_address(address)).call()  # Calls the `balanceOf` function
    
    def get_token_allowance(self, spender):
        """
        Returns the token allowance for a spender in Wei.
        - `spender`: Address of the spender.
        """
        return self.token_Instance.functions.allowance(self.user_address, spender).call()  # Calls the `allowance` function
    
    def approveSwapper_(self, amountIn: int = 0):
        """
        Approves the maximum amount for the Swapper contract to spend tokens.
        - `amount`: Amount to approve in Wei.
        """
        return self.approve(self.chain.BTTSwapper, amountIn)
    
    def approveSwapper(self, amountIn: float = 0):
        """
        Approves a specific amount for the Swapper contract to spend, converting from a human-readable format to Wei.
        - `amount`: Amount to approve.
        """
        return self.approve(self.chain.BTTSwapper, self.w3U.to_wei(amountIn, self.get_token_decimals()))  # Convert amount to Wei based on token decimals
    
    def is_approved(self, spender, amountIn):
        """
        Checks if the spender is already approved for a given amount.
        - `spender`: Address of the spender.
        - `amountIn`: Amount to check for approval.
        """
        allowance = self.get_token_allowance(spender)  # Get current allowance for spender
        return int(allowance) >= int(amountIn)  # Check if the allowance is greater than or equal to the required amount
    
    def approve(self, spender, amountIn: int = 0):
        """
        Approves the spender to spend a specified amount of tokens on the user's behalf.
        - `spender`: Address of the spender.
        - `amountIn`: Amount to approve (default is 0, meaning full approval).
        """
        approveAmount = 2**256 - 1  # Set the approval amount to max (2^256 - 1)
        if amountIn > 0:
            approveAmount = amountIn 
        if not self.is_approved(spender, amountIn):
            # Use the specified amount if it's greater than 0
            txn = self.token_Instance.functions.approve(
                Web3.to_checksum_address(spender),
                approveAmount
            ).build_transaction({
                'from': self.user_address,
                'gasPrice': self.w3.eth.gas_price,  # Add gas price offset
                'nonce': self.w3.eth.get_transaction_count(self.user_address),
                'value': 0
            })
            gas = self.w3U.estimateGas(txn)  # Estimate gas cost for the transaction
            txn.update({'gas': int(gas[0])})  # Update transaction with the estimated gas
            signed_txn = self.w3.eth.account.sign_transaction(
                txn,
                self.priv_key  # Sign the transaction with the user's private key
            )
            txn = self.w3.eth.send_raw_transaction(signed_txn.raw_transaction)  # Send the signed transaction
            txn_receipt = self.w3.eth.wait_for_transaction_receipt(
                txn, timeout=self.settings.settings["timeout"])  # Wait for transaction receipt
            if txn_receipt['status'] == 1:  # Check if the transaction was successful
                return True, txn.hex(), gas
            else:
                return False, txn.hex(), gas
        else:
            return True, "0", "Already Approved"  # Return if already approved
