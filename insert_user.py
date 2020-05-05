import mysql.connector
import bcrypt
import json
import os
import base64
from cryptography.fernet import Fernet

with open('api.json') as creds:
    credentials = json.load(creds)


def hash_smth(secret):
    secret = secret.encode()
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(secret, salt)
    return hashed.decode('utf-8')


def encrypt_smth(secret):
    key_input = credentials['encryption_key']
    key = base64.urlsafe_b64encode(key_input.encode())
    cipher_suite = Fernet(key)
    ciphered_text = cipher_suite.encrypt(secret.encode())
    return ciphered_text.decode('utf-8')


def add(email, name, password):
    cnx = mysql.connector.connect(user=credentials['mysql_user'], password=credentials['mysql_password'],
                                  host='127.0.0.1',
                                  database=credentials['mysql_database_name'])
    cursor = cnx.cursor()
    add_user = (
        "INSERT INTO user (email, name, password) VALUES (\" " + encrypt_smth(email)+"\", \"" + name+"\", \"" + hash_smth(password)+"\")")
    cursor.execute(add_user)
    cnx.commit()
    cnx.close()
    return
