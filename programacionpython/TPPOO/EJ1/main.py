from entidad_matriz import Matriz

m = Matriz()
valor = str()
while True:
    print("ingrese la poscion donde almacenar el valor ")
    valor = input("ingrese el valor que desea almacenar(o 'FIN' para terminar): ")
    if valor == "FIN":
        break
    fila = int(input("ingrese la posicion de la FILA: "))
    columna = int(input("ingrese la posicion de la COLUMNA: "))
    c = m.agrgarCelda(fila,columna,valor)
    print("--------------------------------")

m.mostrarCeldas()
print("ingrese la poscion donde buscar el VALOR ")
fila = int(input("posicion de la FILA: "))
columna = int(input("posicion de la COLUMNA: "))
s = m.retornarValor(fila,columna)
print(s)

