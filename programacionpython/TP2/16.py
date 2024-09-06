frase = input("escruba una frase => ")
lista = list(frase)
print(lista)
for i in range(len(lista)):
    if lista[i] in ("1","2","3","4","5","6","7","8","9"):
        print("Esta lista contiene numeros")
        break
