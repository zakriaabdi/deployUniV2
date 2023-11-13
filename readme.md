## Important notes on usage
1. Whilst -- args are typically optional in this case these are required, please specify all three.
2. run `pip install web3` this should also install `eth-account` if it doesnt then also run `pip install eth-account`
3. Example usage (using default key provided by anvil):
`python3 deploy_uni_v2.py --private-key 0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80 --rpc-url "http://127.0.0.1:8545" --governance-addr 0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266` 
4. Networks with multiple gas tokens e.g. Boba supports both Eth and Boba token might overcharge you with the gas price because the quote might be the wrong token.
We recommend checking with your relevant networks and if there is a similar scenario then hardcode the  `gas_price` variable (line 31)
e.g we choose to hardcode the gas_price to 1 gwei when deploying to boba.
5. If you want to do a test run the using [Anvil](https://github.com/foundry-rs/foundry) is convenient. Start it by specifying a fork url for your relevant network and then pass in `127.0.0.1:8545` as the rpc_url arg to this script.