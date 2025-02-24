# instalar la libreria --> pip install google-genai

# obtener la API key --> https://aistudio.google.com/

# # Importa la biblioteca para usar la IA generativa de Google
from google import genai

# Crea un cliente para conectar con la IA.
client = genai.Client(api_key="API_KEY_GEMINI")

response = client.models.generate_content( # Llama al modelo para generar contenido
    model="gemini-2.0-flash", # Especifica el modelo Gemini a utilizar
    contents="Dame un consejo sobre programación", # El mensaje que le enviamos al modelo (nuestro "prompt")
)

print(response.text) # Imprime la respuesta del modelo


# EXPLICACION:
# Este código utiliza la biblioteca google-generativeai para interactuar con los 
# modelos de IA generativa de Google, específicamente con el modelo Gemini.
# Su objetivo principal es obtener un consejo sobre programación.
