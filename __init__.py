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
@app.route('/encrypt1/<string:valeur>')
def encryptage(valeur):
    valeur_bytes = valeur.encode()
    token = f.encrypt(valeur_bytes)
    return f"Valeur encryptée : {token.decode()}"

# ✅ Déchiffrement avec clé globale
@app.route('/decrypt1/<string:token>')
def decryptage(token):
        token_bytes = token.encode()
        decrypted = f.decrypt(token_bytes)
        return f"Valeur décryptée : {decrypted.decode()}"


# ✅ Chiffrement avec une clé fournie par l'utilisateur
@app.route('/encrypt2/<key>/<valeur>')
def encrypt_personnalise(key, valeur):
        fernet = Fernet(key.encode())
        valeur_bytes = valeur.encode()
        token = fernet.encrypt(valeur_bytes)
        return f"Valeur encryptée : {token.decode()}"



# ✅ Déchiffrement avec une clé fournie
@app.route('/decrypt2/<key>/<path:token>')
def decrypt_personnalise(key, token):
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
