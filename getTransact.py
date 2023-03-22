import json
from web3 import Web3, HTTPProvider


def getTransaction(_address, _id):

    blockchainAddress = 'http://127.0.0.1:7545'
    web3 = Web3(HTTPProvider(blockchainAddress))
    compiledContractPath = 'build/contracts/HashStorage.json'
    deployedContractAddress = '0xca547958Be0b9B44e79bfaEc7B25F14A8276bec1'

    with open(compiledContractPath) as file:
        contractJson = json.load(file)

        contractAbi = contractJson['abi']

    contract = web3.eth.contract(address=deployedContractAddress, abi=contractAbi)
    senderAddress = _address
    output = contract.functions.getHash(_id).call({'from': web3.toChecksumAddress(senderAddress)})

    return output
