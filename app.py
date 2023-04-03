import random
from flask import Flask, request, jsonify, render_template, session, send_file, redirect
import InGetTransact
import hash

app = Flask(__name__,  template_folder='template', static_folder='static')


@app.route('/')
def Index():
    return render_template('index.html')


@app.route('/hash')
def IndexHash():
    return render_template('hash.html')


@app.route('/hash', methods=['POST'])
def UploadHash():

    file = request.files['file']
    file.save(file.filename)
    fileHash = hash.getHash(file.filename)
    userAddress = request.form['userAddress']
    userId = random.getrandbits(212)
    with open('certificate\\certificate.txt', "w") as fileCertificate:
        fileCertificate.write('Address: ' + str(userAddress) + '\n' + 'File Name: ' + file.filename + '\n' + 'ID: ' + str(userId) + '\n' + 'File Hash: ' + fileHash)
    transact = InGetTransact.Transact()
    transact.insertTransaction(str(userAddress), int(userId), str(fileHash))
    path = 'certificate\\certificate.txt'
    return send_file(path, as_attachment=True)


@app.route('/verify')
def VerifyIndex():
    return render_template('verify.html')


@app.route('/verify', methods=['POST'])
def Verify():
    userAddress = request.form['userAddress']
    userId = request.form['userId']
    file = request.files['file']
    file.save(file.filename)
    fileHash = hash.getHash(file.filename)
    transact = InGetTransact.Transact()
    hashInBlock = transact.getTransaction(str(userAddress), int(userId))


    if fileHash == hashInBlock:
        return render_template('good.html')
    else:
        return render_template('bad.html')


if __name__ == '__main__':
    app.run(debug=True)