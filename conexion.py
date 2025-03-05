import firebase_admin
from firebase_admin import credentials, firestore
import os
import tempfile
import streamlit as st

# Recuperar el secreto del JSON desde la variable de entorno
firebase_cred_json = os.getenv("FIREBASE_CREDENTIALS")
# firebase_cred_json = os.getenv("SURVEII")
# firebase_cred_json = os.getenv("CREED")

# Verifica que el secreto esté disponible
if not firebase_cred_json:
    st.error(f"El secreto de Firebase no está configurado correctamente.")
else:
    # Crear un archivo temporal para guardar el contenido del JSON
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(firebase_cred_json.encode('utf-8'))
        temp_file_path = temp_file.name

    # Inicializar Firebase solo si no está ya inicializado
    if not firebase_admin._apps:
        cred = credentials.Certificate(temp_file_path)  # Usar el archivo temporal
        firebase_admin.initialize_app(cred)

    # Obtener una referencia a Firestore
    db = firestore.client()

    # Ahora puedes usar db para acceder a Firestore y almacenar datos
    st.success("Conexión a Firebase exitosa.")

st.stop()