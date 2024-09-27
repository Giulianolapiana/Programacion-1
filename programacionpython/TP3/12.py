""" Escribe un programa que sume dos listas de números elemento por elemento. Las
listas deben tener la misma longitud. """

def addList(linkedList,n):
    for i in range(n):
        linkedList.append(int(input()))

def sumaListas(lista_1,lista_2):
    resultado = []
    for i in range(len(lista_2)):
        resultado.append(lista_1[i]+lista_2[i])
    return resultado    


n = int(input("Elija la longitud de las dos listas => "))
print("ingrese la primera lista => ")
lista_1 = []
addList(lista_1,n)
print("ingrese la segunda lista => ")
lista_2 = []
addList(lista_2,n)
print(lista_2)
print(lista_1)

resultado = sumaListas(lista_1,lista_2)
print(resultado)
