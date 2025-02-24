# crea una lista de personas
personas = ["Juan", "Maria", "Pedro", "Ana", "Luis", "Carlos", "Sofia", "Miguel", "Laura", "Diego"]

# recorre la lista e imprime por pantalla un saludo a cada persona
for persona in personas:
    print(f"Hola {persona}, como estas?")

# recorre la lista y muestra por pantalla un saludo a cada persona, preguntando por su edad
for persona in personas:
    edad = input(f"Hola {persona}, ¿cuántos años tienes? ")
    print(f"{persona} tiene {edad} años.")



# Alternativa
# crea una lista con 10 nombres de personas
personas = ["Juan", "Pedro", "Maria", "Luis", "Ana", "Sofia", "Miguel", "Carlos", "Laura", "Javier"]

# recorre la lista e imprima un saludo a cada persona de la siguiente manera "Hola persona, ¿Como estas?"
for persona in personas:
    print(f"Hola {persona}, ¿Como estas?")