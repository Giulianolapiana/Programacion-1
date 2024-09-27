""" Escribe un programa que permita al usuario ingresar una lista de números y filtre los
números primos """

linkedList = list([6,8,7,6,1,2,3,5,25,7,9,33,21,21,7])
print(linkedList)
cont = {}

def numPrimo(linkedList):
    linkedList = set(linkedList)
    for i in linkedList:
        cont[i] = 0
        for j in range(1,(i+1)):
            if ((i)%(j)) == 0:
                cont[i] += 1  
        if cont[i] == 2:
            print("es primo ",i)     
    print(cont)

numPrimo(linkedList)
""" primos = [i for i in linkedList if i % 2 == 0]
print(pares)  """