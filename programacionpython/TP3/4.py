""" Escribe un programa que pida al usuario una lista de números y cuente cuántos de
ellos son pares y cuántos son impares. """

linkedList = list([5,2,8,5,1,9,10])
print(linkedList)

pares = [x for x in linkedList if x % 2 == 0]
print(pares) 
impares = [x for x in linkedList if x % 2 != 0]
print(impares) 