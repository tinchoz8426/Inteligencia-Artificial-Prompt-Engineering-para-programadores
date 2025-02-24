import json

# Ruta al archivo JSON
ruta_archivo = 'productos.json'

# Abrir el archivo JSON
with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
    # Cargar el contenido del archivo JSON
    datos = json.load(archivo)
    print(type(datos)) # para mostrar que lo transforma a dict

# Imprimir el contenido del archivo JSON
# productos = json.dumps(datos, indent=4)
# print(productos)

# Iterar sobre la lista de productos y mostrar nombre y precio
for producto in datos['productos']:
    nombre = producto['nombre']
    precio = producto['precio']
    print(f"Nombre: {nombre}, Precio: ${precio:.2f}")
