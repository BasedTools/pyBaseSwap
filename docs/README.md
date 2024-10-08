<a id="core_abis"></a>

# core\_abis

<a id="core_chains"></a>

# core\_chains

<a id="core_chains.chains"></a>

## chains Objects

```python
class chains()
```

<a id="core_chains.chains.__init__"></a>

#### \_\_init\_\_

```python
def __init__(chainID)
```

Initializes the chains class with specific settings based on the provided chain ID.
- `chainID`: The ID of the blockchain network. Supported IDs are 8453 (Base) and 31337 (Local Hardhat).

<a id="core_settings"></a>

# core\_settings

<a id="core_settings.CoreSettings"></a>

## CoreSettings Objects

```python
class CoreSettings()
```

<a id="core_settings.CoreSettings.__init__"></a>

#### \_\_init\_\_

```python
def __init__(settings_file_path: str = "Settings.json",
             saveSetting: bool = False)
```

Initializes the CoreSettings class.
- `settings_file_path`: Path to the JSON file where settings are stored.
- `saveSetting`: If True, changes in settings will be saved to the file.

<a id="core_settings.CoreSettings.reinit_settings"></a>

#### reinit\_settings

```python
def reinit_settings()
```

Resets settings to default and reloads from the settings file.

<a id="core_settings.CoreSettings.load_settings"></a>

#### load\_settings

```python
def load_settings()
```

Loads the settings from the JSON file.
If the file doesn't exist or there's an error, it creates a new file with default settings.

<a id="core_settings.CoreSettings.save_settings_to_file"></a>

#### save\_settings\_to\_file

```python
def save_settings_to_file()
```

Saves the current settings to the JSON file.

<a id="core_settings.CoreSettings.change_settings"></a>

#### change\_settings

```python
def change_settings(key: str, new_value)
```

Changes a specific setting by its key and saves it to the file if required.
- `key`: The setting to be changed.
- `new_value`: The new value for the setting.

<a id="IERC20"></a>

# IERC20

<a id="IERC20.IERC20"></a>

## IERC20 Objects

```python
class IERC20()
```

A class to interact with ERC-20 token contracts on the Ethereum blockchain.

This class provides methods to retrieve token balances, approve spending,
and manage allowances for ERC-20 tokens. It leverages the Web3.py library
to communicate with the Ethereum network and requires the ERC-20 ABI to
function correctly.

**Attributes**:

- `settings` - Core settings for managing RPC connection and user account.
- `user_address` _str_ - User's wallet address from settings.
- `priv_key` _str_ - User's private key for signing transactions.
- `w3` _Web3_ - Web3 instance for blockchain interaction.
- `token` _str_ - ERC-20 token contract address.
- `w3U` - Utility object for helper functions.
- `chain` - Chain instance associated with the current network.
- `token_Instance` - Contract instance of the ERC-20 token.

<a id="IERC20.IERC20.__init__"></a>

#### \_\_init\_\_

```python
def __init__(settings, w3, token, w3U)
```

Initializes the IERC20 class for interacting with ERC-20 tokens.
- `settings`: Core settings for managing RPC connection and user account.
- `w3`: Web3 instance for blockchain interaction.
- `token`: ERC-20 token address.
- `w3U`: Utility class for helper functions like converting Wei.

<a id="IERC20.IERC20.init_token_instance"></a>

#### init\_token\_instance

```python
def init_token_instance()
```

Initializes and returns the ERC-20 contract instance.

<a id="IERC20.IERC20.get_token_balanceOf"></a>

#### get\_token\_balanceOf

```python
def get_token_balanceOf(address)
```

Returns the balance of the token in a human-readable format (converted from Wei).
- `address`: Address to check the balance for.

<a id="IERC20.IERC20.get_token_balanceOf_"></a>

#### get\_token\_balanceOf\_

```python
def get_token_balanceOf_(address)
```

Returns the balance of the token in Wei.
- `address`: Address to check the balance for.

<a id="IERC20.IERC20.get_token_balance_"></a>

#### get\_token\_balance\_

```python
def get_token_balance_()
```

Returns the user's token balance in Wei.

<a id="IERC20.IERC20.get_token_balance"></a>

#### get\_token\_balance

```python
def get_token_balance()
```

Returns the user's token balance in a human-readable format (converted from Wei).

<a id="IERC20.IERC20.get_token_allowance"></a>

#### get\_token\_allowance

```python
def get_token_allowance(spender)
```

Returns the token allowance for a specific spender in a human-readable format (converted from Wei).
- `spender`: Address of the spender to check allowance for.

<a id="IERC20.IERC20.get_token_address"></a>

#### get\_token\_address

```python
def get_token_address()
```

Returns the token's contract address.

<a id="IERC20.IERC20.get_token_decimals"></a>

#### get\_token\_decimals

```python
def get_token_decimals()
```

Returns the number of decimals for the token (used for conversion from Wei).

<a id="IERC20.IERC20.get_token_Name"></a>

#### get\_token\_Name

```python
def get_token_Name()
```

Returns the name of the token.

<a id="IERC20.IERC20.get_token_Symbol"></a>

#### get\_token\_Symbol

```python
def get_token_Symbol()
```

Returns the symbol of the token.

<a id="IERC20.IERC20.get_token_balance_"></a>

#### get\_token\_balance\_

```python
def get_token_balance_(address)
```

Returns the token balance in Wei for a specific address.
- `address`: Address to check the balance for.

<a id="IERC20.IERC20.get_token_allowance"></a>

#### get\_token\_allowance

```python
def get_token_allowance(spender)
```

Returns the token allowance for a spender in Wei.
- `spender`: Address of the spender.

<a id="IERC20.IERC20.approveSwapper_"></a>

#### approveSwapper\_

```python
def approveSwapper_(amount)
```

Approves the maximum amount for the Swapper contract to spend tokens.
- `amount`: Amount to approve in Wei.

<a id="IERC20.IERC20.approveSwapper"></a>

#### approveSwapper

```python
def approveSwapper(amount)
```

Approves a specific amount for the Swapper contract to spend, converting from a human-readable format to Wei.
- `amount`: Amount to approve.

<a id="IERC20.IERC20.is_approved"></a>

#### is\_approved

```python
def is_approved(spender, amountIn)
```

Checks if the spender is already approved for a given amount.
- `spender`: Address of the spender.
- `amountIn`: Amount to check for approval.

<a id="IERC20.IERC20.approve"></a>

#### approve

```python
def approve(spender, amountIn: int = 0)
```

Approves the spender to spend a specified amount of tokens on the user's behalf.
- `spender`: Address of the spender.
- `amountIn`: Amount to approve (default is 0, meaning full approval).

<a id="ISwapperContract"></a>

# ISwapperContract

<a id="ISwapperContract.InterfaceSwapperContract"></a>

## InterfaceSwapperContract Objects

```python
class InterfaceSwapperContract()
```

Interface for interacting with a blockchain-based token swapper smart contract.

This class provides methods for querying token prices, liquidity, swapping tokens,
and building transactions for multiple token swap protocols (V2 and V3).

<a id="ISwapperContract.InterfaceSwapperContract.__init__"></a>

#### \_\_init\_\_

```python
def __init__(settings, w3, IERC20, w3U)
```

Initializes the InterfaceSwapperContract instance with Web3 and token contract information.

**Arguments**:

- `settings`: Object containing configuration and user settings.
- `w3`: Web3 instance to interact with Ethereum-like blockchain.
- `IERC20`: Interface for interacting with ERC20 tokens.
- `w3U`: Utility functions for Web3-related conversions.

<a id="ISwapperContract.InterfaceSwapperContract.initRouter"></a>

#### initRouter

```python
def initRouter()
```

Initializes and returns the swapper smart contract.

**Returns**:

Web3 contract instance of the swapper.

<a id="ISwapperContract.InterfaceSwapperContract.getAmountsOutV3"></a>

#### getAmountsOutV3

```python
def getAmountsOutV3(pools, path, amountIn)
```

Fetches the amount of tokens obtainable from a V3 swap route.

**Arguments**:

- `pools`: List of pool addresses involved in the V3 swap.
- `path`: Token addresses specifying the swap path.
- `amountIn`: Input amount of tokens.

**Returns**:

The output token amount for the given input and path.

<a id="ISwapperContract.InterfaceSwapperContract.getAmountsOutV2"></a>

#### getAmountsOutV2

```python
def getAmountsOutV2(amountIn, path, dexPath)
```

Fetches the amount of tokens obtainable from a V2 swap route.

**Arguments**:

- `amountIn`: Input amount of tokens.
- `path`: Token addresses specifying the swap path.
- `dexPath`: Decentralized exchanges involved in the swap.

**Returns**:

The output token amount for the given input and path.

<a id="ISwapperContract.InterfaceSwapperContract.getUSDPrice_"></a>

#### getUSDPrice\_

```python
def getUSDPrice_()
```

Fetches the USD price of the current token from the contract (raw Wei format).

**Returns**:

Token price in USD (Wei).

<a id="ISwapperContract.InterfaceSwapperContract.getUSDPrice"></a>

#### getUSDPrice

```python
def getUSDPrice()
```

Fetches the USD price of the current token and converts it to Ether format.

**Returns**:

Token price in USD (Ether).

<a id="ISwapperContract.InterfaceSwapperContract.getUSDPriceOf"></a>

#### getUSDPriceOf

```python
def getUSDPriceOf(tokenAddress)
```

Fetches the USD price of a specified token and converts it to Ether format.

**Arguments**:

- `tokenAddress`: Address of the token.

**Returns**:

Token price in USD (Ether).

<a id="ISwapperContract.InterfaceSwapperContract.getUSDPriceOf_"></a>

#### getUSDPriceOf\_

```python
def getUSDPriceOf_(tokenAddress)
```

Fetches the ETH price of a specified token (raw Wei format).

**Arguments**:

- `tokenAddress`: Address of the token.

**Returns**:

Token price in ETH (Wei).

<a id="ISwapperContract.InterfaceSwapperContract.getTokenETHPrice_"></a>

#### getTokenETHPrice\_

```python
def getTokenETHPrice_(tokenAddress)
```

Fetches the ETH price of a specified token (raw Wei format).

**Arguments**:

- `tokenAddress`: Address of the token.

**Returns**:

Token price in ETH (Wei).

<a id="ISwapperContract.InterfaceSwapperContract.getTokenETHPrice"></a>

#### getTokenETHPrice

```python
def getTokenETHPrice(tokenAddress)
```

Fetches the ETH price of a specified token (ether format).

**Arguments**:

- `tokenAddress`: Address of the token.

**Returns**:

Token price in ETH (Ether).

<a id="ISwapperContract.InterfaceSwapperContract.geNativPrice_"></a>

#### geNativPrice\_

```python
def geNativPrice_()
```

Fetches the USD price of Wrapped ETH (WETH) from the contract (raw Wei format).

**Returns**:

WETH price in USD (Wei).

<a id="ISwapperContract.InterfaceSwapperContract.getNativPrice"></a>

#### getNativPrice

```python
def getNativPrice()
```

Fetches the USD price of  ETH (WETH) and converts it to Ether format.

**Returns**:

WETH price in USD (Ether).

<a id="ISwapperContract.InterfaceSwapperContract.getAmountsOutTokenToETH_"></a>

#### getAmountsOutTokenToETH\_

```python
def getAmountsOutTokenToETH_(inputAmount: int)
```

Fetches the output token amount when swapping from ETH to the current token.

**Arguments**:

- `inputAmount`: Input ETH amount.

**Returns**:

Output token amount in Wei.

<a id="ISwapperContract.InterfaceSwapperContract.getAmountsOutETHToToken_"></a>

#### getAmountsOutETHToToken\_

```python
def getAmountsOutETHToToken_(inputAmount: int)
```

Fetches the output token amount when swapping from ETH to the current token.

**Arguments**:

- `inputAmount`: Input ETH amount.

**Returns**:

Output token amount in Wei.

<a id="ISwapperContract.InterfaceSwapperContract.getAmountsOutTokenToToken_"></a>

#### getAmountsOutTokenToToken\_

```python
def getAmountsOutTokenToToken_(tokenIn, tokenOut, inputAmount: int)
```

Fetches the output token amount when swapping between two tokens.

**Arguments**:

- `tokenIn`: Address of the input token.
- `tokenOut`: Address of the output token.
- `inputAmount`: Input token amount.

**Returns**:

Output token amount in Wei.

<a id="ISwapperContract.InterfaceSwapperContract.getLiquidityUSD_"></a>

#### getLiquidityUSD\_

```python
def getLiquidityUSD_()
```

Fetches the liquidity available for the current token in the USD pair (raw Wei format).

**Arguments**:

- `isTokenIn`: Boolean flag to indicate if the current token is the input.

**Returns**:

Available liquidity in USD (Wei).

<a id="ISwapperContract.InterfaceSwapperContract.getLiquidityUSD"></a>

#### getLiquidityUSD

```python
def getLiquidityUSD()
```

Fetches the liquidity available for the current token in the USD pair and converts it to Ether.

**Arguments**:

- `isTokenIn`: Boolean flag to indicate if the current token is the input.

**Returns**:

Available liquidity in USD (Ether).

<a id="ISwapperContract.InterfaceSwapperContract.getSwapProtocollVersion"></a>

#### getSwapProtocollVersion

```python
def getSwapProtocollVersion()
```

Returns the swap protocol version used for the current token.

**Returns**:

Swap protocol version number.

<a id="ISwapperContract.InterfaceSwapperContract.getTokenInfos"></a>

#### getTokenInfos

```python
def getTokenInfos()
```

Fetches detailed token information including tax rates, honeypot status, etc.

**Returns**:

Tuple containing buy tax, sell tax, and honeypot status.

<a id="ISwapperContract.InterfaceSwapperContract.getWalletTokenDATA"></a>

#### getWalletTokenDATA

```python
def getWalletTokenDATA(wallet_address: str, tokenList: list)
```

Fetches wallet token data such as balances, decimals, prices for the provided list of tokens.

Breaks the calls into batches of 28 addresses to handle large lists.

Returns a JSON string with Price, Decimal, Balance, Version, and Address for each token.

**Arguments**:

- `tokenList`: List of token addresses.

**Returns**:

JSON string containing the token data.

<a id="ISwapperContract.InterfaceSwapperContract.getBestPool"></a>

#### getBestPool

```python
def getBestPool()
```

Retrieves the best liquidity pool for the default token.

This method calls the `getBestPool` function of the `BTTSwapper` smart contract,
using the token address obtained from the `IERC20` token interface.

**Returns**:

- `tuple` - A tuple containing:
  - DexIdent (str): The identifier of the decentralized exchange.
  - Pool_address (str): The address of the best liquidity pool for the default token.
  - BaseToken (str): The base token associated with the pool.

<a id="ISwapperContract.InterfaceSwapperContract.getBestPoolFor"></a>

#### getBestPoolFor

```python
def getBestPoolFor(token_address)
```

Retrieves the best liquidity pool for a specific token.

This method calls the `getBestPool` function of the `BTTSwapper` smart contract
using the specified token address.

**Arguments**:

- `token_address` _str_ - The address of the token for which to find the best pool.
  

**Returns**:

- `tuple` - A tuple containing:
  - DexIdent (str): The identifier of the decentralized exchange.
  - Pool_address (str): The address of the best liquidity pool for the specified token.
  - BaseToken (str): The base token associated with the pool.

<a id="ISwapperContract.InterfaceSwapperContract.getETHtoTokenPathV3"></a>

#### getETHtoTokenPathV3

```python
def getETHtoTokenPathV3()
```

Retrieves the Uniswap V3 path from ETH (WETH) to a specified token.

**Returns**:

- `tuple` - A tuple representing the path and pool information for swapping ETH to a token in V3.

<a id="ISwapperContract.InterfaceSwapperContract.getTokentoETHPathV3"></a>

#### getTokentoETHPathV3

```python
def getTokentoETHPathV3()
```

Retrieves the Uniswap V3 path from a specified token to ETH (WETH).

**Returns**:

- `tuple` - A tuple representing the path and pool information for swapping a token to ETH in V3.

<a id="ISwapperContract.InterfaceSwapperContract.getTokentoTokenPathV3"></a>

#### getTokentoTokenPathV3

```python
def getTokentoTokenPathV3(tokenIn, tokenOut)
```

Retrieves the Uniswap V3 path between two specified tokens.

**Arguments**:

- `tokenIn` _str_ - Address of the input token.
- `tokenOut` _str_ - Address of the output token.
  

**Returns**:

- `tuple` - A tuple representing the path and pool information for swapping from one token to another in V3.

<a id="ISwapperContract.InterfaceSwapperContract.getETHtoTokenPathV2"></a>

#### getETHtoTokenPathV2

```python
def getETHtoTokenPathV2()
```

Retrieves the Uniswap V2 path from ETH (WETH) to a specified token.

**Returns**:

- `tuple` - A tuple representing the path and dex identifiers for swapping ETH to a token in V2.

<a id="ISwapperContract.InterfaceSwapperContract.getTokentoETHPathV2"></a>

#### getTokentoETHPathV2

```python
def getTokentoETHPathV2()
```

Retrieves the Uniswap V2 path from a specified token to ETH (WETH).

**Returns**:

- `tuple` - A tuple representing the path and dex identifiers for swapping a token to ETH in V2.

<a id="ISwapperContract.InterfaceSwapperContract.getTokentoTokenPathV2"></a>

#### getTokentoTokenPathV2

```python
def getTokentoTokenPathV2(tokenIn, tokenOut)
```

Retrieves the Uniswap V2 path between two specified tokens.

**Arguments**:

- `tokenIn` _str_ - Address of the input token.
- `tokenOut` _str_ - Address of the output token.
  

**Returns**:

- `tuple` - A tuple representing the path and dex identifiers for swapping from one token to another in V2.

<a id="ISwapperContract.InterfaceSwapperContract.getETHBalance_"></a>

#### getETHBalance\_

```python
def getETHBalance_()
```

Gets the ETH balance of the user in wei.

**Returns**:

- `int` - The user's ETH balance in wei.

<a id="ISwapperContract.InterfaceSwapperContract.getETHBalance"></a>

#### getETHBalance

```python
def getETHBalance()
```

Gets the ETH balance of the user in ether.

**Returns**:

- `float` - The user's ETH balance in ether.

<a id="ISwapperContract.InterfaceSwapperContract.getETHBalanceOf_"></a>

#### getETHBalanceOf\_

```python
def getETHBalanceOf_(address)
```

Gets the ETH balance of a specified address in wei.

**Arguments**:

- `address` _str_ - The address to check the balance for.
  

**Returns**:

- `int` - The ETH balance of the address in wei.

<a id="ISwapperContract.InterfaceSwapperContract.getETHBalanceOf"></a>

#### getETHBalanceOf

```python
def getETHBalanceOf(address)
```

Gets the ETH balance of a specified address in ether.

**Arguments**:

- `address` _str_ - The address to check the balance for.
  

**Returns**:

- `float` - The ETH balance of the address in ether.

<a id="ISwapperContract.InterfaceSwapperContract.TestSwapETHtoToken"></a>

#### TestSwapETHtoToken

```python
def TestSwapETHtoToken(inputAmount: float)
```

Tests swapping ETH for a specified token using the correct Uniswap protocol version.

**Arguments**:

- `inputAmount` _float_ - The amount of ETH to swap.
  

**Returns**:

- `bool` - True if the test swap was successful, False otherwise.
  

**Raises**:

- `SystemExit` - If there are insufficient ETH funds for the transaction.

<a id="ISwapperContract.InterfaceSwapperContract.TestSwapFromETHtoTokenV2"></a>

#### TestSwapFromETHtoTokenV2

```python
def TestSwapFromETHtoTokenV2(inputAmount: int)
```

Tests swapping ETH for a specified token using Uniswap V2.

**Arguments**:

- `inputAmount` _int_ - The amount of ETH (in wei) to swap.
  

**Returns**:

- `bool` - True if the test swap was successful, False otherwise.

<a id="ISwapperContract.InterfaceSwapperContract.TestSwapFromETHtoTokenV3"></a>

#### TestSwapFromETHtoTokenV3

```python
def TestSwapFromETHtoTokenV3(inputAmount: int)
```

Tests swapping ETH for a specified token using Uniswap V3.

**Arguments**:

- `inputAmount` _int_ - The amount of ETH (in wei) to swap.
  

**Returns**:

- `bool` - True if the test swap was successful, False otherwise.

<a id="ISwapperContract.InterfaceSwapperContract.SwapETHtoToken"></a>

#### SwapETHtoToken

```python
def SwapETHtoToken(inputAmount: float, trys: int)
```

Executes the swap from ETH to a specified token using the correct Uniswap protocol version.

**Arguments**:

- `inputAmount` _float_ - The amount of ETH to swap.
- `trys` _int_ - The number of retry attempts if the transaction fails.
  

**Returns**:

- `tuple` - A tuple containing a boolean (success status), transaction hex, and gas estimate.

<a id="ISwapperContract.InterfaceSwapperContract.SwapFromETHtoTokenV2"></a>

#### SwapFromETHtoTokenV2

```python
def SwapFromETHtoTokenV2(inputAmount: int)
```

Swaps ETH for a specified token using Uniswap V2.

**Arguments**:

- `inputAmount` _int_ - The amount of ETH (in wei) to swap.
  

**Returns**:

- `tuple` - A tuple containing a boolean (success status), transaction hex, and gas estimate.

<a id="ISwapperContract.InterfaceSwapperContract.SwapFromETHtoTokenV3"></a>

#### SwapFromETHtoTokenV3

```python
def SwapFromETHtoTokenV3(inputAmount: int)
```

Swaps ETH for a specified token using Uniswap V3.

**Arguments**:

- `inputAmount` _int_ - The amount of ETH (in wei) to swap.
  

**Returns**:

- `tuple` - A tuple containing a boolean (success status), transaction hex, and gas estimate.

<a id="ISwapperContract.InterfaceSwapperContract.SwapTokentoETH"></a>

#### SwapTokentoETH

```python
def SwapTokentoETH(inputAmount: float, trys: int = 1)
```

Executes the swap from a specified token to ETH using the correct Uniswap protocol version.

**Arguments**:

- `inputAmount` _float_ - The amount of the token to swap.
- `trys` _int, optional_ - The number of retry attempts if the transaction fails. Defaults to 1.
  

**Returns**:

- `tuple` - A tuple containing a boolean (success status), transaction hex, and gas estimate.

<a id="ISwapperContract.InterfaceSwapperContract.SwapFromTokentoETHV3"></a>

#### SwapFromTokentoETHV3

```python
def SwapFromTokentoETHV3(inputAmount: int)
```

Swaps a specified token for ETH using Uniswap V3.

**Arguments**:

- `inputAmount` _int_ - The amount of the token (in wei) to swap.
  

**Returns**:

- `tuple` - A tuple containing a boolean (success status), transaction hex, and gas estimate.

<a id="ISwapperContract.InterfaceSwapperContract.SwapFromTokentoTokenV3"></a>

#### SwapFromTokentoTokenV3

```python
def SwapFromTokentoTokenV3(tokenIn, tokenOut, inputAmount: int)
```

Swaps one token for another using Uniswap V3.

**Arguments**:

- `tokenIn` _str_ - Address of the input token.
- `tokenOut` _str_ - Address of the output token.
- `inputAmount` _int_ - The amount of the input token (in wei) to swap.
  

**Returns**:

- `tuple` - A tuple containing a boolean (success status), transaction hex, and gas estimate.

<a id="ISwapperContract.InterfaceSwapperContract.SwapFromTokentoETHV2"></a>

#### SwapFromTokentoETHV2

```python
def SwapFromTokentoETHV2(inputAmount: int, trys: int = 1)
```

Swaps a specified token for ETH using Uniswap V2.

**Arguments**:

- `inputAmount` _int_ - The amount of the token (in wei) to swap.
- `trys` _int, optional_ - The number of retry attempts if the transaction fails. Defaults to 1.
  

**Returns**:

- `tuple` - A tuple containing a boolean (success status), transaction hex, and gas estimate.

<a id="ISwapperContract.InterfaceSwapperContract.SwapFromTokentoTokenV2"></a>

#### SwapFromTokentoTokenV2

```python
def SwapFromTokentoTokenV2(tokenIn, tokenOut, inputAmount: int, trys: int = 1)
```

Swaps one token for another using Uniswap V2.

**Arguments**:

- `tokenIn` _str_ - Address of the input token.
- `tokenOut` _str_ - Address of the output token.
- `inputAmount` _int_ - The amount of the input token (in wei) to swap.
- `trys` _int, optional_ - The number of retry attempts if the transaction fails. Defaults to 1.
  

**Returns**:

- `tuple` - A tuple containing a boolean (success status), transaction hex, and gas estimate.

<a id="SwapperModul"></a>

# SwapperModul

<a id="SwapperModul.BaseSwap"></a>

## BaseSwap Objects

```python
class BaseSwap(InterfaceSwapperContract, W3Utils, IERC20)
```

A module for interacting with decentralized exchanges (DEX) and managing token swaps on the blockchain.

**Attributes**:

- `token` _str_ - The address of the token to interact with.
- `settings` _CoreSettings_ - Settings for the swapper, loaded from a configuration file.
- `w3` _Web3_ - The Web3 connection to the blockchain.
- `w3U` _W3Utils_ - Utility class for Web3 interactions.
- `IERC20` _IERC20_ - Contract interface for the ERC-20 token being swapped.
- `IAC` _InterfaceSwapperContract_ - Interface for interacting with the swapper contract.
  

**Arguments**:

- `token` _str_ - The token address to initialize. If not provided, falls back to BasedTools Governance Token.
- `settings_file_path` _str_ - The path to the settings file (default is "./Settings.json").
- `saveSettings` _bool_ - Flag to save settings changes back to the file (default is False).

<a id="SwapperModul.BaseSwap.__init__"></a>

#### \_\_init\_\_

```python
def __init__(token: str = None,
             settings_file_path: str = "./Settings.json",
             saveSettings: bool = False)
```

Initialize the swapper module, set up the Web3 connection, and load token and contract interfaces.

**Arguments**:

- `token` _str, optional_ - The token address for interactions (in checksum format).
- `settings_file_path` _str, optional_ - Path to the settings JSON file. Defaults to "./Settings.json".
- `saveSettings` _bool, optional_ - Whether to save changes to the settings file. Defaults to False.

<a id="SwapperModul.BaseSwap.reload"></a>

#### reload

```python
def reload()
```

Reload the Web3 connection, utilities, and contract interfaces after a settings change.

<a id="SwapperModul.BaseSwap.connect"></a>

#### connect

```python
def connect()
```

Establish a Web3 connection using the RPC endpoint specified in settings.

**Returns**:

- `Web3` - The Web3 instance connected to the specified RPC endpoint.

<a id="SwapperModul.BaseSwap.check_settings"></a>

#### check\_settings

```python
def check_settings() -> str
```

Validate the critical settings such as address and private key.

**Returns**:

- `str` - Message indicating the validation result of settings.

<a id="SwapperModul.BaseSwap.printSettings"></a>

#### printSettings

```python
def printSettings()
```

Print the current settings in a formatted JSON style.

<a id="SwapperModul.BaseSwap.loadWalletFromMnomic"></a>

#### loadWalletFromMnomic

```python
def loadWalletFromMnomic(mnemoic)
```

Load a wallet from a mnemonic phrase and update the address and private key in the settings.

**Arguments**:

- `mnemoic` _str_ - The mnemonic phrase to derive the wallet from.

<a id="SwapperModul.BaseSwap.loadWalletFromPrivKey"></a>

#### loadWalletFromPrivKey

```python
def loadWalletFromPrivKey(private_key)
```

Load a wallet from a private key and update the address in the settings.

**Arguments**:

- `private_key` _str_ - The private key for the wallet.

<a id="SwapperModul.BaseSwap.changeRPC"></a>

#### changeRPC

```python
def changeRPC(newRPC)
```

Change the RPC endpoint in the settings and reload the connection.

**Arguments**:

- `newRPC` _str_ - The new RPC endpoint to use.

<a id="SwapperModul.BaseSwap.editSettings"></a>

#### editSettings

```python
def editSettings(key, newValue, skipReload: bool = False)
```

Edit a setting in the configuration and optionally reload the connection.

**Arguments**:

- `key` _str_ - The key of the setting to change.
- `newValue` _any_ - The new value for the setting.
- `skipReload` _bool, optional_ - Whether to skip reloading the connection after changing the setting. Defaults to False.

<a id="SwapperModul.BaseSwap.getSettings"></a>

#### getSettings

```python
def getSettings()
```

Retrieve the current settings.

**Returns**:

- `dict` - The settings dictionary.

<a id="SwapperModul.BaseSwap.changeToken"></a>

#### changeToken

```python
def changeToken(token: str)
```

Change the token being swapped and reload the token and contract interfaces.

**Arguments**:

- `token` _str_ - The new token address (in checksum format).

<a id="W3Utils"></a>

# W3Utils

<a id="W3Utils.W3Utils"></a>

## W3Utils Objects

```python
class W3Utils()
```

A utility class for interacting with the Ethereum blockchain using Web3.
Provides helper methods for common operations like obtaining the current block number, 
converting mnemonics to private keys, estimating gas costs, and managing token amounts 
in different formats.

<a id="W3Utils.W3Utils.__init__"></a>

#### \_\_init\_\_

```python
def __init__(settings, w3)
```

Initializes the W3Utils class.

**Arguments**:

  -----------
  settings : object
  Configuration object containing gas-related settings like GWEI offset and max transaction fees.
  w3 : Web3 instance
  Instance of Web3 used to interact with the Ethereum blockchain.

<a id="W3Utils.W3Utils.block"></a>

#### block

```python
def block()
```

Returns the current Ethereum block number.

**Returns**:

  --------
  int
  The current block number.

<a id="W3Utils.W3Utils.getMnemonicToPrivKey"></a>

#### getMnemonicToPrivKey

```python
def getMnemonicToPrivKey(mnemonic, account_path: str = "m/44'/60'/0'/0/0")
```

Converts a mnemonic phrase to a private key and corresponding Ethereum address.

**Arguments**:

  -----------
  mnemonic : str
  The mnemonic phrase to convert to a private key.
  account_path : str, optional
  The derivation path for the HD wallet, by default "m/44'/60'/0'/0/0".
  

**Returns**:

  --------
  tuple
  A tuple containing the Ethereum address and the private key (in hex format).

<a id="W3Utils.W3Utils.getAddresFromPrivKey"></a>

#### getAddresFromPrivKey

```python
def getAddresFromPrivKey(private_key)
```

Retrieves the Ethereum address associated with the provided private key.

**Arguments**:

  -----------
  private_key : str
  The private key to derive the Ethereum address from.
  

**Returns**:

  --------
  str
  The Ethereum address corresponding to the private key.

<a id="W3Utils.W3Utils.estimateGas"></a>

#### estimateGas

```python
def estimateGas(txn)
```

Estimates gas required for a transaction and checks if the gas cost is within the allowed limit.

**Arguments**:

  -----------
  txn : dict
  A dictionary representing the transaction object (e.g., to, from, value, etc.).
  

**Returns**:

  --------
  tuple
  A tuple containing:
  - int: Estimated gas amount (with 10% overhead).
  - str: Estimated gas cost in Ether.
  - bool: Whether the gas cost is within the maximum allowed transaction fee.

<a id="W3Utils.W3Utils.custom_round"></a>

#### custom\_round

```python
def custom_round(num)
```

Rounds a given decimal number according to specified rules based on its size.

**Arguments**:

  -----------
  num : Decimal
  The number to round.
  

**Returns**:

  --------
  Decimal
  The rounded number based on specific formatting rules.

<a id="W3Utils.W3Utils.to_wei"></a>

#### to\_wei

```python
def to_wei(token_amount: Decimal, decimals: int) -> int
```

Converts a token amount from its human-readable form to the smallest unit (wei).

**Arguments**:

  -----------
  token_amount : Decimal
  The amount of the token in its human-readable form.
  decimals : int
  The number of decimal places the token supports.
  

**Returns**:

  --------
  int
  The token amount in its smallest unit (wei).

<a id="W3Utils.W3Utils.from_wei"></a>

#### from\_wei

```python
def from_wei(token_amount: int, decimals: int) -> Decimal
```

Converts a token amount from its smallest unit (wei) to its human-readable form.

**Arguments**:

  -----------
  token_amount : int
  The amount of the token in its smallest unit (wei).
  decimals : int
  The number of decimal places the token supports.
  

**Returns**:

  --------
  Decimal
  The token amount in its human-readable form.

<a id="W3Utils.W3Utils.get_decimal_places"></a>

#### get\_decimal\_places

```python
def get_decimal_places(number)
```

Determines the number of decimal places in a given number.

**Arguments**:

  -----------
  number : float or Decimal
  The number to evaluate.
  

**Returns**:

  --------
  int
  The number of decimal places.

<a id="W3Utils.W3Utils.get_human_amount"></a>

#### get\_human\_amount

```python
def get_human_amount(number)
```

Formats a number with the appropriate number of decimal places for human-readable display.

**Arguments**:

  -----------
  number : float or Decimal
  The number to format.
  

**Returns**:

  --------
  str
  The formatted number as a string.

<a id="W3Utils.W3Utils.getWalletTokens"></a>

#### getWalletTokens

```python
def getWalletTokens(wallet_address: str,
                    batch_size: int = 10000,
                    blocks_to_check: int = 150000)
```

Fetches a list of unique token addresses that have been transferred to a specified wallet address
within a defined range of Ethereum blocks.

**Arguments**:

- `wallet_address` _str_ - The Ethereum address of the wallet to check for token transfers.
- `batch_size` _int, optional_ - The number of blocks to process in each batch when querying logs. Defaults to 10,000.
- `blocks_to_check` _int, optional_ - The number of past blocks to check for transfers, starting from the latest block. Defaults to 150,000.
  

**Returns**:

- `set` - A set of token contract addresses that have transferred tokens to the specified wallet.
  
  Methodology:
  1. Retrieves the latest block number from the Ethereum blockchain.
  2. Computes the starting block based on the number of `blocks_to_check`.
  3. Creates a filter for Transfer events, looking specifically for logs where the wallet_address is the recipient.
  4. Iterates over the blocks in batches, fetching logs and extracting token addresses from the logs.
  5. Returns a set of unique token contract addresses associated with transfers to the wallet.
  

**Notes**:

  - This method only checks for ERC-20 token transfer events (using the "Transfer" event signature).
  - Logs are retrieved in batches to avoid timeouts for large ranges.
  - If an error occurs during log retrieval, it will return an empty list for that batch of logs.

<a id="__init__"></a>

# \_\_init\_\_

