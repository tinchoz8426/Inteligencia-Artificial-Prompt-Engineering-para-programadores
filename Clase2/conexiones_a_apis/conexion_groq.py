# instalar la libreria --> pip install groq

# obtener la API key --> https://console.groq.com/

# importamos la clase Groq de la libreria
from groq import Groq

# Se crea una instancia de la clase `Groq` y se le pasa un parámetro `api_key` con un valor  de API válida. Esta clave de API se utiliza para autenticar la instancia del cliente y permitirle acceder a los servicios de Groq.
client = Groq(
    api_key="API_KEY_GROQ"
)

# Aquí, se llama al método `create` del objeto `chat.completions` de la instancia del cliente `client`. Este método crea una nueva conversación y devuelve un objeto que representa la respuesta del modelo de lenguaje.
# El método `create` recibe un parámetro que es un diccionario con dos claves:
# * `messages`: una lista de mensajes que se utilizarán para inicializar la conversación. En este caso, la lista contiene un solo mensaje con dos claves:
#  + `role`: especifica el rol del mensaje, que en este caso es `"user"`, lo que indica que el mensaje proviene del usuario.
#  + `content`: el contenido del mensaje, que en este caso es la cadena `"Dame un consejo sobre programación"`.
# * `model`: especifica el modelo de lenguaje que se utilizará para generar la respuesta. En este caso, se utiliza el modelo `"llama-3.3-70b-versatile"`.
# La expresión `chat_completion.choices[0].message.content` se refiere a:
# * `chat_completion`: el objeto que representa la respuesta del modelo de lenguaje.
# * `choices`: una lista de respuestas generadas por el modelo. En este caso, se selecciona la primera respuesta (`[0]`).
# * `message`: el mensaje de respuesta generado por el modelo.
# * `content`: el contenido del mensaje de respuesta.

input_usuario = input("Ingrese su pregunta: ")
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": input_usuario,
        }
    ],
    model="llama-3.3-70b-versatile",
)

print(chat_completion.choices[0].message.content)
