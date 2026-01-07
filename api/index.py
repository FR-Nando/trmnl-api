from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/trmnl', methods=['GET'])
def get_json():
    # TEST FINAL POUR VERCEL
    return jsonify({
        "merge_variables": {
            "VAR_SALLE": "SA.126 (VERCEL)",
            "VAR_TITRE": "TEST REUSSI !!!",
            "VAR_QUI": "Moi",
            "VAR_QUAND": "Maintenant",
            "VAR_SUIVANT_QUI": "Personne",
            "VAR_SUIVANT_QUAND": "Demain",
            "VAR_QR": "https://api.qrserver.com/v1/create-qr-code/?data=test"
        }
    })

if __name__ == '__main__':
    app.run()
