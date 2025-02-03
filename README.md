# CosmosBot 

### El ChatBot con la personalidad de un divulgador de ciencia

Este proyecto combina la técnica del fine-tuning de modelos de lenguaje y la Retrieval-augmented-generation (RAG) para responder preguntas interesantes sobre ciencia y filosofía. 

## Características

- Fine-tuning para un modelo de lenguaje *gpt-3.5-turbo-0125* basado en la personalidad de un divulgador y youtuber de ciencia
- Recuperación de texto relevante con FAISS para su utilización en el contexto del modelo
    - Creación de embeddings para almacenamiento de información relativa a diferentes temáticas 
    - Indexación de embeddings con FAISS
    - Búsqueda de los k elementos más cercanos (a la consulta) con FAISS para combinarlos con el prompt y obtener mejores respuestas
- App de Streamlit para probar el ChatBot

## Aplicación de Streamlit
Usar el chat en el siguiente link: https://cosmosbot-modelo-con-rag-y-fine-tuning-iurmqrelaawektdbwcktka.streamlit.app/

## Cómo usarlo | Consejos
- **Hacer una pregunta o plantear un tema científico.**  
- **Preferible un tono informal (opcional).**  

### Temáticas del embedding:  
- ⭐ **Las estrellas y sus ciclos**  
- 🌌 **Las galaxias, la Vía Láctea y Andrómeda**  
- 🌈 **La atmósfera y su efecto en las ondas de luz**  
- 🧭 **La estrella polar, brújulas y los polos magnéticos**  

- **Repetir la pregunta con otras palabras en caso de respuesta corta o genérica.**  

- **Dar feedback:**  
  Por ejemplo, si en una respuesta sobre estrellas te responde:  
  💬 *"En las estrellas tienen lugar reacciones nucleares."*  
  Puedes preguntar:  
  💬 *"¿Y qué reacciones nucleares pueden tener lugar en las estrellas?"*
