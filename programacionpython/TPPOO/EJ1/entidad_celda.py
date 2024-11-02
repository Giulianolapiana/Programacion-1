class Celda:
    def __init__(self, fila, columna, valor):
        self.fila = fila
        self.columna = columna
        self.valor = valor
    
    def __repr__(self):
        return f"Celda(fila={self.fila}, columna={self.columna}, valor='{self.valor}')"