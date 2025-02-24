# Variables básicas
""" # Entero
edad = 25

# Flotante
altura = 1.75

# Cadena de texto
nombre = "Juan"

# Booleano
es_estudiante = True

# Imprimir las variables
print("Nombre:", nombre)
print("Edad:", edad)
print("Altura:", altura)
print("Es estudiante:", es_estudiante)

# para ver el tipo de dato
print(type(nombre))
print(type(edad)) """

######################################

# casting
# Tipos de casting comunes en Python:
# int(): Convierte un valor a un entero.
# float(): Convierte un valor a un número de punto flotante.
# str(): Convierte un valor a una cadena de texto.
# bool(): Convierte un valor a un booleano (True o False).
# list(): Convierte un valor a una lista.
# tuple(): Convierte un valor a una tupla.
# set(): Convierte un valor a un conjunto.
# dict(): Convierte un valor a un diccionario.

""" # entero a flotante
x = 10
y = float(x)
print(y)  # Output: 10.0
print(type(y))

# flotante a entero
x = 10.7
y = int(x)
print(y)  # Output: 10 --> perdida de precisión
print(type(y))  # Output: <class 'int'>

# entero a cadena
x = 42
y = str(x)
print(y)  # Output: '42'
print(type(y))  # Output: <class 'str'>

# cadena a entero
x = "123"
y = int(x)
print(y)  # Output: 123
print(type(y))  # Output: <class 'int'>

# cadena a flotante
x = "123.45"
y = float(x)
print(y)  # Output: 123.45
print(type(y))  # Output: <class 'float'>

# booleano a entero
x = True
y = int(x)
print(y)  # Output: 1
print(type(y))  # Output: <class 'int'>

# entero a booleano
x = 0
y = bool(x)
print(y)  # Output: False
print(type(y))  # Output: <class 'bool'>

# Errores de conversión
x = "abc"
y = int(x)  # Esto lanzará un ValueError

# Conversión implícita
x = 10 + 5.5  # x será 15.5 (un flotante) """

######################################

# Reasignación de variables
""" puntuacion = 100
print("Puntuación inicial:", puntuacion)

puntuacion = 200
print("Puntuación actualizada:", puntuacion) """

######################################

