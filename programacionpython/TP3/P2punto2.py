"""Escribe un programa que calcule la suma de todos los elementos en una lista
bidimensional.
Pista: Aplique la función sum"""

def laMatriz(filas2,columnas2):
    matriz = []
    for f in range(filas2):
        fila = []
        for c in range(columnas2):
            fila.append(int(input(f"ingrese el valor para la posicion [{f}][{c}]")))
            
        matriz.append(fila)
    return matriz
def sumar_valores(matriz):
    lista_a_sumar = [numero for fila in matriz for numero in fila]
    total = sum(lista_a_sumar)
    return total    
    
filas = (int(input("ingrese la cantidad de filas de la matriz: ")))
columnas = int(input("Ingrese la cantidad de columnas de la matriz: "))

matriz = laMatriz(filas, columnas)
for i in matriz:
    print(i)

suma = sumar_valores(matriz)    
print(f"La suma de los valores es: {suma}")