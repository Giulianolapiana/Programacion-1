def transponer(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    
    matriz_transpuesta = []
    for i in range(columnas):
        nueva_fila = []
        for j in range(filas):
            nueva_fila.append(matriz[j][i])
        matriz_transpuesta.append(nueva_fila)
    
    return matriz_transpuesta

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz_t = transponer(matriz)

print("Matriz transpuesta:")
for fila in matriz_t:
    print(fila)