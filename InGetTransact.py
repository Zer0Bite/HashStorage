
import json
from web3 import Web3, HTTPProvider


BLOCKCHAIN_ADDRESS = 'http://127.0.0.1:7545'
COMPILED_CONTRACT_PATH = 'build/contracts/HashStorage.json'
DEPLOYED_CONTRACT_ADDRESS = '0xBa4f9a0EC4b79d6BE9f4efB21eB861CE2c97c6b0'


class Transact:
    def __init__(self, blockchain_address, compiled_contract_path,deployed_contract_address):
        self.blockchain_address = blockchain_address
        self.compiled_contract_path = compiled_contract_path
        self.deployed_contract_address = deployed_contract_address
        self.web3 = Web3(HTTPProvider(blockchain_address))
        self.contract = self.connect()

    def connect(self):
        with open(self.compiled_contract_path) as file:
            contract_json = json.load(file)
            contract_abi = contract_json['abi']
        return self.web3.eth.contract(address=self.deployed_contract_address, abi=contract_abi)

    def getTransaction(self, _address, _id):
        senderAddress = _address
        output = self.contract.functions.getHash(_id).call({'from': self.web3.to_checksum_address(senderAddress)})

        return output

    def insertTransaction(self, _address, _id, _hash):

        senderAddress = _address
        txHash = self.contract.functions.insertHash(_id, _hash).transact({'from': self.web3.to_checksum_address(senderAddress)})
        txReceipt = self.web3.eth.wait_for_transaction_receipt(txHash)

        if txReceipt['status'] == 1:
            print('Transaction successful!')
        else:
            print('Transaction failed!')


transact_in = Transact(BLOCKCHAIN_ADDRESS, COMPILED_CONTRACT_PATH, DEPLOYED_CONTRACT_ADDRESS)

transact_get = Transact(BLOCKCHAIN_ADDRESS, COMPILED_CONTRACT_PATH, DEPLOYED_CONTRACT_ADDRESS)