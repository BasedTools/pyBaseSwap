
class chains:
    def __init__(self, chainID):
        """
        Initializes the chains class with specific settings based on the provided chain ID.
        - `chainID`: The ID of the blockchain network. Supported IDs are 8453 (Base) and 31337 (Local Hardhat).
        """
        self.BTTSwapper = None
        self.ZERO = "0x0000000000000000000000000000000000000000"  # This is constant across all chains
        self.WETH = None
        self.BTT = None

        if int(chainID) == 8453: # Base Mainnet
            self.BTTSwapper = "0xdfFaE64f8E4a0E2389f7EC8d2745E8fa6Fa806eC"
            self.BTT = "0x833589fcd6edb6e08f4c7c32d4f71b54bda02913" #USDC, BTT Soon
            self.WETH = "0x4200000000000000000000000000000000000006"
            self.chainID = 8453

        elif int(chainID) == 31337: #Local Hardhat fork of Base for testing 
            self.BTTSwapper = "0xdfFaE64f8E4a0E2389f7EC8d2745E8fa6Fa806eC"
            self.BTT = "0x833589fcd6edb6e08f4c7c32d4f71b54bda02913" #USDC, BTT Soon
            self.WETH = "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c"
            self.chainID = 31337

        else:
            raise SystemExit(f"ChainID {chainID} currently not Supported!")

