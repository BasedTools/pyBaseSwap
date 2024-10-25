from setuptools import setup, find_packages

setup(
    name='pyBaseSwap',
    version='0.13',
    description='A Python library for aggregating token prices and swaps across multiple DEXs',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/BasedTools/pyBaseSwap',
    author='BasedTools',
    author_email='BasedToolsAdmin@protonmail.com"', 
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'requests',               # For making HTTP requests
        'web3',                   # For interacting with the Ethereum blockchain
        'eth-abi',                # For Ethereum ABI encoding/decoding
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',  # Adjust as needed
        'Programming Language :: Python :: 3.9',  # Adjust as needed
        'Programming Language :: Python :: 3.10',  # Adjust as needed
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
    ],
    python_requires='>=3.6',  # Adjust as needed
)
