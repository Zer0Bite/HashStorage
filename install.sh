#!/bin/bash
echo "Install truffle"
sudo apt install npm
sudo npm install -g truffle
sudo pip install web3==6.0.0
sudo pip install flask==2.2.2
sudo pip install pyfiglet
echo "Compile project"
truffle compile
truffle develop
