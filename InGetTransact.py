import json
from web3 import Web3, HTTPProvider


BLOCKCHAIN_ADDRESS = 'http://127.0.0.1:7545'
WEB3 = Web3(HTTPProvider(BLOCKCHAIN_ADDRESS))
COMPILED_CONTRACT_PATH = 'build/contracts/HashStorage.json'
DEPLOYED_CONTRACT_ADDRESS = '0x6384c68D6Cc53B3841e157a52a1650b2ce926340'


class Transact:

    def getTransaction(self, _address, _id):

        with open(COMPILED_CONTRACT_PATH) as file:
            contractJson = json.load(file)

            contractAbi = contractJson['abi']

        contract = WEB3.eth.contract(address=DEPLOYED_CONTRACT_ADDRESS, abi=contractAbi)
        senderAddress = _address
        output = contract.functions.getHash(_id).call({'from': WEB3.toChecksumAddress(senderAddress)})

        return output

    def insertTransaction(self, _address, _id, _hash):

        with open(COMPILED_CONTRACT_PATH) as file:
            contractJson = json.load(file)

            contractAbi = contractJson['abi']

        contract = WEB3.eth.contract(address=DEPLOYED_CONTRACT_ADDRESS, abi=contractAbi)
        senderAddress = _address
        txHash = contract.functions.insertHash(_id, _hash).transact({'from': WEB3.toChecksumAddress(senderAddress)})
        txReceipt = WEB3.eth.waitForTransactionReceipt(txHash)

        if txReceipt['status'] == 1:
            print('Transaction successful!')
        else:
            print('Transaction failed!')




