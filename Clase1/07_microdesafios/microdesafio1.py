"""
Crear una funcion en Python que determine si un numero
es primo o no.
"""

# Función realizada sin IA
def es_primo(numero):
    for n in range(2, numero):
        if numero % n == 0:
            print(f"El número {numero} NO es primo")
            break
    else:
        print(f"El número {numero} ES primo")

es_primo(4)
es_primo(5)
es_primo(17)
es_primo(39)
es_primo(83)


# Función realizada con Amazon Q
# Crear una funcion en Python que determine si un numero
# es primo o no.
def es_primo(numero):
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    numero = int(input("Ingrese un número: "))
    if es_primo(numero):
        print(f"El número {numero} es primo")
    else:
        print(f"El número {numero} no es primo")

if __name__ == "__main__":
    main()