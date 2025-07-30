import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    greeting_from_compose = os.getenv("GREETING", "Nenhuma saudacao definida.")

    return jsonify({
        "service": "Service A",
        "message": "Ola do Servico A!",
        "version": "1.0.0",
        "from_compose": greeting_from_compose
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)