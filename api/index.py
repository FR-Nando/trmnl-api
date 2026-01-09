from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/trmnl', methods=['GET'])
def get_json():
    # --- 1. VOS DONNÉES À MODIFIER ---
    donnees = {
        "salle": "SA.126 (Fixe)",
        "qr_link": "https://votre-site-de-resa.com",
        
        # Réunion actuelle
        "titre": "Workshop UX Design",
        "orga": "Julie M.",
        "date": "Lundi 18 Janv.",
        "heure": "16h00 - 18h00",
        
        # Réunion suivante
        "next_titre": "Comité Direction",
        "next_orga": "Équipe Tech",
        "next_date": "Lundi 18 Janv.",
        "next_heure": "18h00 - 19h00"
    }
    
    # --- 2. GÉNÉRATION QR CODE ---
    qr_api = f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={donnees['qr_link']}"

    # --- 3. MAPPING STRICT POUR VOTRE HTML ---
    return jsonify({
        "merge_variables": {
            # Variables appelées directement {{ VAR_... }}
            "VAR_SALLE": donnees['salle'],
            "VAR_QR": qr_api,
            
            # Variables appelées via {{ merge_variables.XXX }}
            "TITRE": donnees['titre'],
            "QUI": donnees['orga'],
            "DATE": donnees['date'],
            "HEURE": donnees['heure'],
            
            "NEXT_TITRE": donnees['next_titre'],
            "NEXT_QUI": donnees['next_orga'],
            "NEXT_DATE": donnees['next_date'],
            "NEXT_HEURE": donnees['next_heure']
        }
    })

if __name__ == '__main__':
    app.run()
