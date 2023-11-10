from web3 import (Web3, HTTPProvider)
from web3.contract.contract import Contract
from eth_account.signers.local import (LocalAccount)
import json
import os

 
# Set provider
w3 = Web3(HTTPProvider('SET PROVIDER'))


# set env var
DEPLOYER: LocalAccount = w3.eth.account.from_key(os.environ.get("PRIVATE_KEY"))
# Set constructor param to right governance addr
V2_OWNER = None

abi = None
bytecode = None


gas_limit = 10_000_000
nonce = w3.eth.get_transaction_count(DEPLOYER.address)


# NOTE: Best to check with whichever network you are deploying to since some have weird gas systems (e.g. Boba network)
gas_price = w3.eth.gas_price


with open("./canonical_artifacts/UniswapV2Factory.json", 'r') as artifact:
    artifact = json.load(artifact)
    abi = artifact["abi"]
    bytecode = artifact["bytecode"]


UniV2Factory: Contract = w3.eth.contract(abi=abi, bytecode=bytecode)


tx = UniV2Factory.constructor(V2_OWNER).build_transaction({"from": DEPLOYER, "gasPrice": gas_price, 'gas': gas_limit, 'nonce': nonce})
singed_tx = DEPLOYER.sign_transaction(tx)

res: bytes = w3.eth.send_raw_transaction(singed_tx.rawTransaction)
receipt = w3.eth.wait_for_transaction_receipt(res)

if receipt["status"] == 1:
    print(f"Deployed UniV2 to {receipt['contractAddress']}")
else:
    print(f"Error in deployment")
    print(receipt)   

