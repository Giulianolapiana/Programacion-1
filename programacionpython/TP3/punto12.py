"""Ejercicio 12: Sumar Listas Elemento por Elemento
Escribe un programa que sume dos listas de números elemento por elemento. Las
listas deben tener la misma longitud.
"""
arreglo1 = []
arreglo2 = []
dimen = int(input("Ingrese la dimension de los arreglos: "))
for i in range(dimen):
    arreglo1.append(int(input(f"Ingrese un valor para la posicion [{i}] del primero arreglo: ")))
    
for x in range(dimen):
    arreglo2.append(int(input(f"Ingrese un valor para la posicion [{x}] del segundo arreglo: ")))
print(f"Primer arreglo = {arreglo1}, segundo arreglo {arreglo2}")

suma = []
for y in range(dimen):
    suma.append(arreglo1[y] + arreglo2[y])
    
print(f"La suma de los valores, en nuevo arreglo es: {suma}")