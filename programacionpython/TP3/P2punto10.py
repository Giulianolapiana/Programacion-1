""" Una matriz es simétrica si es igual a su transpuesta. Escribe un programa que verifique 
si una matriz es simétrica.  """

import numpy as np 
matriz = np.array([ 
[1, 0, 0], 
[0, 1, 0], 
[0, 0, 1] 
]) 
print(matriz)
#creamos la transpuesta y usamos numpy
transpuesta = np.array([[int(matriz[j][i]) for j in range(len(matriz))] for i in range(len(matriz[0]))])
#verificamos que todos los elementos coincidan
contador = 0
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if transpuesta [i][j] == matriz [i][j]:
            contador += 1
print(transpuesta)

if contador == (len(matriz)*len(matriz)):
    print("Es simetrica. ")

