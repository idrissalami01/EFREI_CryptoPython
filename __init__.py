from cryptography.fernet import Fernet
from flask import Flask, render_template

app = Flask(__name__)

# 🔑 Clé globale pour les routes sans clé utilisateur
global_key = Fernet.generate_key()
f = Fernet(global_key)

@app.route('/')
def hello_world():
    return render_template('hello.html')

# ✅ Chiffrement avec clé globale (session actuelle)
@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    valeur_bytes = valeur.encode()
    token = f.encrypt(valeur_bytes)
    return f"Valeur encryptée : {token.decode()}"

# ✅ Déchiffrement avec clé globale
@app.route('/decrypt/<string:token>')
def decryptage(token):
    try:
        token_bytes = token.encode()
        decrypted = f.decrypt(token_bytes)
        return f"Valeur décryptée : {decrypted.decode()}"
    except Exception as e:
        return f"Erreur lors du déchiffrement : {str(e)}"

# ✅ Chiffrement avec une clé fournie par l'utilisateur
@app.route('/encrypt/<key>/<valeur>')
def encrypt_personnalise(key, valeur):
    try:
        fernet = Fernet(key.encode())
        valeur_bytes = valeur.encode()
        token = fernet.encrypt(valeur_bytes)
        return f"Valeur encryptée : {token.decode()}"
    except Exception as e:
        return f"Erreur lors du chiffrement : {str(e)}"


# ✅ Déchiffrement avec une clé fournie
@app.route('/decrypt/<key>/<path:token>')
def decrypt_personnalise(key, token):
    try:
        fernet = Fernet(key.encode())
        token_bytes = token.encode()
        decrypted = fernet.decrypt(token_bytes)
        return f"Valeur décryptée : {decrypted.decode()}"
    except Exception as e:
        return f"Erreur lors du déchiffrement : {str(e)}"

# ✅ Générer une nouvelle clé à utiliser
@app.route('/generate-key')
def generate_key():
    return Fernet.generate_key().decode()

if __name__ == "__main__":
    app.run(debug=True)
