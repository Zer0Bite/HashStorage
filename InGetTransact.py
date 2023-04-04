import json
from web3 import Web3, HTTPProvider


BLOCKCHAIN_ADDRESS = 'http://127.0.0.1:7545'
WEB3 = Web3(HTTPProvider(BLOCKCHAIN_ADDRESS))
COMPILED_CONTRACT_PATH = 'build/contracts/HashStorage.json'
DEPLOYED_CONTRACT_ADDRESS = '0x90f4eab8D774d611d18c31e1689d97f733C49114'

with open(COMPILED_CONTRACT_PATH) as file:
    CONTRACT_JSON = json.load(file)
    CONTRACT_ABi = CONTRACT_JSON['abi']

CONTRACT = WEB3.eth.contract(address=DEPLOYED_CONTRACT_ADDRESS, abi=CONTRACT_ABi)


class Transact:

    def getTransaction(self, _address, _id):
        senderAddress = _address
        output = CONTRACT.functions.getHash(_id).call({'from': WEB3.to_checksum_address(senderAddress)})

        return output

    def insertTransaction(self, _address, _id, _hash):

        senderAddress = _address
        txHash = CONTRACT.functions.insertHash(_id, _hash).transact({'from': WEB3.to_checksum_address(senderAddress)})
        txReceipt = WEB3.eth.wait_for_transaction_receipt(txHash)

        if txReceipt['status'] == 1:
            print('Transaction successful!')
        else:
            print('Transaction failed!')




