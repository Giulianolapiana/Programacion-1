"""Ejercicio 1: Suma de Elementos
Escribe un programa que permita al usuario ingresar una lista de números y calcule la
suma de todos los elementos en la lista."""
arreglo = []
dimension = int(input("ingrese la dimension del arreglo: "))
for i in range(dimension):
    arreglo.append(int(input(f"Ingrese valores para la posicion [{i}]: ")))
    
print(f"los valores del arreglo son: {arreglo}")
suma = sum(arreglo)
print(f"La suma de los valores es: {suma}")