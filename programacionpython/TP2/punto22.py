"""Suma los dígitos de un número ingresado por el usuario de forma recursiva.
Ejemplo: el usuario ingresa 1596
El programa debe sumar 1 + 5 + 9 + 6 """

def sumarN(x):
    if x == 0:
        return 0
    else:
        return x % 10 + sumarN(x//10)


numero = int(input("Ingrese un numero: "))
suma = sumarN(numero)
print(f"La suma de los numeros es: {suma}")
