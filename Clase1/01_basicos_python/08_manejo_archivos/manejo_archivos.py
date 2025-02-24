# Lectura de un archivo de texto
""" # Abrir un archivo en modo lectura ('r')
with open('archivo.txt', 'r') as archivo:
    contenido = archivo.read()
    print(contenido) """

######################################

# Escritura en un archivo de texto
""" # Abrir un archivo en modo escritura ('w')
with open('archivo.txt', 'w') as archivo:
    archivo.write('Hola, mundo!\n')
    archivo.write('Este es un ejemplo de escritura en un archivo.') """

######################################

# Leer un archivo línea por línea
""" with open('archivo.txt', 'r') as archivo:
    for linea in archivo:
        print(linea.strip())  # strip() elimina los saltos de línea """

######################################

# Manejo de excepciones al trabajar con archivos
""" try:
    with open('archivo_inexistente.txt', 'r') as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    print("El archivo no existe.") """

######################################

# Uso de seek() y tell() para manipular la posición del cursor
""" with open('archivo.txt', 'r') as archivo:
    archivo.seek(10)  # Mueve el cursor al byte 10
    print(archivo.tell())  # Muestra la posición actual del cursor
    contenido = archivo.read(5)  # Lee los siguientes 5 bytes
    print(contenido)

# El método seek() permite mover el cursor dentro del archivo a una 
# posición específica, mientras que tell() devuelve la posición 
# actual del cursor. Esto es útil para acceder a partes específicas de un archivo. """

######################################

# Leer y escribir archivos CSV
""" import csv

# Escribir en un archivo CSV
with open('datos.csv', 'w', newline='') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(['Nombre', 'Edad', 'Ciudad'])
    escritor.writerow(['Alice', '30', 'Nueva York'])
    escritor.writerow(['Bob', '25', 'Los Ángeles'])

# Leer un archivo CSV
with open('datos.csv', 'r') as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila) """

######################################

# Manejo de archivos JSON
import json

# Escribir en un archivo JSON
datos = {
    "nombre": "Alice",
    "edad": 30,
    "ciudad": "Nueva York"
}

with open('datos.json', 'w') as archivo:
    json.dump(datos, archivo)

# Leer un archivo JSON
with open('datos.json', 'r') as archivo:
    datos_leidos = json.load(archivo)
    print(datos_leidos)

######################################

# Manejo de archivos con os y shutil
import os
import shutil

# Crear un directorio
os.mkdir('nuevo_directorio')

# Copiar un archivo
shutil.copy('archivo.txt', 'nuevo_directorio/copia_archivo.txt')

# Eliminar un archivo
os.remove('nuevo_directorio/copia_archivo.txt')

# Eliminar un directorio
os.rmdir('nuevo_directorio')

######################################