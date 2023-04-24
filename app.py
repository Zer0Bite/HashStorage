import datetime
import random
import os
import uuid
import pyfiglet
from flask import Flask, request, jsonify, render_template, send_file
from pathlib import Path
import InGetTransact
import hash

intro = pyfiglet.figlet_format('Hash Storage', font='slant')
print('-------------------------------------------------------------------------')
print(intro)
print('-------------------------------------------------------------------------')

app = Flask(__name__, template_folder='template', static_folder='static')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hash')
def index_hash():
    return render_template('hash.html')


@app.route('/hash', methods=['POST'])
def upload_hash():
    file = request.files['file']
    file.save(file.filename)
    file_hash = hash.getHash(file.filename)
    user_address = request.form['userAddress']
    user_id = uuid.uuid4().int
    certificate_path = os.path.join('certificate', file.filename + '.cert')
    with open(certificate_path, "w") as certificate_file:
        certificate_file.write('Address: ' + str(user_address) + '\n' +
                                'File Name: ' + file.filename + '\n' +
                                'ID: ' + str(user_id) + '\n' +
                                'File Hash: ' + file_hash + '\n' +
                                'Date: ' + str(datetime.datetime.now()))
    transact = InGetTransact.Transact()
    transact.insertTransaction(str(user_address), int(user_id), str(file_hash))
    Path(file.filename).unlink()
    return send_file(certificate_path, as_attachment=True)



@app.route('/verify')
def verify_index():
    return render_template('verify.html')


@app.route('/verify', methods=['POST'])
def verify():
    user_address = request.form['userAddress']
    user_id = request.form['userId']
    file = request.files['file']
    file.save(file.filename)
    file_hash = hash.getHash(file.filename)
    transact = InGetTransact.Transact()
    hash_in_block = transact.getTransaction(str(user_address), int(user_id))
    Path(file.filename).unlink()
    if file_hash == hash_in_block:
        return render_template('verify.html', show_panel_good=True)
    else:
        return render_template('verify.html', show_panel_bad=True)


if __name__ == '__main__':
    app.run()
