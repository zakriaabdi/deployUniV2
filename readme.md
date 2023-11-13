## Important notes on usage
1. Whilst -- args are typically optional in this case these are required, please specify all three.
2. Networks with multiple gas tokens e.g. Boba supports both Eth and Boba token might overcharge you with the gas price because the quote might be the wrong token.
We recommend checking with your relevant networks and if there is a similar scenario then hardcode the  `gas_price` variable (line 31)
e.g we choose to hardcode the gas_price to 1 gwei when deploying to boba.
3. If you want to do a test run the using [Anvil](https://github.com/foundry-rs/foundry) is convenient. Start it by specifying a fork url for your relevant network and then pass in `127.0.0.1:8545` as the rpc_url arg.