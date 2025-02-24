# funcion para calcular el promedio de notas
def promedio_notas(notas):
    suma = 0
    for nota in notas:
        suma += nota
    return suma / len(notas)

# lista de notas
notas = [10, 20, 30, 40, 50]

# calcular el promedio de notas
promedio = promedio_notas(notas)

# imprimir el promedio de notas
print(f"El promedio de notas es: {promedio}")