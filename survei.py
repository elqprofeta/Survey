import sys
import streamlit as st
import pandas as pd
import os

import os
import json




# Definir preguntas y respuestas
preguntas = [
    ("¿Qué tipo de actividades disfrutas más?", 
     ["Resolver acertijos o programar", "Leer o investigar historia", "Ayudar a las personas", 
      "Emprender o analizar negocios", "Dibujar, diseñar o crear música", "Viajar y explorar el mundo"]),

    ("Si pudieras elegir un proyecto, ¿cuál sería?", 
     ["Crear una aplicación o robot", "Escribir un libro o investigar historia", "Descubrir una cura para una enfermedad", 
      "Crear una empresa", "Diseñar un videojuego o escultura", "Pilotar un avión o diseñar motores de aviación"]),

    ("¿En qué área sientes más facilidad?", 
     ["Matemáticas y lógica", "Comunicación y escritura", "Empatía y trabajo con personas", 
      "Liderazgo y toma de decisiones", "Creatividad y expresión artística", "Orientación espacial y navegación"]),

    ("¿Qué tipo de problemas disfrutas resolver?", 
     ["Desafíos matemáticos o lógicos", "Debates filosóficos", "Casos médicos", 
      "Estrategias de mercado", "Creación de contenido visual o musical", "Manejo de emergencias y logística de vuelos"]),

    ("¿Cómo te imaginas en el futuro?", 
     ["Desarrollando tecnología", "Escribiendo o investigando", "Trabajando en salud", 
      "Dirigiendo una empresa", "Creando arte o música", "Volando aviones o trabajando en aeropuertos"]),
]

habilidades = [
    ("¿Qué idiomas hablas o te gustaría aprender?", 
     ["Inglés", "Portugués", "Alemán", "Chino Mandarín", "Italiano", "Otro", "Ninguna"]),

    ("¿Qué tan cómodo te sientes utilizando Excel avanzado?", 
     ["Principiante", "Intermedio", "Avanzado", "Ninguna"]),

    ("¿Qué tan cómodo te sientes utilizando herramientas de oficina (Word, Excel, PowerPoint)?", 
     ["Principiante", "Intermedio", "Avanzado", "Ninguna"]),

    ("¿Qué nivel de conocimiento tienes en programas de arquitectura y modelado en 3D (rendering)?", 
     ["Básico", "Intermedio", "Avanzado", "Ninguna"]),

    ("¿Qué nivel de conocimiento tienes con inteligencia artificial?", 
     ["Básico", "Intermedio", "Avanzado", "No tengo experiencia", "Ninguna"])
]

categorias = {
    "Ingeniería y Tecnología": ["Resolver acertijos o programar", "Crear una aplicación o robot", "Matemáticas y lógica",
                                "Desafíos matemáticos o lógicos", "Desarrollando tecnología"],
    "Humanidades": ["Leer o investigar historia", "Escribir un libro o investigar historia", "Comunicación y escritura",
                    "Debates filosóficos", "Escribiendo o investigando"],
    "Ciencias de la Salud": ["Ayudar a las personas", "Descubrir una cura para una enfermedad", "Empatía y trabajo con personas",
                              "Casos médicos", "Trabajando en salud"],
    "Negocios y Economía": ["Emprender o analizar negocios", "Crear una empresa", "Liderazgo y toma de decisiones",
                            "Estrategias de mercado", "Dirigiendo una empresa"],
    "Artes y Diseño": ["Dibujar, diseñar o crear música", "Diseñar un videojuego o escultura", "Creatividad y expresión artística",
                       "Creación de contenido visual o musical", "Creando arte o música"],
    "Aviación y Logística": ["Viajar y explorar el mundo", "Pilotar un avión o diseñar motores de aviación", "Orientación espacial y navegación",
                              "Manejo de emergencias y logística de vuelos", "Volando aviones o trabajando en aeropuertos"]
}

# Interfaz en Streamlit
st.title("Prueba de Orientación Vocacional con Recomendaciones")
st.write("Responde las siguientes preguntas para obtener tu perfil.")

# Contador de categorías según respuestas
contador_categorias = {cat: 0 for cat in categorias.keys()}

# Sección de preguntas principales
opciones_seleccionadas = []
for i, (pregunta, opciones) in enumerate(preguntas):
    respuesta = st.radio(pregunta, opciones, key=f"pregunta_{i}")
    opciones_seleccionadas.append(respuesta)

    # Sumar un punto a la categoría correspondiente
    for categoria, respuestas in categorias.items():
        if respuesta in respuestas:
            contador_categorias[categoria] += 1

# Sección de habilidades
habilidades_respuestas = {}
for i, (pregunta, opciones) in enumerate(habilidades):
    respuesta = st.radio(pregunta, opciones, key=f"habilidad_{i}")
#    respuesta = st.multiselect(pregunta, opciones, key=f"habilidad_{i}")
    habilidades_respuestas[pregunta] = respuesta

import firebase_admin
# from firebase_admin import credentials, firestore
from firebase_admin import credentials

# Inicializar Firebase ************* ------- *****


# Recuperar el JSON de las credenciales desde una variable de entorno
# firebase_credentials = os.getenv("FIREBASE_CREDENTIALS")
firebase_credentials = os.getenv("SURVEII")

if firebase_credentials:
    cred_dict = json.loads(firebase_credentials)  # Convertir la cadena en un diccionario Python
    cred = credentials.Certificate(cred_dict)    # Usar credenciales desde diccionario
    firebase_admin.initialize_app(cred)
else:
    raise ValueError("⚠️ No se encontraron credenciales de Firebase en las variables de entorno")

print(f"Ruta de credenciales de Firebase: {firebase_cred_path}")
if not os.path.exists(firebase_cred_path):
    print(f"No se encontró el archivo de credenciales en: {firebase_cred_path}")

    # Inicializar Firebase con el archivo de credenciales dinámicamente cargado #1
    print(f"Ruta de credenciales de Firebase: {firebase_cred_path}")
#    cred = credentials.Certificate(firebase_cred_path)                                    
    print ("va bien")
#    firebase_admin.initialize_app(cred)                                         #3
#    db = firestore.client()                                                     #4
#    print("Firebase inicializado correctamente.")                               #5 copia de la def arriba

#    firebase_admin.initialize_app(cred)

    db = firestore.client()

# Solicitar correo electrónico del usuario
user_email = st.text_input("Por favor ingresa tu correo electrónico:", "")

# Verificar si el correo no está vacío antes de guardar
if user_email:

# Inferencia de la mejor opción según respuestas  ******************
    if st.button("Obtener Resultado"):
    # Ordenar categorías según la cantidad de coincidencias
       categorias_ordenadas = sorted(contador_categorias.items(), key=lambda x: x[1], reverse=True)

    # Mostrar las mejores opciones
    st.subheader("Tus opciones recomendadas:")
    if len(categorias_ordenadas) >= 3:
       st.write(f"1️⃣ Primera opción: **{categorias_ordenadas[0][0]}**")
       st.write(f"2️⃣ Segunda opción: **{categorias_ordenadas[1][0]}**")
       st.write(f"3️⃣ Tercera opción: **{categorias_ordenadas[2][0]}**")
    else:
       st.write("No hay suficientes datos para determinar tres opciones.")

    # Mostrar habilidades y herramientas seleccionadas
    st.subheader("Habilidades y herramientas seleccionadas:")
    for pregunta, respuesta in habilidades_respuestas.items():
        st.write(f"{pregunta}: {respuesta}")

    # Inferencias y recomendaciones basadas en habilidades blandas
    st.subheader("📌 Recomendaciones para mejorar:")
    if habilidades_respuestas["¿Qué idiomas hablas o te gustaría aprender?"] == "Ninguna":
        st.write("🌍 Se recomienda aprender al menos un idioma adicional como Inglés o Portugués para mejorar oportunidades profesionales.")
    
    if habilidades_respuestas["¿Qué tan cómodo te sientes utilizando Excel avanzado?"] in ["Principiante", "Ninguna"]:
        st.write("📊 Aprender Excel avanzado puede ayudarte en cualquier carrera profesional.")

    if habilidades_respuestas["¿Qué nivel de conocimiento tienes con inteligencia artificial?"] in ["No tengo experiencia", "Ninguna"]:
        st.write("🤖 Familiarizarse con herramientas de IA como ChatGPT, Gemini o Copilot puede mejorar tus habilidades tecnológicas.")

    if habilidades_respuestas["¿Qué nivel de conocimiento tienes en programas de arquitectura y modelado en 3D (rendering)?"] == "Ninguna":
        st.write("🏗️ Considera aprender modelado en 3D si te interesa diseño y creatividad.")

    # Guardar resultados en Firebase
    # Intentar ejecutar código que puede generar un error
    try:
    #    user_id = "usuario_demo"  # Reemplazar con identificador real
    #    doc_ref = db.collection("resultados_vocacionales").document(user_email)
	
        top_categorias = [cat[0] for cat in categorias_ordenadas[:3]]  # Máximo 3 opciones
        while len(top_categorias) < 3:
            top_categorias.append("No determinado")

        doc_ref.set({
   	    "opcion_1": categorias_ordenadas[0][0],
  	    "opcion_2": categorias_ordenadas[1][0],
  	    "opcion_3": categorias_ordenadas[2][0],
   	    "habilidades": habilidades_respuestas
	})

        st.success("Tus respuestas han sido guardadas en Firebase.")
    except Exception as e:
        st.error(f"Error al guardar en Firebase: {e}")

    # Detener la ejecución para evitar que el script siga corriendo en segundo plano
    st.stop()
else:
    st.warning("Por favor, ingresa tu correo electrónico para continuar.")