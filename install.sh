#!/bin/bash
echo "Install truffle"
sudo apt install npm
sudo npm install -g truffle
sudo pip install web3==6.0.0
echo "Compile project"
truffle compile
truffle develop
