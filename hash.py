import hashlib
from os import path


def getHash(filename):

    if path.isfile(filename) is False:
        raise Exception("File not found! Try again")

    hashSha256 = hashlib.sha256()

    with open(filename, 'rb') as file:

        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            hashSha256.update(chunk)

    return hashSha256.hexdigest()


