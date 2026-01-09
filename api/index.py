from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/trmnl', methods=['GET'])
def get_json():
    # ==========================================
    # 1. ZONE DE CONFIGURATION (Modifiez ici)
    # ==========================================
    
    # LA VARIABLE SALLE (Celle qui s'affiche en gros et gras)
    nom_de_la_salle = "VI.126" 
    
    # Lien vers lequel pointe le QR Code
    lien_reservation = "https://votre-intranet.com/reservation/VI126"

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

    # ==========================================
    # 2. LOGIQUE (Ne pas toucher en dessous)
    # ==========================================

    # Génération automatique de l'image du QR Code
    qr_code_genere = f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&color=000000&margin=0&data={lien_reservation}"

    # Création du JSON exact attendu par votre HTML TRMNL
    return jsonify({
        "merge_variables": {
            # Variable Salle (Haut droite)
            "VAR_SALLE": nom_de_la_salle,
            
            # Variable QR Code (Bas droite)
            "VAR_QR": qr_code_genere,
            
            # Variables Réunion En Cours
            "TITRE": reunion_actuelle["titre"],
            "QUI": reunion_actuelle["organisateur"],
            "DATE": reunion_actuelle["date_jour"],
            "HEURE": reunion_actuelle["creneau"],
            
            # Variables Réunion Suivante
            "NEXT_TITRE": reunion_suivante["titre"],
            "NEXT_QUI": reunion_suivante["organisateur"],
            "NEXT_DATE": reunion_suivante["date_jour"],
            "NEXT_HEURE": reunion_suivante["creneau"]
        }
    })

# Nécessaire pour le fonctionnement sur Vercel
if __name__ == '__main__':
    app.run()
