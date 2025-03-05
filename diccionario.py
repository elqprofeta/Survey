import json
import firebase_admin
from firebase_admin import credentials

firebase_cred_json = os.getenv("FIREBASE_CREDENTIALS")

if firebase_cred_json:
    cred_dict = json.loads(firebase_cred_json)  # Convertir string a diccionario
    cred = credentials.Certificate(cred_dict)
    firebase_admin.initialize_app(cred)
else:
    print("Error: No se pudo cargar FIREBASE_CREDENTIALS")
