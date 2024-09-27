""" Escribe un programa que multiplique cada elemento de una lista bidimensional por un 
valor escalar dado por el usuario. """
import numpy as np 
matriz = np.array([ 
[10, 8, 3], 
[4, 22, 6], 
[7, 18, 99] 
]) 
print(matriz)

n = int(input("ingrese un valor para multiplicar a la matriz => "))

producto = n*matriz
print("El resultado es: " , producto)
