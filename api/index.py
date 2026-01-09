from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/trmnl', methods=['GET'])
def get_json():
    # ==========================================
    # 1. ZONE DE TEXTE
    # ==========================================
    
    # Infos générales
    nom_de_la_salle = "VI.126"
    
    # NOUVEAU : Message d'information en bas de page
    message_info = "Toute réunion sera supprimée si la salle reste vide 15 mn après le début de réunion"
    
    # Infos : RÉUNION EN COURS
    reunion_actuelle = {
        "titre": "Workshop UX Design",
        "organisateur": "Julie M.",
        "date_jour": "Lundi 18 Janv.",
        "creneau": "16h00 - 18h00"
    }

    # Infos : PROCHAINE RÉUNION
    reunion_suivante = {
        "titre": "Comité Direction",
        "organisateur": "Équipe Tech",
        "date_jour": "Lundi 18 Janv.",
        "creneau": "18h00 - 19h00"
    }

    # Image QR Code (Lien fixe GitHub)
    mon_image_qr = "https://github.com/FR-Nando/trmnl-api/blob/main/qrcode.png?raw=true"

    # ==========================================
    # 2. ENVOI AU TRMNL
    # ==========================================
    return jsonify({
        "merge_variables": {
            "VAR_SALLE": nom_de_la_salle,
            "VAR_QR": mon_image_qr,
            
            # La nouvelle variable
            "INFOS": message_info,
            
            "TITRE": reunion_actuelle["titre"],
            "QUI": reunion_actuelle["organisateur"],
            "DATE": reunion_actuelle["date_jour"],
            "HEURE": reunion_actuelle["creneau"],
            
            "NEXT_TITRE": reunion_suivante["titre"],
            "NEXT_QUI": reunion_suivante["organisateur"],
            "NEXT_DATE": reunion_suivante["date_jour"],
            "NEXT_HEURE": reunion_suivante["creneau"]
        }
    })

if __name__ == '__main__':
    app.run()
