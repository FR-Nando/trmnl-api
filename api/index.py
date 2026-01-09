from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/trmnl', methods=['GET'])
def get_json():
    # --- VOS DONNÉES ---
    donnees = {
        "salle": "SA.126",
        "qr_link": "https://votre-site.com",
        
        # Réunion actuelle
        "c_titre": "Workshop UX Design",
        "c_orga": "Julie M.",
        "c_date": "Lundi 18 Janv.",
        "c_heure": "16h00 - 18h00",
        
        # Réunion suivante
        "n_titre": "Comité Direction", # J'ajoute un titre pour la suivante
        "n_orga": "Équipe Tech",
        "n_date": "Lundi 18 Janv.",
        "n_heure": "18h00 - 19h00"
    }
    
    qr_api = f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={donnees['qr_link']}"

    return jsonify({
        "merge_variables": {
            "VAR_SALLE": donnees['salle'],
            "VAR_QR": qr_api,
            
            # Variables Actuelles
            "TITRE": donnees['c_titre'],
            "QUI": donnees['c_orga'],
            "DATE": donnees['c_date'],
            "HEURE": donnees['c_heure'],
            
            # Variables Suivantes
            "NEXT_TITRE": donnees['n_titre'],
            "NEXT_QUI": donnees['n_orga'],
            "NEXT_DATE": donnees['n_date'],
            "NEXT_HEURE": donnees['n_heure']
        }
    })

if __name__ == '__main__':
    app.run()
