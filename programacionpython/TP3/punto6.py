"""Ejercicio 6: Eliminar Duplicados
Escribe un programa que permita al usuario ingresar una lista de números y elimine los
elementos duplicados.
Pista:
 Utiliza la función set()."""
arreglo = []
dimension = int(input("Ingrese la dimension del arreglo: "))
for i in range(dimension):
    arreglo.append(int(input(f"Ingrese un valor para la posicion [{i}]: ")))

print(f"El arreglo es: {arreglo}")

arreglo = set(arreglo)
print(f"modificado es: {arreglo}")