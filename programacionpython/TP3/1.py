""" Escribe un programa que permita al usuario ingresar una lista de números y calcule la
suma de todos los elementos en la lista. """
import random

def addRamdom(linkedList,n):
    for i in range(n):
        linkedList.append(random.randint(0,20))

def sumaList(linkedList):
    suma = 0
    for i in range(len(linkedList)):
        suma = linkedList[i] + suma
    return suma


linkedList = []
n = int(input("cuantos elementos desea agregar: "))
addRamdom(linkedList,n)
suma = sumaList(linkedList)
print(linkedList)
print(suma)