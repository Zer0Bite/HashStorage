import InGetTransact
transact = InGetTransact.Transact()

address = input()
Id = input()
Hash = input()

transact.insertTransaction(str(address), int(Id), str(Hash))

print(transact.getTransaction('0x29F38fe8336f5B087108eA26b48Fd452546b81E6', 1))