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

## Cómo usarlo

