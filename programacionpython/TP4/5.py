numeros = (1, 2, 2, 3, 4, 4, 4, 5)
#Cuenta cuántas veces aparece el número 4 en la tupla.
cont = 0
for i in numeros:
    if i == 4:
        cont += 1

print(cont)