""" Escribe un programa que gire una lista bidimensional (matriz) 90 grados en el sentido 
de las agujas del reloj.  """

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matriz original:")
for fila in matriz:
    print(fila)

n = len(matriz)  

for i in range(n):
    for j in range(i, n):
        matriz[i][j], matriz[j][i] = matriz[j][i], matriz[i][j]

for i in range(n):
    matriz[i].reverse()  

print("Matriz rotada:")
for fila in matriz:
    print(fila)