from web3 import (Web3, HTTPProvider)
from web3.contract.contract import Contract
from eth_account.signers.local import (LocalAccount)
import json
import argparse

parser = argparse.ArgumentParser(description="") 
parser.add_argument('--private-key', type=str, help="Private key for deployer addr, beginning with 0x", required=True)
parser.add_argument('--rpc-url',type=str, help="specify the rpc endpoint you are deploying to (https)", required=True)
parser.add_argument('--governance-addr', type=str, help="specify the governance address to be used in constructor", required=True)

args =  parser.parse_args()
PRIVATE_KEY = args.private_key
RPC_URL = args.rpc_url
GOVERNANCE_ADDR = args.governance_addr


w3 = Web3(HTTPProvider(RPC_URL))


DEPLOYER: LocalAccount = w3.eth.account.from_key(PRIVATE_KEY)
abi = None
bytecode = None


gas_limit = 10_000_000
nonce = w3.eth.get_transaction_count(DEPLOYER.address)
# NOTE: Best to check with whichever network you are deploying to since some have odd gas systems (e.g. Boba network)
gas_price = w3.eth.gas_price


with open("./canonical_artifacts/UniswapV2Factory.json", 'r') as artifact:
    artifact = json.load(artifact)
    abi = artifact["abi"]
    bytecode = artifact["bytecode"]


UniV2Factory: Contract = w3.eth.contract(abi=abi, bytecode=bytecode)


tx = UniV2Factory.constructor(GOVERNANCE_ADDR).build_transaction({"from": DEPLOYER.address, "gasPrice": gas_price, 'gas': gas_limit, 'nonce': nonce})
singed_tx = DEPLOYER.sign_transaction(tx)

res: bytes = w3.eth.send_raw_transaction(singed_tx.rawTransaction)
receipt = w3.eth.wait_for_transaction_receipt(res)

if receipt["status"] == 1:
    print(f"Deployed UniV2 to {receipt['contractAddress']}")
else:
    print(f"Error in deployment")
    print(receipt)   

