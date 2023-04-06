#!/bin/bash
echo "Install truffle"
sudo apt update
sudo apt install nodejs
sudo apt install npm
sudo npm install -g truffle
sudo apt -y install python3-pip
sudo pip install web3==6.0.0
sudo pip install flask==2.2.2
sudo pip install pyfiglet
echo "Compile project"
truffle compile
truffle develop
