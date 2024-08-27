import math
numUsuario = input("Ingrese un numero y le diremos que criterios de visibilidad cumple ")
numUsuario = int(numUsuario)
num3 = 0
num5 = 0

""" divisible por 2"""
if (numUsuario % 2 == 0):
    print("el numero es divisible por 2")
"""divisible por 3"""
while(numUsuario != 0):
    num3 = numUsuario % 10 + num3
    numUsuario = int(numUsuario/10)
    
if (num3 % 3 == 0):
        print("el numero es divisible por 3")

"""divisible por 5"""

if(numUsuario % 10 == 5 or numUsuario % 10 == 0):
     print("El numero es divisible por 5")

