"""Ejercicio 7: Promedio de una Lista
Escribe un programa que permita al usuario ingresar una lista de números y calcule el
promedio de los elementos."""

arreglo = []
dimen = int(input("Ingrese la dimension del arreglo: "))
for i in range(dimen):
    arreglo.append(int(input(f"Ingrese un valor para la posicion [{i}]: ")))

suma = sum(arreglo)
promedio = suma/dimen
print(f"Los nº del arreglo son: {arreglo}, la suma de estos es: {suma} y el promedio es: {promedio} ")