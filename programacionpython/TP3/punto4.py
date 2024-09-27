"""Ejercicio 4: Contar Elementos Pares e Impares
Escribe un programa que pida al usuario una lista de números y cuente cuántos de
ellos son pares y cuántos son impares.
"""
arreglo = []
dimen = int(input("ingrese la dimension del arreglo: "))
par = 0
impar = 0
for i in range(dimen):
    arreglo.append(int(input(f"ingrese el valor de la posicion [{i}]: ")))
    if arreglo[i] % 2 == 0:
        par +=1
    else:
        impar +=1

print(f"Los valores del arreglo son {arreglo}, la cantidad de numeros pares es: {par} y la cantidad de impares es: {impar}")