from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/trmnl', methods=['GET'])
def get_json():
    # Le test le plus simple du monde
    return jsonify({
        "merge_variables": {
            "MESSAGE": "CONNEXION OK"
        }
    })

if __name__ == '__main__':
    app.run()
