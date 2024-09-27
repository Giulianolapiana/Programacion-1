"""Ejercicio 9: Lista de Números Primos
Escribe un programa que permita al usuario ingresar una lista de números y filtre los
números primos.
Pista:
 Usa una función para verificar si un número es primo.
"""
def es_primo(num):
    if num <= 1:
        return False
    for x in range(2, int(num**0.5) + 1):
        if num % x == 0:
            return False
    return True

def encontrar_primos(arreglo):
    primos = []
    for num in arreglo:
        if es_primo(num):
            primos.append(num)
    return primos

arreglo = []
dimen = int(input("Ingrese la dimension del arreglo: "))

for i in range(dimen):
    arreglo.append(int(input(f"Ingrese un valor para la posicion [{i}]: ")))

primos = encontrar_primos(arreglo)

print(f"De los numeros ingresados: {arreglo}, estos numeros son primos: {primos}")