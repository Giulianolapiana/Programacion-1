matriz = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]
for i in range (len(matriz)):
    for j in range(len(matriz)):
            if (j == ((len(matriz)-1)-i)):
                  print(len(matriz))
                  matriz[i][j] = 1
            else: matriz[i][j] = 0
    print(matriz[i])

