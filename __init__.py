from cryptography.fernet import Fernet
from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                

@app.route('/decrypt/<string:token>')
def decryptage(token):
    try:
        token_bytes = token.encode()
        decrypted = f.decrypt(token_bytes)
        return f"Valeur décryptée : {decrypted.decode()}"
    except Exception as e:
        return f"Erreur lors du déchiffrement : {str(e)}"
@app.route('/encrypt/<key>/<valeur>')
def encrypt_personnalise(key, valeur):
    try:
        fernet = Fernet(key.encode())
        valeur_bytes = valeur.encode()
        token = fernet.encrypt(valeur_bytes)
        return f"Valeur encryptée : {token.decode()}"
    except Exception as e:
        return f"Erreur lors du chiffrement : {str(e)}"

@app.route('/decrypt/<key>/<token>')
def decrypt_personnalise(key, token):
    try:
        fernet = Fernet(key.encode())
        token_bytes = token.encode()
        decrypted = fernet.decrypt(token_bytes)
        return f"Valeur décryptée : {decrypted.decode()}"
    except Exception as e:
        return f"Erreur lors du déchiffrement : {str(e)}"


from cryptography.fernet import Fernet
print(Fernet.generate_key().decode())

                                                                                                                       
@app.route('/')
def hello_world():
    return render_template('hello.html') #comm

key = Fernet.generate_key()
f = Fernet(key)

@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    valeur_bytes = valeur.encode()  # Conversion str -> bytes
    token = f.encrypt(valeur_bytes)  # Encrypt la valeur
    return f"Valeur encryptée : {token.decode()}"  # Retourne le token en str
                                                                                                                                                     
if __name__ == "__main__":
  app.run(debug=True)
