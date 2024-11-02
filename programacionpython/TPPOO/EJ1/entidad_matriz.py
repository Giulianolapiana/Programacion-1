from entidad_celda import Celda

class Matriz:
    def __init__(self):
        self.celdasMatriz = []

    def agrgarCelda(self, fila, columna, valor):
        for celda in self.celdasMatriz:
            if celda.fila == fila and celda.columna == columna:
                print("La celda ya existe en esa posición.")
                return 
        nuevaCelda = Celda(fila, columna, valor)
        self.celdasMatriz.append(nuevaCelda)

    def mostrarCeldas(self):
        print("----------------------------------------------------------------")
        for celda in self.celdasMatriz:
            print(f"Fila: {celda.fila}, Columna: {celda.columna}, Valor: {celda.valor}")

    def retornarValor(self, fila, columna):
        for celda in self.celdasMatriz:
            if celda.fila == fila and celda.columna == columna:
                return celda.valor
        return ("La fila y columna indicada no ha sido asignada en ninguna celda")