import streamlit as st
import openai
import faiss
import numpy as np
from dotenv import load_dotenv
import os

# Configurar tu API Key
load_dotenv()
apikey = os.getenv("clave")
openai.api_key = apikey

# Cargar el índice FAISS y documentos
import faiss
import json
index = faiss.read_index("faiss_index.index")
with open("embeddings/document_texts.json", "r") as f:
    documentos = json.load(f)




openai.api_key = apikey
def get_embedding(text):
    # Este es el método correcto para la versión >= 1.0.0
    response = openai.embeddings.create(
        model="text-embedding-ada-002",
        input=text
    )
    return response.data[0].embedding

def search(query_embedding, k=5):
    # Buscar los k documentos más cercanos al embedding de la consulta
    D, I = index.search(np.array([query_embedding]).astype('float32'), k)
    return I, D

def retrieve_context(query_text, k=5):
    # Obtener el embedding de la consulta
    query_embedding = get_embedding(query_text)
    
    # Buscar los documentos más relevantes
    indices, distances = search(query_embedding, k)
    
    # Recuperar los textos correspondientes (si el índice está en rango)
    relevant_texts = [documentos[i] for i in indices[0] if i < len(documentos)]
    
    return " ".join(relevant_texts)


from openai import OpenAI
client = OpenAI(api_key=apikey)
def generate_response(prompt):
    response = client.chat.completions.create(
        model="ft:gpt-3.5-turbo-0125:personal::AwCV0n9Y",  # Ajusta con el nombre de tu modelo fine-tuned
        messages=[
            {"role": "system", "content": "Eres una persona que está teniendo nua conversación distendida con un divulgador de ciencia"},
            {"role": "user", "content": prompt}
        ],
        temperature=0.9,  # Ajusta la creatividad de la respuesta (0.0 - 1.0)
        max_tokens=1150,   # Número máximo de tokens en la respuesta
        top_p=1,          # Control de muestreo por núcleo (0.0 - 1.0)
        frequency_penalty=0,  # Penaliza repeticiones
        presence_penalty=0
    )
    return response.choices[0].message.content



# Interfaz de usuario con Streamlit
st.title("Asistente de Ciencia Personalizado 🧑‍🔬")
st.write("Haz preguntas relacionadas con ciencia o reflexiones profundas.")

# Entrada del usuario
user_input = st.text_input("Escribe tu pregunta:")

if user_input:
    with st.spinner("Buscando información y generando respuesta..."):
        # Recuperar contexto relevante
        context = retrieve_context(user_input)
        
        # Crear prompt combinando contexto y pregunta
        prompt = f"Contexto relevante: {context}\nPregunta: {user_input}\nRespuesta:"
        
        # Obtener respuesta del modelo
        response = generate_response(prompt)
        
        # Mostrar resultado
        st.write("**Respuesta:**", response)