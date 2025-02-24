# --- Este ejemplo sirve tambien para alucinaciones --- #
""" 
Contador de vocales
Descripción: Escribe un programa que cuente cuántas 
vocales hay en una palabra ingresada por el usuario.
"""

texto = """
Un modelo de IA es un programa informático diseñado para realizar tareas que normalmente requieren inteligencia humana, como aprender, razonar o tomar decisiones. Estos modelos se basan en algoritmos y grandes cantidades de datos para identificar patrones, hacer predicciones y mejorar su rendimiento con el tiempo. Algunos ejemplos comunes de modelos de IA incluyen los asistentes virtuales como Siri o Alexa, los sistemas de recomendación de plataformas como Netflix o Spotify, y los chatbots que encontramos en sitios web para interactuar con los clientes. Los modelos de IA están transformando diversas industrias y aspectos de nuestra vida cotidiana, desde la medicina hasta el transporte y el entretenimiento.
"""

texto = texto.lower()
vocales = "aeiou"
contador = 0
for letra in texto:
    if letra in vocales:
        contador += 1

print(f"El texto tiene {contador} vocales")


# este algoritmo tiene un error en que no cuenta las vocales con tilde
# y en que no cuenta las vocales con diéresis
# para solucionar esto, se puede usar el método replace() para reemplazar las vocales con tilde y diéresis por vocales sin tilde y sin diéresis respectivamente

texto = texto.replace("á", "a")
texto = texto.replace("é", "e")
texto = texto.replace("í", "i")
texto = texto.replace("ó", "o")
texto = texto.replace("ú", "u")
vocales = "aeiou"
contador = 0
for letra in texto:
    if letra in vocales:
        contador += 1
        
print(f"El texto tiene {contador} vocales")