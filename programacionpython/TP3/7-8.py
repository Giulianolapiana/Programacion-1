""" Ejercicio 7: Promedio de una Lista
Escribe un programa que permita al usuario ingresar una lista de números y calcule el
promedio de los elementos.
Ejercicio 8: Encontrar Elementos Repetidos
Escribe un programa que identifique y muestre los elementos que se repiten en una
lista. """

#7
linkedList = list([5,2,8,5,1,9,10,9])
print(linkedList)
promedio = sum(linkedList)/len(linkedList)
print(promedio)

#8

# Usamos un diccionario para contar las repeticiones
contador = {}

# Contamos las veces que aparece cada número
for num in linkedList:
    if num in contador:
        contador[num] += 1
    else:
        contador[num] = 1

# Filtramos los elementos que se repiten y los mostramos
repetidos = [num for num, count in contador.items() if count > 1]

# Mostramos los elementos repetidos
if repetidos:
    print("Elementos repetidos:", repetidos)
else:
    print("No hay elementos repetidos.")