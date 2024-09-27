"""Ejercicio 8: Encontrar Elementos Repetidos
Escribe un programa que identifique y muestre los elementos que se repiten en una
lista.
Pista:
 Utiliza un diccionario o un conjunto (set) para hacer el seguimiento de los
elementos."""
def devolver_repetidos(arreglo):
    vistos = set()
    repetido = set()
    
    for i in arreglo:
        if i in vistos:
            repetido.add(i)
        else:
            vistos.add(i)
    return list(repetido)
    
arreglo = []    
dimen = int(input("Ingrese la dimension del arreglo: "))

for i in range(dimen):
    arreglo.append(int(input(f"Ingrese un valor para la posicion [{i}]")))
    
repetidos = devolver_repetidos(arreglo)
print(f"Los elemenos repetidos son: {repetidos}")