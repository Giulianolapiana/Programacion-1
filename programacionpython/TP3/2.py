""" Escribe un programa que pida al usuario una lista de números y encuentre el mayor y
el menor de ellos. """

class listas:
    def __init__(self, linkedList):
        self.linkedList = linkedList
    

    def sumaList(linkedList):
        suma = 0
        for i in range(len(linkedList)):
            suma = linkedList[i] + suma
        return suma


linkedList = list([5,2,8,5,1,9,10])
print(linkedList)

suma = listas.sumaList(linkedList)
print(sum(linkedList))
print(max(linkedList))
print(min(linkedList))