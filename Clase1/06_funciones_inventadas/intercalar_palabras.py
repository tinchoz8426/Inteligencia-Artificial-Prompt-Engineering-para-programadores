# Realizad con Qwen2.5-Max

"""
Descripción de la función:
Nombre : intercalar_palabras
Descripción : Toma dos cadenas de texto como entrada y devuelve una nueva cadena donde 
las palabras de ambas cadenas se intercalan una a una. Si una cadena tiene más palabras 
que la otra, las palabras restantes de la cadena más larga se añaden al final.
Parámetros :
cadena1: Primera cadena de texto.
cadena2: Segunda cadena de texto.
Valor de retorno : Una nueva cadena con las palabras intercaladas.

Explicación del código:
División de cadenas : Usamos split() para dividir las cadenas en listas de palabras.
Intercalado : Iteramos sobre el rango de la longitud máxima entre las dos listas. En cada 
iteración, añadimos una palabra de la primera lista (si queda alguna) y luego una palabra 
de la segunda lista (si queda alguna).
Unión de palabras : Finalmente, usamos ' '.join() para unir las palabras intercaladas en 
una sola cadena separada por espacios.
Esta función puede ser útil en situaciones donde quieras mezclar textos de diferentes 
fuentes o crear efectos visuales interesantes con texto.
"""

def intercalar_palabras(cadena1, cadena2):
    # Dividir ambas cadenas en listas de palabras
    palabras1 = cadena1.split()
    palabras2 = cadena2.split()
    
    # Determinar la longitud de las listas
    longitud_maxima = max(len(palabras1), len(palabras2))
    
    # Intercalar palabras
    resultado = []
    for i in range(longitud_maxima):
        if i < len(palabras1):
            resultado.append(palabras1[i])
        if i < len(palabras2):
            resultado.append(palabras2[i])
    
    # Unir las palabras intercaladas en una sola cadena y devolverla
    return ' '.join(resultado)

# Ejemplo de uso
cadena1 = "Hola mundo este es un ejemplo"
cadena2 = "Python es divertido"

resultado = intercalar_palabras(cadena1, cadena2)
print(resultado)