from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Mengizinkan akses dari frontend (CORS)

@app.route('/api/status')
def status():
    return jsonify({
        "status": "success",
        "message": "Halo! Backend (Flask) dan Frontend (Nginx) berhasil terhubung secara terpisah.",
        "version": "2.0"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)