class Ingrediente:
    def __init__(self, nombre,cantidad,unidad_medida):
        self.nombre = nombre
        self.cantidad = cantidad
        self.unidad_medida = unidad_medida
    
    def  __str__(self):
        return f"Ingredientes/n Nombre: {self.nombre}, cantidad: {self.cantidad}, unidad de medida: {self.unidad_medida}"