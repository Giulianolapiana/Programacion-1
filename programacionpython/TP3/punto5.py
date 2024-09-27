"""Ejercicio 5: Multiplicar Elementos por un Valor
Escribe un programa que multiplique cada elemento de una lista de números por un
valor ingresado por el usuario.
"""
arreglo = []
dimension = int(input("ingrese la dimension del arreglo: "))
num = int(input("Ingrese el numero por el que desea multiplicar los valores del arreglo: "))

for i in range(dimension):
    arreglo.append(int(input(f"Ingrese un valor para la posicion [{i}]: ")))

print(f"El arreglo es: {arreglo}")
for j in range(dimension):
    print(f"{arreglo[j]} * {num} = {arreglo[j]*num}")
