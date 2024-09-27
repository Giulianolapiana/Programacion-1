""" Escribe un programa que extraiga los elementos de la diagonal principal de una matriz 
cuadrada.  """
import numpy as np 
matriz = np.array([ 
[10, 8, 3], 
[4, 22, 6], 
[7, 18, 99] 
]) 
print(matriz)

diagonal = []
for i in range(len(matriz)):
    diagonal.append(int(matriz[i][i]))

print("Los elementos de la diagonal son => ", diagonal)
