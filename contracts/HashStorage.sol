pragma solidity ^0.8.17;

contract HashStorage {

    struct HashStruct {
        string hash;
    }

    mapping(uint => HashStruct) hashStructs;

    function insertHash(uint id, string memory hash) public {
        HashStruct storage key = hashStructs[id];
        key.hash = hash;
    }

    function getHash(uint id) public view returns (string memory) {
        HashStruct storage key = hashStructs[id];
        return (key.hash);
    }
}