import json
import requests

# URL base de la API
url = "https://fastapiproject-1-eziw.onrender.com/oficial"

try:
    # Realizar una solicitud GET a la API
    response = requests.get(url)

    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        print("Respuesta de la API:")

        # Convertir la respuesta a un diccionario
        data = json.loads(response.text)
        print(data)
        print(data["venta"])
    else:
        print(f"Error al acceder a la API. Código de estado: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Ocurrió un error durante la solicitud: {e}")