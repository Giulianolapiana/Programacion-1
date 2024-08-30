import math
numUsuario = input("Ingrese un numero y le diremos que criterios de divisibilidad cumple -> ")
numUsuario = int(numUsuario)
num3 = 0
num5 = 0
num9 = 9

""" divisible por 2"""
if (numUsuario % 2 == 0):
    print("el numero es divisible por 2")

"""divisible por 3"""
numUsuario2 = numUsuario
while(numUsuario2 != 0):
    num3 = numUsuario2 % 10 + num3
    numUsuario2 = int(numUsuario2/10)
    
if (num3 % 3 == 0):
        print("el numero es divisible por 3")

"""divisible por 5"""

if(numUsuario % 10 == 5 or numUsuario % 10 == 0):
    print("El numero es divisible por 5") 

""" divisible por 9 """
numUsuario3 = numUsuario
while(numUsuario3 != 0):
    num9 = numUsuario3 % 10 + num9
    numUsuario3 = int(numUsuario3/10)
    
if (num9 % 9 == 0):
    print("el numero es divisible por 9")


""" divisible por 10 """

if(numUsuario % 10 == 0):
    print("El numero es divisible por 10")
