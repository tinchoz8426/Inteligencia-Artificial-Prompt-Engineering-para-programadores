# Funciones simples que no toman argumentos ni devuelven valores
def saludar():
    print("¡Hola, mundo!")

saludar()

######################################

# Funciones que toman uno o más parámetros
def saludar(nombre):
    print(f"¡Hola, {nombre}!")

saludar("Juan") 

######################################

# Funciones que tienen valores predeterminados para algunos argumentos
def saludar(nombre="mundo"):
    print(f"¡Hola, {nombre}!")

saludar()  # Usa el valor predeterminado
saludar("Ana")

######################################

# Funciones que procesan datos y devuelven un resultado usando return
def suma(a, b):
    return a + b

resultado = suma(3, 5)
print(resultado) 

######################################

# Funciones que devuelven varios valores en forma de tupla
def operaciones(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    return suma, resta, multiplicacion

resultados = operaciones(10, 5)
print(resultados)

######################################

# Funciones que aceptan un número variable de argumentos posicionales
def sumar(*args):
    total = 0
    for numero in args:
        total += numero
    return total

resultado = sumar(1, 2, 3, 4, 5)
print(resultado)

######################################

# Funciones que aceptan un número variable de argumentos de palabras clave
def mostrar_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Juan", edad=25, ciudad="Madrid")

######################################

# Funciones pequeñas y anónimas definidas con lambda
cuadrado = lambda x: x**2
print(cuadrado(5))

######################################

# Funciones que se llaman a sí mismas para resolver un problema
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5)) 

######################################

# Funciones como objetos de primera clase
# En Python, las funciones son objetos de primera clase, 
# lo que significa que pueden ser pasadas como argumentos, 
# devueltas por otras funciones o asignadas a variables.
def aplicar_funcion(funcion, valor):
    return funcion(valor)

def cuadrado(x):
    return x**2

resultado = aplicar_funcion(cuadrado, 4)
print(resultado)

######################################

# Funciones con anotaciones de tipo
def suma(a: int, b: int) -> int:
    return a + b

resultado = suma(3, 5)
print(resultado)

######################################

# Funciones dentro de funciones (closures)
# Funciones definidas dentro de otras funciones 
# que capturan variables del ámbito exterior.
def exterior(mensaje):
    def interior():
        print(mensaje)
    return interior

mi_funcion = exterior("¡Hola desde el closure!")
mi_funcion()