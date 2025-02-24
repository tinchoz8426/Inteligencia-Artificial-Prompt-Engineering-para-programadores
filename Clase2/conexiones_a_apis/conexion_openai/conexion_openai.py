# instalar la libreria --> pip install openai

# obtener la API key (clave de API)

# Importa la librería openai, que es el SDK oficial de OpenAI para interactuar con sus modelos de IA.
import openai

from dotenv import load_dotenv # pip install python-dotenv

import os

# Cargar el archivo .env
load_dotenv()

try:
    # Se crea un objeto client de la clase OpenAI, que se usa para interactuar con la API de OpenAI.
    client = openai.OpenAI(api_key=os.getenv("OPEN_AI_KEY"))
    
    # Se hace una solicitud a la API de OpenAI para generar una respuesta de chat usando el modelo "gpt-4o-mini".
    # La conversación se define con messages, que es una lista de diccionarios.
    # El mensaje enviado tiene:
    # "role": "user" → Indica que este mensaje es del usuario.
    # "content": "Dame un consejo sobre programación" → El contenido del mensaje, es decir, lo que el usuario le pregunta al modelo.
    respuesta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Dame un consejo sobre programación"}, {"role": "system", "content": "Eres un asistente que responde con bromas."}],
    )
    
    # respuesta es la respuesta generada por el modelo de OpenAI.
    # choices[0] accede a la primera opción de respuesta generada por el modelo.
    # .message.content obtiene el texto de la respuesta del modelo.
    print(respuesta.choices[0].message.content)
    
except Exception as e:
    print(f"Error con la API: {e}")



# Roles en la API de OpenAI (role)
# En los mensajes enviados a la API de OpenAI, el campo "role" define el emisor del mensaje. Los valores posibles son:

# 1- "system" → Mensajes que configuran el comportamiento del modelo.
# 2- "user" → Mensajes escritos por el usuario que hace la consulta.
# 3- "assistant" → Respuestas generadas por el modelo de OpenAI.

# Ejemplo de cada uno:
# messages = [
#     {"role": "system", "content": "Responde en un tono profesional y técnico."},
#     {"role": "user", "content": "¿Cómo funciona un algoritmo de búsqueda binaria?"},
#     {"role": "assistant", "content": "Un algoritmo de búsqueda binaria divide repetidamente la lista en mitades..."},
# ]

