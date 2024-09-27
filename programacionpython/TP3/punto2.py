"""Ejercicio 2: Encontrar el Mayor y el Menor
Escribe un programa que pida al usuario una lista de números y encuentre el mayor y
el menor de ellos.
"""
arreglo = []
dimension = int(input("ingrese la dimension del arreglo: "))
mayor = 0
for i in range(dimension):
    arreglo.append(int(input(f"Ingrese un valor para la posicion [{i}]: ")))
    if arreglo[i] > mayor:
        mayor = arreglo[i]

print(f"El arreglo tiene los valores: {arreglo} y el numero mayor es: {mayor}")

maxim = max(arreglo)
print(f"el mayor numero es: {maxim}")        