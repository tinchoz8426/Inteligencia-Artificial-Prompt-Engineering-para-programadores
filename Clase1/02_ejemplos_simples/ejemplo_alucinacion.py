# algoritmo que elimina numeros pares
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lista = [1, 2, 3, 4, 4, 4, 4, 5, 6, 7, 8, 9, 10]
for i in lista:
    if i % 2 == 0:
        lista.remove(i)

print(lista)


"""
Este codigo lo propuso Amazon Codewhisperer, hay un error en la linea 6, ya que al eliminar 
un elemento de la lista, la lista se actualiza y el bucle se detiene antes de recorrer todos 
los elementos. Para solucionar esto, se debe recorrer la lista en reversa.
A su vez esta solucion tambien la propuso Amazon Codewhisperer
"""
lista = [1, 2, 3, 4, 4, 4, 4, 5, 6, 7, 8, 9, 10]

for i in reversed(lista):
    if i % 2 == 0:
        lista.remove(i)

print(lista)