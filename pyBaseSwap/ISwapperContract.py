from web3 import Web3
from eth_abi import abi
from .core_abis import BTTSwapper_ABI
from .core_chains import chains
import time, json


class InterfaceSwapperContract: #ISC
    """
    Interface for interacting with a blockchain-based token swapper smart contract.

    This class provides methods for querying token prices, liquidity, swapping tokens,
    and building transactions for multiple token swap protocols (V2 and V3).
    """
    
    def __init__(self, settings, w3, IERC20, w3U):
        """
        Initializes the InterfaceSwapperContract instance with Web3 and token contract information.

        :param settings: Object containing configuration and user settings.
        :param w3: Web3 instance to interact with Ethereum-like blockchain.
        :param IERC20: Interface for interacting with ERC20 tokens.
        :param w3U: Utility functions for Web3-related conversions.
        """
        self.settings, self.user_address, self.priv_key, self.w3, self.IERC20, self.w3U = settings, settings.settings["address"], settings.settings["private_key"], w3, IERC20, w3U
        self.chain = chains(self.w3.eth.chain_id)
        self.BTTSwapper = self.initRouter()

    def initRouter(self):
        """
        Initializes and returns the swapper smart contract.

        :return: Web3 contract instance of the swapper.
        """
        BTTSwapper = self.w3.eth.contract(
            address=self.chain.BTTSwapper, abi=BTTSwapper_ABI)
        return BTTSwapper
    
    def getAmountsOutV3(self, pools, path, amountIn):
        """
        Fetches the amount of tokens obtainable from a V3 swap route.

        :param pools: List of pool addresses involved in the V3 swap.
        :param path: Token addresses specifying the swap path.
        :param amountIn: Input amount of tokens.
        :return: The output token amount for the given input and path.
        """
        return self.BTTSwapper.functions.getAmountsOutV3(
            pools, path, amountIn
            ).call()
    
    def getAmountsOutV2(self, amountIn, path, dexPath):
        """
        Fetches the amount of tokens obtainable from a V2 swap route.

        :param amountIn: Input amount of tokens.
        :param path: Token addresses specifying the swap path.
        :param dexPath: Decentralized exchanges involved in the swap.
        :return: The output token amount for the given input and path.
        """
        return self.BTTSwapper.functions.getAmountsOutV2(
            amountIn, path, dexPath
            ).call()
    
    def getUSDPrice_(self):
        """
        Fetches the USD price of the current token from the contract (raw Wei format).

        :return: Token price in USD (Wei).
        """
        return self.BTTSwapper.functions.getUSDPrice(
            self.IERC20.get_token_address()
            ).call()
        
    def getUSDPrice(self):
        """
        Fetches the USD price of the current token and converts it to Ether format.

        :return: Token price in USD (Ether).
        """
        return Web3.from_wei(self.BTTSwapper.functions.getUSDPrice(
            self.IERC20.get_token_address()
            ).call(), "mwei")
    
    
    def getUSDPriceOf(self, tokenAddress):
        """
        Fetches the USD price of a specified token and converts it to Ether format.

        :param tokenAddress: Address of the token.
        :return: Token price in USD (Ether).
        """
        return Web3.from_wei(self.BTTSwapper.functions.getUSDPrice(
            self.w3.to_checksum_address(tokenAddress)
            ).call(), "mwei")
    
    def getUSDPriceOf_(self, tokenAddress):
        """
        Fetches the ETH price of a specified token (raw Wei format).

        :param tokenAddress: Address of the token.
        :return: Token price in ETH (Wei).
        """
        return self.BTTSwapper.functions.getUSDPrice(
            self.w3.to_checksum_address(tokenAddress)
            ).call()
        
        
    def getTokenETHPrice_(self, tokenAddress):
        """
        Fetches the ETH price of a specified token (raw Wei format).

        :param tokenAddress: Address of the token.
        :return: Token price in ETH (Wei).
        """
        return self.BTTSwapper.functions.getETHPrice(
            self.w3.to_checksum_address(tokenAddress)
            ).call()
        
    def getTokenETHPrice(self, tokenAddress):
        """
        Fetches the ETH price of a specified token (ether format).

        :param tokenAddress: Address of the token.
        :return: Token price in ETH (Ether).
        """
        return Web3.from_wei(self.BTTSwapper.functions.getETHPrice(
            self.w3.to_checksum_address(tokenAddress)
            ).call(), "ether")    
    
        
    def getNativPrice_(self):
        """
        Fetches the USD price of Wrapped ETH (WETH) from the contract (raw Wei format).

        :return: WETH price in USD (Wei).
        """
        return self.BTTSwapper.functions.getUSDPrice(
            self.chain.WETH).call()
        
    def getNativPrice(self):
        """
        Fetches the USD price of  ETH (WETH) and converts it to Ether format.

        :return: WETH price in USD (Ether).
        """
        return Web3.from_wei(self.BTTSwapper.functions.getUSDPrice(
            self.chain.WETH).call(), "mwei")
    
    def getAmountsOutTokenToETH_(self, inputAmount:int):
        """
        Fetches the output token amount when swapping from ETH to the current token.

        :param inputAmount: Input ETH amount.
        :return: Output token amount in Wei.
        """

        return self.BTTSwapper.functions.getAmountsOut(
            self.IERC20.get_token_address(),
            self.chain.WETH,
            inputAmount
        ).call()

    def getAmountsOutETHToToken_(self, inputAmount:int):
        """
        Fetches the output token amount when swapping from ETH to the current token.

        :param inputAmount: Input ETH amount.
        :return: Output token amount in Wei.
        """
        return self.BTTSwapper.functions.getAmountsOut(
            self.chain.WETH,
            self.IERC20.get_token_address(),
            inputAmount
        ).call()
    
    def getAmountsOutTokenToToken_(self, tokenIn, tokenOut, inputAmount:int):
        """
        Fetches the output token amount when swapping between two tokens.

        :param tokenIn: Address of the input token.
        :param tokenOut: Address of the output token.
        :param inputAmount: Input token amount.
        :return: Output token amount in Wei.
        """
        return self.BTTSwapper.functions.getAmountsOut(
            Web3.to_checksum_address(tokenIn),
            Web3.to_checksum_address(tokenOut),
            inputAmount
        ).call()
    
    def getLiquidityUSD_(self):
        """
        Fetches the liquidity available for the current token in the USD pair (raw Wei format).

        :param isTokenIn: Boolean flag to indicate if the current token is the input.
        :return: Available liquidity in USD (Wei).
        """
        return self.BTTSwapper.functions.getLiquidity(
            self.IERC20.get_token_address()
        ).call()
        
    def getLiquidityUSD(self):
        """
        Fetches the liquidity available for the current token in the USD pair and converts it to Ether.

        :param isTokenIn: Boolean flag to indicate if the current token is the input.
        :return: Available liquidity in USD (Ether).
        """
        return self.w3U.from_wei(
            self.BTTSwapper.functions.getLiquidity(
            self.IERC20.get_token_address()
        ).call(), 6)

    def getSwapProtocollVersion(self):
        """
        Returns the swap protocol version used for the current token.

        :return: Swap protocol version number.
        """
        return self.BTTSwapper.functions.checkVersion(self.IERC20.get_token_address()).call()

    def getTokenInfos(self):
        """
        Fetches detailed token information including tax rates, honeypot status, etc.

        :return: Tuple containing buy tax, sell tax, and honeypot status.
        """
        function_signature = self.BTTSwapper.encode_abi("getTokenInfos", args=[self.IERC20.get_token_address()])
        data = {
            "to": self.BTTSwapper.address,
            "data": function_signature,
            "from": self.chain.ZERO
        }
        _data = self.w3.eth.call(data)
        call = abi.decode(
            ['uint256', 'uint256', 'uint256', 'uint256', 'bool', 'bool', 'bool', 'bool', 'string'],
            _data
        )
        buy_tax = round(
            ((call[0] - call[1]) / (call[0]) * 100) - 1, 3)
        sell_tax = round(
            ((call[2] - call[3]) / (call[2]) * 100) - 1, 3)

        if call[4] and call[5] and call[6] and call[7] == True:
            honeypot = False
        else:
            honeypot = True
        return buy_tax, sell_tax, honeypot
    
    def getETHUSDPrice(self):
        return Web3.from_wei(self.BTTSwapper.functions.getUSDPrice(
            self.chain.WETH
            ).call(), "mwei")
    
    def getWalletTokenDATA(self, wallet_address:str, tokenList:list):
        """
        Fetches wallet token data such as balances, decimals, prices for the provided list of tokens.
        Breaks the calls into batches of 28 addresses to handle large lists.

        Returns a JSON string with Price, Decimal, Balance, Version, and Address for each token.

        :param tokenList: List of token addresses.
        :returns: JSON string containing the token data.
        """
        MAX_BATCH_SIZE = 28
        tokenList = [Web3.to_checksum_address(address) for address in tokenList]
        tokenDataList = []
        ethPrice = self.getETHUSDPrice()
       
        for i in range(0, len(tokenList), MAX_BATCH_SIZE):
            tokenBatch = tokenList[i:i + MAX_BATCH_SIZE]
            try:
                tokenAddress, tokenName, tokenSymbol, tokenDecimals, tokensVersion, tokenBalances, tokenUSDPrice, tokenETHPrice = (
                    self.BTTSwapper.functions.getWalletTokenDATA(wallet_address, tokenBatch).call()
                )

                for j in range(len(tokenBatch)):
                    hBalance = tokenBalances[j] / 10**tokenDecimals[j]
                    tokenPriceEth = Web3.from_wei(tokenETHPrice[j], "ether")
                    tokenUSD = tokenPriceEth * ethPrice

                    tokenData = {
                        "Address": tokenAddress[j],
                        "Name": tokenName[j],
                        "Symbol": tokenSymbol[j],
                        "Decimals": int(tokenDecimals[j]),
                        "UniswapV": tokensVersion[j],
                        "BalanceWei": tokenBalances[j],
                        "Balance": hBalance,
                        "BalanceUSD": float(self.w3U.get_human_amount(float(tokenUSD) * float(hBalance))),
                        "USDPriceWei": tokenUSDPrice[j],
                        "ETHPriceWei": tokenETHPrice[j],
                        "USDPrice":  self.w3U.get_human_amount(float(tokenUSD)),
                        "ETHPrice": self.w3U.get_human_amount(tokenPriceEth)
                    }
                    tokenDataList.append(tokenData)
            except Exception as e:
                print(e, tokenBatch)
                
        ethBalance = self.getETHBalanceOf_(wallet_address)
        eths = Web3.from_wei(ethBalance,"ether")
        nativData = {
                "Address": "Nativ",
                "Name": "Ethereum",
                "Symbol": "ETH",
                "Decimals": int(18),
                "UniswapV": 3,
                "BalanceWei": ethBalance,
                "Balance": eths,
                "BalanceUSD": float(self.w3U.get_human_amount(float(ethPrice) * float(eths))),
                "USDPriceWei": Web3.to_wei(ethPrice,"mwei"),
                "ETHPriceWei": 1*(10**18),
                "USDPrice":  self.w3U.get_human_amount(float(ethPrice)),
                "ETHPrice": 1
        }        
        tokenDataList.append(nativData)
        return sorted(tokenDataList, key=lambda x: float(x["BalanceUSD"]), reverse=True)

    
    def getWalletAssets(self, wallet_address: str, batch_size: int=10000, blocks_to_check: int = 150000):
        tokenList = self.w3U.getWalletTokens(wallet_address, batch_size, blocks_to_check)
        tokenHoldings = self.getWalletTokenDATA(wallet_address, tokenList)
        return tokenHoldings

    def getBestPool(self):
        """
        Retrieves the best liquidity pool for the default token.

        This method calls the `getBestPool` function of the `BTTSwapper` smart contract,
        using the token address obtained from the `IERC20` token interface.

        Returns:
            tuple: A tuple containing:
                - DexIdent (str): The identifier of the decentralized exchange.
                - Pool_address (str): The address of the best liquidity pool for the default token.
                - BaseToken (str): The base token associated with the pool.
        """
        return self.BTTSwapper.functions.getBestPool(self.IERC20.get_token_address()).call()
    
    def getBestPoolFor(self, token_address):
        """
        Retrieves the best liquidity pool for a specific token.

        This method calls the `getBestPool` function of the `BTTSwapper` smart contract
        using the specified token address.

        Args:
            token_address (str): The address of the token for which to find the best pool.

        Returns:
            tuple: A tuple containing:
                - DexIdent (str): The identifier of the decentralized exchange.
                - Pool_address (str): The address of the best liquidity pool for the specified token.
                - BaseToken (str): The base token associated with the pool.
        """
        return self.BTTSwapper.functions.getBestPool(Web3.to_checksum_address(token_address)).call()
    
    def getETHtoTokenPathV3(self):
        """
        Retrieves the Uniswap V3 path from ETH (WETH) to a specified token.

        Returns:
            tuple: A tuple representing the path and pool information for swapping ETH to a token in V3.
        """
        return self.BTTSwapper.functions.getSwapPathV3(self.chain.WETH, self.IERC20.get_token_address()).call()
    
    def getTokentoETHPathV3(self):
        """
        Retrieves the Uniswap V3 path from a specified token to ETH (WETH).

        Returns:
            tuple: A tuple representing the path and pool information for swapping a token to ETH in V3.
        """
        return self.BTTSwapper.functions.getSwapPathV3(self.IERC20.get_token_address(),self.chain.WETH).call()
        
    def getTokentoTokenPathV3(self, tokenIn, tokenOut):
        """
        Retrieves the Uniswap V3 path between two specified tokens.

        Args:
            tokenIn (str): Address of the input token.
            tokenOut (str): Address of the output token.

        Returns:
            tuple: A tuple representing the path and pool information for swapping from one token to another in V3.
        """
        return self.BTTSwapper.functions.getSwapPathV3(
                Web3.to_checksum_address(tokenIn),
                Web3.to_checksum_address(tokenOut)
            ).call()
    
    
    def getETHtoTokenPathV2(self):
        """
        Retrieves the Uniswap V2 path from ETH (WETH) to a specified token.

        Returns:
            tuple: A tuple representing the path and dex identifiers for swapping ETH to a token in V2.
        """
        return self.BTTSwapper.functions.getSwapPathV2(self.chain.WETH, self.IERC20.get_token_address()).call()
    
    def getTokentoETHPathV2(self):
        """
        Retrieves the Uniswap V2 path from a specified token to ETH (WETH).

        Returns:
            tuple: A tuple representing the path and dex identifiers for swapping a token to ETH in V2.
        """
        return self.BTTSwapper.functions.getSwapPathV2(self.IERC20.get_token_address(),self.chain.WETH).call()
        
    def getTokentoTokenPathV2(self, tokenIn, tokenOut):
        """
        Retrieves the Uniswap V2 path between two specified tokens.

        Args:
            tokenIn (str): Address of the input token.
            tokenOut (str): Address of the output token.

        Returns:
            tuple: A tuple representing the path and dex identifiers for swapping from one token to another in V2.
        """
        return self.BTTSwapper.functions.getSwapPathV2(
                Web3.to_checksum_address(tokenIn),
                Web3.to_checksum_address(tokenOut)
            ).call()
    
    def getETHBalance_(self):
        """
        Gets the ETH balance of the user in wei.

        Returns:
            int: The user's ETH balance in wei.
        """
        return self.w3.eth.get_balance(self.user_address)
    
    def getETHBalance(self):
        """
        Gets the ETH balance of the user in ether.

        Returns:
            float: The user's ETH balance in ether.
        """
        return self.w3.from_wei(self.w3.eth.get_balance(self.user_address), "ether")
    
    def getETHBalanceOf_(self, address):
        """
        Gets the ETH balance of a specified address in wei.

        Args:
            address (str): The address to check the balance for.

        Returns:
            int: The ETH balance of the address in wei.
        """
        return self.w3.eth.get_balance(address)
    
    def getETHBalanceOf(self, address):
        """
        Gets the ETH balance of a specified address in ether.

        Args:
            address (str): The address to check the balance for.

        Returns:
            float: The ETH balance of the address in ether.
        """
        return self.w3.from_wei(self.w3.eth.get_balance(address), "ether")

    def TestSwapETHtoToken(self, inputAmount: float):
        """
        Tests swapping ETH for a specified token using the correct Uniswap protocol version.

        Args:
            inputAmount (float): The amount of ETH to swap.

        Returns:
            bool: True if the test swap was successful, False otherwise.

        Raises:
            SystemExit: If there are insufficient ETH funds for the transaction.
        """
        try:
            v = self.getSwapProtocollVersion()
            inputETH = self.w3U.to_wei(inputAmount, 18)
            if int(v) == 2:
                try:
                    if self.TestSwapFromETHtoTokenV2(inputETH):
                        return True
                except ValueError as e:
                    if 'message' in str(e):
                        if  'insufficient funds for transfer' in str(e):
                            print("")
                            print("ERROR:", "insufficient ETH funds for transaction!")
                            print("Exiting Now")
                            raise SystemExit
                        
            elif int(v) == 3:
               try:
                    if self.TestSwapFromETHtoTokenV3(inputETH):
                         return True
               except ValueError as e:
                    if 'message' in str(e):
                        if  'insufficient funds for transfer' in str(e):
                            print("")
                            print("ERROR:", "insufficient ETH funds for transaction!")
                            print("Exiting Now")
                            raise SystemExit

        except Exception as e:
            print(e)
            return False


    def TestSwapFromETHtoTokenV2(self, inputAmount: int):
        """
        Tests swapping ETH for a specified token using Uniswap V2.

        Args:
            inputAmount (int): The amount of ETH (in wei) to swap.

        Returns:
            bool: True if the test swap was successful, False otherwise.
        """
        path, dexIdents  = self.getETHtoTokenPathV2()
        amountOut = self.getAmountsOutV2(inputAmount, path, dexIdents)[-1]
        amountOutMinimum = int(amountOut - (amountOut * int(self.settings.settings["Slippage"])) / 100)
        txn = self.BTTSwapper.functions.swapETHtoTokenV2(
                path,
                dexIdents,
                amountOutMinimum
        ).build_transaction({
                    'from': self.user_address,
                    'gasPrice': self.w3.eth.gas_price ,
                    'nonce': self.w3.eth.get_transaction_count(self.user_address),
                    'value': int(inputAmount)
        })
        return True


    def TestSwapFromETHtoTokenV3(self, inputAmount: int):
        """
        Tests swapping ETH for a specified token using Uniswap V3.

        Args:
            inputAmount (int): The amount of ETH (in wei) to swap.

        Returns:
            bool: True if the test swap was successful, False otherwise.
        """
        path, _, pools, poolFees = self.getETHtoTokenPathV3()
        amountOut = self.getAmountsOutV3(pools, path, inputAmount)[-1]
        minOutput = int(amountOut - (amountOut * int(self.settings.settings["Slippage"])) / 100)
        txn = self.BTTSwapper.functions.swapETHtoTokenV3(
            path,
            pools,
            poolFees,
            minOutput
        ).build_transaction({
                'from': self.user_address,
                'gasPrice': int(self.w3.eth.gas_price ),
                'nonce': self.w3.eth.get_transaction_count(self.user_address),
                'value': int(inputAmount)
        })
        return True
    

    def SwapETHtoToken(self, inputAmount: float, trys: int):
        """
        Executes the swap from ETH to a specified token using the correct Uniswap protocol version.

        Args:
            inputAmount (float): The amount of ETH to swap.
            trys (int): The number of retry attempts if the transaction fails.

        Returns:
            tuple: A tuple containing a boolean (success status), transaction hex, and gas estimate.
        """
        while trys:
            try:
                v = self.getSwapProtocollVersion()
                inputETH = self.w3U.to_wei(inputAmount, 18)
                if int(v) == 2:
                    return self.SwapFromETHtoTokenV2(inputETH)
                elif int(v) == 3:
                    return self.SwapFromETHtoTokenV3(inputETH)
            except Exception as e:
                print(e)
                trys -= 1
                time.sleep(1)
                if trys == 0:
                    return False, "0", e

    def SwapFromETHtoTokenV2(self, inputAmount: int):
        """
        Swaps ETH for a specified token using Uniswap V2.

        Args:
            inputAmount (int): The amount of ETH (in wei) to swap.

        Returns:
            tuple: A tuple containing a boolean (success status), transaction hex, and gas estimate.
        """
        path, dexIdents  = self.getETHtoTokenPathV2()
        amountOut = self.getAmountsOutV2(inputAmount, path, dexIdents)[-1]
        amountOutMinimum = int(amountOut - (amountOut * int(self.settings.settings["Slippage"])) / 100)
        txn = self.BTTSwapper.functions.swapETHtoTokenV2(
            path,
            dexIdents,
            amountOutMinimum
        ).build_transaction({
            'from': self.user_address,
             'gasPrice': self.w3.eth.gas_price ,
             'nonce': self.w3.eth.get_transaction_count(self.user_address),
             'value': int(inputAmount)
        })
        gas = self.w3U.estimateGas(txn)
        txn.update({'gas': gas[0]})
        signed_txn = self.w3.eth.account.sign_transaction(
            txn,
            self.priv_key
        )
        txn = self.w3.eth.send_raw_transaction(signed_txn.raw_transaction)
        txn_receipt = self.w3.eth.wait_for_transaction_receipt(
            txn, timeout=self.settings.settings["timeout"])
        if txn_receipt["status"] == 1:
            return True, txn.hex(), gas
        else:
            return False, txn.hex(), gas
                



    def SwapFromETHtoTokenV3(self, inputAmount: int):
        """
        Swaps ETH for a specified token using Uniswap V3.

        Args:
            inputAmount (int): The amount of ETH (in wei) to swap.

        Returns:
            tuple: A tuple containing a boolean (success status), transaction hex, and gas estimate.
        """
        path, dexIdents, pools, poolFees = self.getETHtoTokenPathV3()
        amountOut = self.getAmountsOutV3(pools, path, inputAmount)[-1]
        minOutput = int(amountOut - (amountOut * int(self.settings.settings["Slippage"])) / 100)
        txn = self.BTTSwapper.functions.swapETHtoTokenV3(
            path,
            pools,
            poolFees,
            minOutput
        ).build_transaction({
            'from': self.user_address,
            'gasPrice': int(self.w3.eth.gas_price ),
            'nonce': self.w3.eth.get_transaction_count(self.user_address),
            'value': int(inputAmount)
        })
        gas = self.w3U.estimateGas(txn)
        txn.update({'gas': gas[0]})
        signed_txn = self.w3.eth.account.sign_transaction(
            txn,
            self.priv_key
        )
        txn = self.w3.eth.send_raw_transaction(signed_txn.raw_transaction)
        txn_receipt = self.w3.eth.wait_for_transaction_receipt(
            txn, timeout=self.settings.settings["timeout"])
        if txn_receipt["status"] == 1:
            return True, txn.hex(), gas
        else:
            return False, txn.hex(), gas




    def SwapTokentoETH(self, inputAmount: float, trys: int = 1):
        """
        Executes the swap from a specified token to ETH using the correct Uniswap protocol version.

        Args:
            inputAmount (float): The amount of the token to swap.
            trys (int, optional): The number of retry attempts if the transaction fails. Defaults to 1.

        Returns:
            tuple: A tuple containing a boolean (success status), transaction hex, and gas estimate.
        """
        while trys:
            try:
                v = self.getSwapProtocollVersion()
                inputToken = self.w3U.to_wei(inputAmount, self.IERC20.get_token_decimals())
                if int(v) == 2:
                    return self.SwapFromTokentoETHV2(inputToken)
                elif int(v) == 3:
                    return self.SwapFromTokentoETHV3(inputToken)
            except Exception as e:
                #print(e)
                trys -= 1
                time.sleep(1)
                if trys == 0:
                    return False, "0", e
        


    def SwapFromTokentoETHV3(self, inputAmount: int,):
        """
    Swaps a specified token for ETH using Uniswap V3.

    Args:
        inputAmount (int): The amount of the token (in wei) to swap.

    Returns:
        tuple: A tuple containing a boolean (success status), transaction hex, and gas estimate.
    """
        try:
            path, _, pools, poolFees = self.getTokentoETHPathV3()
            amountOut = self.getAmountsOutV3(pools, path, inputAmount)[-1]
            amountOutMinimum = int(amountOut - (amountOut * int(self.settings.settings["Slippage"])) / 100)
            txn = self.BTTSwapper.functions.swapTokenToETHV3(
                path,
                pools,
                poolFees,
                inputAmount,
                amountOutMinimum
            ).build_transaction({
                'from': self.user_address,
                'gasPrice': self.w3.eth.gas_price,
                'nonce': self.w3.eth.get_transaction_count(self.user_address),
                'value': 0
            })
            gas = self.w3U.estimateGas(txn)
            txn.update({'gas': gas[0]})
            signed_txn = self.w3.eth.account.sign_transaction(
                txn,
                self.priv_key
            )
            txn = self.w3.eth.send_raw_transaction(signed_txn.raw_transaction)
            txn_receipt = self.w3.eth.wait_for_transaction_receipt(
                txn, timeout=self.settings.settings["timeout"])
            if txn_receipt["status"] == 1:
                return True, txn.hex(), gas
            else:
                return False, txn.hex(), gas
        except Exception as e:
            return False, "0x0", e



    def SwapFromTokentoTokenV3(self, tokenIn, tokenOut, inputAmount: int):
        """
        Swaps one token for another using Uniswap V3.

        Args:
            tokenIn (str): Address of the input token.
            tokenOut (str): Address of the output token.
            inputAmount (int): The amount of the input token (in wei) to swap.

        Returns:
            tuple: A tuple containing a boolean (success status), transaction hex, and gas estimate.
        """
        path, dexIdents, pools, poolFees = self.getTokentoTokenPathV3(tokenIn, tokenOut)
        amountOut = self.getAmountsOutV3(pools, path, inputAmount)[-1]
        amountOutMinimum = int(amountOut - (amountOut * int(self.settings.settings["Slippage"])) / 100)
        txn = self.BTTSwapper.functions.swapTokentoTokenV3(
            path,
            pools,
            poolFees,
            inputAmount,
            amountOutMinimum
        ).build_transaction({
            'from': self.user_address,
            'gasPrice': self.w3.eth.gas_price,
            'nonce': self.w3.eth.get_transaction_count(self.user_address),
            'value': 0
        })
        gas = self.w3U.estimateGas(txn)
        txn.update({'gas': gas[0]})
        signed_txn = self.w3.eth.account.sign_transaction(
            txn,
            self.priv_key
        )
        txn = self.w3.eth.send_raw_transaction(signed_txn.raw_transaction)
        txn_receipt = self.w3.eth.wait_for_transaction_receipt(
            txn, timeout=self.settings.settings["timeout"])
        if txn_receipt["status"] == 1:
            return True, txn.hex(), gas
        else:
            return False, txn.hex(), gas

    


    def SwapFromTokentoETHV2(self, inputAmount: int, trys: int = 1):
        """
        Swaps a specified token for ETH using Uniswap V2.

        Args:
            inputAmount (int): The amount of the token (in wei) to swap.
            trys (int, optional): The number of retry attempts if the transaction fails. Defaults to 1.

        Returns:
            tuple: A tuple containing a boolean (success status), transaction hex, and gas estimate.
        """
        try:
            path, dexIdents = self.getTokentoETHPathV2()
            amountOut = self.getAmountsOutV2(inputAmount, path, dexIdents)[-1]
            amountOutMinimum = int(amountOut - (amountOut * int(self.settings.settings["Slippage"])) / 100)
            txn = self.BTTSwapper.functions.swapTokentoETHV2(
                path,
                dexIdents,
                inputAmount,
                amountOutMinimum
            ).build_transaction({
                'from': self.user_address,
                'gasPrice': self.w3.eth.gas_price,
                'nonce': self.w3.eth.get_transaction_count(self.user_address),
                'value': 0
            })
            gas = self.w3U.estimateGas(txn)
            txn.update({'gas': gas[0]})
            signed_txn = self.w3.eth.account.sign_transaction(
                txn,
                self.priv_key
            )
            txn = self.w3.eth.send_raw_transaction(signed_txn.raw_transaction)
            txn_receipt = self.w3.eth.wait_for_transaction_receipt(
                txn, timeout=self.settings.settings["timeout"])
            if txn_receipt["status"] == 1:
                return True, txn.hex(), gas
            else:
                return False, txn.hex(), gas
        except Exception as e:
            return False, "0x0", e


    def SwapFromTokentoTokenV2(self, tokenIn, tokenOut, inputAmount: int, trys: int = 1):
        """
        Swaps one token for another using Uniswap V2.
    
        Args:
            tokenIn (str): Address of the input token.
            tokenOut (str): Address of the output token.
            inputAmount (int): The amount of the input token (in wei) to swap.
            trys (int, optional): The number of retry attempts if the transaction fails. Defaults to 1.
    
        Returns:
            tuple: A tuple containing a boolean (success status), transaction hex, and gas estimate.
        """
        path, dexIdents = self.getTokentoTokenPathV2(tokenIn, tokenOut)
        amountOut = self.getAmountsOutV2(inputAmount, path, dexIdents)[-1]
        amountOutMinimum = int(amountOut - (amountOut * int(self.settings.settings["Slippage"])) / 100)
        txn = self.BTTSwapper.functions.swapTokentoTokenV2(
            path,
            dexIdents,
            inputAmount,
            amountOutMinimum
        ).build_transaction({
                'from': self.user_address,
                'gasPrice': self.w3.eth.gas_price,
                'nonce': self.w3.eth.get_transaction_count(self.user_address),
                'value': 0
        })
        gas = self.w3U.estimateGas(txn)
        txn.update({'gas': gas[0]})
        signed_txn = self.w3.eth.account.sign_transaction(
            txn,
            self.priv_key
        )
        txn = self.w3.eth.send_raw_transaction(signed_txn.raw_transaction)
        txn_receipt = self.w3.eth.wait_for_transaction_receipt(
            txn, timeout=self.settings.settings["timeout"])
        if txn_receipt["status"] == 1:
            return True, txn.hex(), gas
        else:
            return False, txn.hex(), gas
        
        
def decodeSwapTransaction(self, tx_hash):
    """
    Decodes the input of a swap transaction given its transaction hash.

    This method retrieves the transaction from the Ethereum network using 
    the provided transaction hash and decodes the input data using the 
    BasedTools Swapper to extract details such as the swap path, the 
    minimum output amount, and the input amount.

    Args:
        tx_hash (str): The transaction hash of the swap transaction to decode.

    Returns:
        tuple: A tuple containing the following elements:
            - tx_hash (str): The transaction hash.
            - path (list): The path of tokens involved in the swap.
            - amount_in (int): The amount of tokens being swapped.
            - min_output (int): The minimum expected output from the swap.

    Raises:
        ValueError: If decoding the transaction input fails or if the 
        transaction is not compatible with the BasedTools Swapper.
    """
    tx = self.w3.eth.get_transaction(tx_hash)
    try:
        function, parameters = self.BTTSwapper.decode_function_input(tx.input)
        print(parameters)
        path = parameters['path']
        min_output = parameters['minOutput']
        amount_in = parameters.get('amountIn', tx["value"])
        return tx_hash, path, amount_in, min_output
    except Exception as e:
        raise ValueError(f"Failed to decode transaction input: {str(e)}")
        
