
def laMatriz(filas2, columnas2):
    matriz = []
    for f in range(filas2):
        fila = []
        for c in range(columnas2):
            fila.append(int(input(f"ingrese el valor para la posición [{f}][{c}]: ")))
        matriz.append(fila)
    return matriz

def sumar_filas(matriz):
    for i, fila in enumerate(matriz):
        suma_fila = sum(fila)
        print(f"La suma de los valores de la fila {i+1} es: {suma_fila}")

def sumar_valores(matriz):
    lista_a_sumar = [numero for fila in matriz for numero in fila]
    total = sum(lista_a_sumar)
    return total

filas = int(input("Ingrese la cantidad de filas de la matriz: "))
columnas = int(input("Ingrese la cantidad de columnas de la matriz: "))

matriz = laMatriz(filas, columnas)

for fila in matriz:
    print(fila)


suma = sumar_valores(matriz)
print(f"\nLa suma de todos los valores es: {suma}")

sumar_filas(matriz)

