# -------------------------- #
# Módulos estándar de Python #
# -------------------------- #

# math (funciones matemáticas)
import math
print(math.sqrt(16))  # Raíz cuadrada
print(math.pi)

######################################

# random (generación de números aleatorios)
import random
print(random.randint(1, 10))  # Número aleatorio entre 1 y 10
print(random.choice(["a", "b", "c"]))  # Elemento aleatorio de una lista

######################################

# datetime (manejo de fechas y horas)
from datetime import datetime
ahora = datetime.now()
print(ahora)  # Fecha y hora actual

######################################

# os (interacción con el sistema operativo)
import os
print(os.getcwd())

######################################

# sys (interacción con el intérprete de Python)
import sys
print(sys.version)  # Versión de Python

######################################


# ------------------- #
# Módulos de terceros #
# ------------------- #

# Puedes instalar y usar módulos de terceros usando pip.
# Por ejemplo, para usar el módulo requests (para hacer solicitudes HTTP)
# pip install requests
import requests

respuesta = requests.get("https://www.example.com")
print(respuesta.status_code)  # Código de estado HTTP

######################################