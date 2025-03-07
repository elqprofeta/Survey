import os
import json
import firebase_admin
from firebase_admin import credentials, firestore

# Cargar credenciales desde la variable de entorno
firebase_credentials = os.getenv("FIREBASE_CREDENTIALS")
if firebase_credentials:
    cred = credentials.Certificate(json.loads(firebase_credentials))
    firebase_admin.initialize_app(cred)
    db = firestore.client()
else:
    print("Error: FIREBASE_CREDENTIALS no está configurada correctamente.")

# Función para guardar datos en Firestore
def guardar_datos(collection, doc_id, datos):
    try:
        doc_ref = db.collection(collection).document(doc_id)
        doc_ref.set(datos)
        print("Datos guardados correctamente en Firestore.")
    except Exception as e:
        print(f"Error al guardar datos: {e}")

# Datos de prueba
datos_usuario = {
    "nombre": "Juan Pérez",
    "edad": 30,
    "correo": "juan@example.com"
}

guardar_datos("vocacion", "usuario_123", datos_usuario)  # Guarda en la colección "vocacion"
