"""Ejercicio 11: Contar Ocurrencias de un Elemento
Escribe un programa que permita al usuario ingresar una lista y un número, y cuente
cuántas veces aparece ese número en la lista.
"""
arreglo = []
dimen = int(input("Ingrese la dimension del arreglo: "))

for x in range(dimen):
    arreglo.append(int(input(f"Ingrese un valor para la posicion [{x}]")))

num = int(input("Que numero desea saber si se repite? "))    
cont = 0
for i in range(dimen):
    if arreglo[i] == num:
        cont +=1

print(f"El nº {num} aparece {cont} veces.")