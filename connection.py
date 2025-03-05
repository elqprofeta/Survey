import os
import json
from firebase_admin import credentials, initialize_app

# Recuperar el secreto del JSON desde la variable de entorno
firebase_cred_json = os.getenv("FIREBASE_CREDENTIALS")

if firebase_cred_json:
    # Convertir el JSON en un diccionario
    firebase_cred_dict = json.loads(firebase_cred_json)

    # Inicializar Firebase
    cred = credentials.Certificate(firebase_cred_dict)
    initialize_app(cred)
    print("Encontré la ENV var FIREBASE_CREDENTIALS.")
else:
    print("No se encontró la variable de entorno FIREBASE_CREDENTIALS_JSON.")
