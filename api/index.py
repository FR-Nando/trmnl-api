from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/trmnl', methods=['GET'])
def get_json():
    # --- 1. MODIFIEZ VOS INFOS ICI ---
    donnees = {
        "salle": "SA.126 (Fixe)",
        "qr_url_cible": "https://votre-site-de-resa.com",
        
        # Réunion En Cours
        "titre": "Workshop UX Design",
        "organisateur": "Julie M.",
        "heure": "16h00 - 18h00",
        
        # Réunion Suivante
        "prochain_orga": "Équipe Tech",
        "prochaine_heure": "18h00 - 19h00"
    }
    
    # --- 2. GÉNÉRATION DU QR CODE ---
    qr_api = f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&color=000000&margin=0&data={donnees['qr_url_cible']}"

    # --- 3. ENVOI AU TRMNL (Ne touchez pas en dessous) ---
    return jsonify({
        "merge_variables": {
            "VAR_SALLE": donnees['salle'],
            "VAR_TITRE": donnees['titre'],
            "VAR_QUI": f"Par : {donnees['organisateur']}",
            "VAR_QUAND": f"Aujourd'hui | {donnees['heure']}",
            
            "VAR_SUIVANT_QUI": f"Suivant : {donnees['prochain_orga']}",
            "VAR_SUIVANT_QUAND": f"Heure : {donnees['prochaine_heure']}",
            
            "VAR_QR": qr_api
        }
    })

if __name__ == '__main__':
    app.run()
