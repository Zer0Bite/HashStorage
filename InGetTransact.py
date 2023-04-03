import json
from web3 import Web3, HTTPProvider

print('Enter contract address')

BLOCKCHAIN_ADDRESS = 'http://127.0.0.1:9545'
WEB3 = Web3(HTTPProvider(BLOCKCHAIN_ADDRESS))
COMPILED_CONTRACT_PATH = 'build/contracts/HashStorage.json'
DEPLOYED_CONTRACT_ADDRESS = 'enter you address smart-contract'

with open(COMPILED_CONTRACT_PATH) as file:
    contractJson = json.load(file)
    contractAbi = contractJson['abi']

contract = WEB3.eth.contract(address=DEPLOYED_CONTRACT_ADDRESS, abi=contractAbi)


class Transact:

    def getTransaction(self, _address, _id):
        senderAddress = _address
        output = contract.functions.getHash(_id).call({'from': WEB3.to_checksum_address(senderAddress)})

        return output

    def insertTransaction(self, _address, _id, _hash):

        senderAddress = _address
        txHash = contract.functions.insertHash(_id, _hash).transact({'from': WEB3.to_checksum_address(senderAddress)})
        txReceipt = WEB3.eth.wait_for_transaction_receipt(txHash)

        if txReceipt['status'] == 1:
            print('Transaction successful!')
        else:
            print('Transaction failed!')




