# pyBaseSwap

pyBaseSwap is a Python library designed to facilitate interaction with ERC-20 tokens on the Base L2 Ethereum blockchain. It provides an easy-to-use interface for managing token balances, allowances, and transactions, allowing developers to focus on building their applications without worrying about the complexities of blockchain interactions.

## Warning

> **Warning:** You will be charged a 1% fee on your swap volume during the initial phase. This fee is temporarily set higher to cover server costs and other expenses.


## Supported DEXs
| DEX Name         |  Versions          |
|------------------|------------------|
| SushiSwap        | v2 & v3            |
| BaseSwap         | v2 & v3            |
| PancakeSwap    | v2 & v3            |
| AlienBase           | v2 & v3          |
| SwapBased         | v2 & v3          |

##  [Documentation](https://github.com/BasedTools/pyBaseSwap/blob/main/docs/README.md)
##  [Examples](https://github.com/BasedTools/pyBaseSwap/tree/main/examples)
##  [Pypi Realese](https://pypi.org/project/pyBaseSwap/)


### Installation
You can install the package using pip:
```bash
pip install pyBaseSwap
```
#### Installing from Source
If you prefer to install pyBaseSwap from the source, follow these steps:

##### Clone the repository:
```bash
git clone https://github.com/BaseTools/pyBaseSwap
cd pyBaseSwap
python setup.py install
```

#### `EXAMPLE USE`
```python
from pyBaseSwap import BaseSwap
BS = BaseSwap() # No Token Addresss Provided fallback to USDC

BS.changeToken(
  "0x65e570b560027F493f2b1907e8e8e3B9546053bD" #Tyler Token
)
usdPrice = BS.getUSDPrice() # fetch usd price

print(usdPrice)
```

#### `LICENSE`
```plaintext
MIT License

Copyright (c) [2024] [BasedTools]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
