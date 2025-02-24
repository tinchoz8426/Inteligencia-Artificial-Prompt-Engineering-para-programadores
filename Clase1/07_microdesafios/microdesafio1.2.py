"""
🏴‍☠️ Desafío: La Búsqueda del Tesoro Numérico 🏴‍☠️
🎯 Objetivo:
Crear un programa en Python que simule la búsqueda de un tesoro escondido en un mapa cuadrado. 
Utiliza conceptos básicos como funciones, manejo de errores, ciclos y generación de números aleatorios.
📜 Instrucciones:
1️⃣Tamaño del Mapa:
Pide al usuario que introduzca el tamaño del mapa (por ejemplo, 5 para un mapa de 5x5). 🗺️

2️⃣ Generación del Tesoro:
Utiliza la librería random para generar aleatoriamente la posición del tesoro dentro del mapa (fila y columna). 🎲

3️⃣ Búsqueda del Tesoro:
Solicita al usuario que ingrese dos números (fila y columna) para adivinar la posición del tesoro. 🔍

Después de cada intento, informa si la fila o columna introducida es mayor o menor que la posición real del tesoro. 
Por ejemplo, si la fila es muy alta o baja, o si la columna es mayor o menor. ⬆️⬇️⬅️➡️

4️⃣ Validación de Entradas:
Asegúrate de que el programa maneje errores en caso de que el usuario ingrese valores no numéricos o fuera del rango permitido. 🚫

5️⃣ Finalización del Juego:
Cuando el usuario adivine correctamente ambas coordenadas, muestra un mensaje de felicitaciones y finaliza el juego. 🎉🏆

6️⃣ Extensión Opcional:
Permite que el usuario juegue múltiples rondas, llevando un conteo del número de intentos en cada partida. 🔄

Incorpora un sistema de puntaje que recompense las partidas completadas en menos intentos. 💯

🛠️ Sugerencia de Uso de Prompts de IA:
Experimenta formulando un prompt para que la IA te ayude a estructurar funciones en Python, o revisa tu 
código para corregir errores. Por ejemplo, puedes pedir:

"Muéstrame cómo crear una función en Python que valide si una entrada es un número dentro de un rango específico." 🤖
"""



# Resolucion archivada en ChatGPT y aca tambien:
import random

def obtener_numero(mensaje, limite):
    """Solicita un número al usuario y valida que esté dentro del rango permitido."""
    while True:
        try:
            numero = int(input(mensaje))
            if 1 <= numero <= limite:
                return numero
            else:
                print(f"Por favor, ingresa un número entre 1 y {limite}.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")

def jugar():
    print("¡Bienvenido a la Búsqueda del Tesoro Numérico!")

    # Solicitar el tamaño del mapa
    tamanio = obtener_numero("Ingresa el tamaño del mapa (por ejemplo, 5 para un mapa de 5x5): ", 20)
    
    # Generar posición aleatoria del tesoro
    tesoro_fila = random.randint(1, tamanio)
    tesoro_columna = random.randint(1, tamanio)
    
    intentos = 0
    
    while True:
        print("\n¡Adivina dónde está el tesoro!")
        
        # Solicitar coordenadas del usuario
        fila = obtener_numero(f"Ingrese el número de fila (1 a {tamanio}): ", tamanio)
        columna = obtener_numero(f"Ingrese el número de columna (1 a {tamanio}): ", tamanio)
        
        intentos += 1
        
        # Verificar la posición ingresada
        if fila == tesoro_fila and columna == tesoro_columna:
            print(f"¡Felicidades! ¡Encontraste el tesoro en {intentos} intentos!")
            break
        else:
            # Dar pistas
            if fila < tesoro_fila:
                print("El tesoro está en una fila más alta.")
            elif fila > tesoro_fila:
                print("El tesoro está en una fila más baja.")
            
            if columna < tesoro_columna:
                print("El tesoro está en una columna más a la derecha.")
            elif columna > tesoro_columna:
                print("El tesoro está en una columna más a la izquierda.")

    print("¡Gracias por jugar!")

# Iniciar el juego
jugar()
