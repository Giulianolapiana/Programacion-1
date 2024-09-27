"""Ejercicio 3: Invertir una Lista
Escribe un programa que permita al usuario ingresar una lista y la invierta.
"""
arreglo = []
dimension = int(input("ingrese la dimension del arreglo: "))

for i in range(dimension):
    arreglo.append(int(input(f"ingrese un valor para la posicion [{i}]: ")))

print(f"El arreglo original es: {arreglo}")
arreglo.reverse()
print(f"Ahora al revez es: {arreglo}")