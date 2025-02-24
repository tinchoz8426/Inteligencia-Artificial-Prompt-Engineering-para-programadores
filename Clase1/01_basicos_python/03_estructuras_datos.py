# listas
# Crear una lista
mi_lista = [1, 2, 3, 4, 5]

# Acceder a un elemento por índice
print(mi_lista[0])  # Salida: 1

# Modificar un elemento
mi_lista[1] = 20
print(mi_lista)  # Salida: [1, 20, 3, 4, 5]

# Añadir un elemento al final
mi_lista.append(6)
print(mi_lista)  # Salida: [1, 20, 3, 4, 5, 6]

# Eliminar un elemento por valor
mi_lista.remove(3)
print(mi_lista)  # Salida: [1, 20, 4, 5, 6]

# Obtener la longitud de la lista
print(len(mi_lista))  # Salida: 5

######################################

# tuplas
# Crear una tupla
mi_tupla = (1, 2, 3, 4, 5)

# Acceder a un elemento por índice
print(mi_tupla[2])  # Salida: 3

# Intentar modificar un elemento (esto dará un error)
# mi_tupla[1] = 20  # TypeError: 'tuple' object does not support item assignment

# Obtener la longitud de la tupla
print(len(mi_tupla))  # Salida: 5

# Las tuplas pueden contener diferentes tipos de datos
tupla_mixta = (1, "Hola", 3.14, True)
print(tupla_mixta)  # Salida: (1, 'Hola', 3.14, True)

######################################

# diccionarios
# Crear un diccionario
mi_diccionario = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Madrid"
}

# Acceder a un valor por clave
print(mi_diccionario["nombre"])  # Salida: Juan

# Modificar un valor
mi_diccionario["edad"] = 26
print(mi_diccionario)  # Salida: {'nombre': 'Juan', 'edad': 26, 'ciudad': 'Madrid'}

# Añadir un nuevo par clave-valor
mi_diccionario["profesion"] = "Ingeniero"
print(mi_diccionario)  # Salida: {'nombre': 'Juan', 'edad': 26, 'ciudad': 'Madrid', 'profesion': 'Ingeniero'}

# Eliminar un par clave-valor
del mi_diccionario["ciudad"]
print(mi_diccionario)  # Salida: {'nombre': 'Juan', 'edad': 26, 'profesion': 'Ingeniero'}

# Obtener todas las claves
print(mi_diccionario.keys())  # Salida: dict_keys(['nombre', 'edad', 'profesion'])

# Obtener todos los valores
print(mi_diccionario.values())  # Salida: dict_values(['Juan', 26, 'Ingeniero'])

######################################

# conjuntos
# Crear un conjunto
mi_conjunto = {1, 2, 3, 4, 5}

# Añadir un elemento
mi_conjunto.add(6)
print(mi_conjunto)  # Salida: {1, 2, 3, 4, 5, 6}

# Intentar añadir un elemento duplicado (no se añadirá)
mi_conjunto.add(3)
print(mi_conjunto)  # Salida: {1, 2, 3, 4, 5, 6}

# Eliminar un elemento
mi_conjunto.remove(4)
print(mi_conjunto)  # Salida: {1, 2, 3, 5, 6}

# Operaciones con conjuntos
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}

# Unión
print(conjunto_a.union(conjunto_b))  # Salida: {1, 2, 3, 4, 5}

# Intersección
print(conjunto_a.intersection(conjunto_b))  # Salida: {3}

# Diferencia
print(conjunto_a.difference(conjunto_b))  # Salida: {1, 2}

# Obtener la longitud del conjunto
print(len(mi_conjunto))  # Salida: 5