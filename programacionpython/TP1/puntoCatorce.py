from random import *
numRandom = randint(0, 100)
print(numRandom)
numUsuario = input("Ingrese un numero del 0 al 100 ")
numUsuario = int(numUsuario)
intentos = 1
while (numUsuario>100 or numUsuario<0):
    numUsuario = input("ingrese un numero dentro de 0 y 100 ")
    numUsuario = int(numUsuario)
   

while (numUsuario != numRandom):
    if(numUsuario > numRandom):
        print("El numero ingresado es mayor al numero aleatorio ")
    elif (numUsuario < numRandom):
        print("El numero ingresado es menor al numero aleaorio ")
    else:
        print("El numero esta fuera de rango ")
    
    intentos += 1
    numUsuario = input("Ingrese un numero nuevo: ")
    numUsuario = int(numUsuario)
    
print(f"Acertaste el numero con {intentos} intentos ")