"""Ejercicio 10: Eliminar un Elemento por su Índice
Escribe un programa que permita al usuario ingresar una lista de números y eliminar
un elemento en un índice especificado.
"""
arreglo = []
dimen = int(input("Ingrese la dimension del arreglo: "))
for x in range(dimen):
    arreglo.append(int(input(f"Ingrese un valor para la posicion [{x}]")))
indice = int(input("Ingrese el nº de indice del cual desea borrar "))
arreglo.remove(arreglo[indice])

print(f"El arreglo quedó: {arreglo}")