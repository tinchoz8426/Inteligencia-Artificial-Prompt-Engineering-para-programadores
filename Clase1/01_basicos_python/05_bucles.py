# bucle for
for i in range(5):  # Itera desde 0 hasta 4
    print(i)

######################################

# iterar sobre una lista con for
frutas = ["manzana", "banana", "cereza"]

for fruta in frutas:
    print(fruta)

######################################

# iterar sobre una cadena con for
for letra in "Python":
    print(letra)

######################################

# usar enumerate para obtener índice y valor:
frutas = ["manzana", "banana", "cereza"]

for indice, fruta in enumerate(frutas):
    print(f"Índice: {indice}, Fruta: {fruta}")

######################################

# iterar sobre un diccionario
persona = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}

for clave, valor in persona.items():
    print(f"{clave}: {valor}")

######################################

# bucle while
contador = 0

while contador < 5:
    print(contador)
    contador += 1

######################################

# bucle infinito con break
while True:
    respuesta = input("Escribe 'salir' para terminar: ")
    if respuesta == "salir":
        break
    print("Continuando...")

######################################

# usar continue para saltar una iteración
contador = 0

while contador < 5:
    contador += 1
    if contador == 3:
        continue  # Salta la iteración cuando contador es 3
    print(contador)

######################################

# bucles anidados
for i in range(3):  # Bucle exterior
    for j in range(2):  # Bucle interior
        print(f"i: {i}, j: {j}")

######################################

# uso de else en bucles
for i in range(3):
    print(i)
else:
    print("Bucle terminado")

# ejemplo con while
contador = 0
while contador < 3:
    print(contador)
    contador += 1
else:
    print("Bucle terminado")

######################################

# bucle for con range inverso
for i in range(5, 0, -1):
    print(i)

######################################

# bucle for con zip
nombres = ["Juan", "Ana", "Luis"]
edades = [25, 30, 35]

for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")

######################################

# comprensión de listas (bucles implícitos)
cuadrados = [x**2 for x in range(5)]
print(cuadrados)

# con condicion
pares = [x for x in range(10) if x % 2 == 0]
print(pares)