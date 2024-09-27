""" Escribe un programa que encuentre el valor más grande en una lista bidimensional. """

import numpy as np 
matriz = np.array([ 
[10, 8, 3], 
[4, 22, 6], 
[7, 18, 99] 
]) 
print(matriz)

#funcion np.max para encontrar el maximo
print(np.max(matriz))