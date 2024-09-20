"""Codifique un programa que solicite un número entero mayor a cero y que
mediante recursión sume todos los números números naturales desde el número
ingresado hasta 1. """
def sumar_num(x):
    if x == 1:
        return 1
    else:
        return x + sumar_num(x - 1)


numero = int(input("Ingrese hasta que numero quiere sumar: "))
mostrar_num = sumar_num(numero) 

print(f"La suma de los numeros es: {mostrar_num}")
