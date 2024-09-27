""" Escribe un programa que multiplique cada elemento de una lista de números por un
valor ingresado por el usuario. """

linkedList = list([5,2,8,5,1,9,10])
print(linkedList)
n = int(2)

mult = [i*n for i in linkedList]
print(mult)  