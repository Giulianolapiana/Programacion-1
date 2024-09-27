"""Ejercicio 1: Crear una Matriz de Números
Crea una función que reciba dos parámetros: el número de filas y columnas. La función
debe generar una matriz de ese tamaño, donde los valores son números enteros
consecutivos empezando desde 1."""
def return_matriz(fila, columna):
    matriz = []
    cont = 1
    for f in range(filas):
        fila = []
        for c in range(columnas):
            fila.append(cont)
            cont+=1
        matriz.append(fila)
        
    return matriz

filas = int(input("Ingrese la cantidad de filas de la matriz: "))    
columnas = int(input("Ingrese la cantidad de columnas de la matriz: "))

matriz = return_matriz(filas,columnas)

for i in matriz:
    print(i)