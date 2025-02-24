# condicional if
x = 10

if x > 5:
    print("x es mayor que 5")

######################################

# condicional if-else
x = 3

if x > 5:
    print("x es mayor que 5")
else:
    print("x no es mayor que 5")

######################################

# condicional if-elif-else
x = 7

if x > 10:
    print("x es mayor que 10")
elif x > 5:
    print("x es mayor que 5 pero menor o igual a 10")
else:
    print("x es menor o igual a 5")

######################################

# condicionales anidados
x = 12

if x > 10:
    if x % 2 == 0:
        print("x es mayor que 10 y es par")
    else:
        print("x es mayor que 10 y es impar")
else:
    print("x es menor o igual a 10")

######################################

# operadores ternarios
x = 8
resultado = "Mayor que 5" if x > 5 else "Menor o igual a 5"
print(resultado)

######################################

# condicional con and y or
x = 7
y = 3

if x > 5 and y > 2:
    print("Ambas condiciones son verdaderas")

if x > 5 or y > 5:
    print("Al menos una de las condiciones es verdadera")

######################################

# condicional con in
frutas = ["manzana", "banana", "cereza"]

if "banana" in frutas:
    print("La banana está en la lista de frutas")