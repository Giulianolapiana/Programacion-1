class ComponentesCPU:
    def __init__(self, componente, marca, cantidad, precio):
        self.componente = componente
        self.marca = marca
        self.cantidad = cantidad
        self.precio = precio
        self.subtotal =  self.cantidad * self.precio


    def __str__(self):
        return f"Componente: {self.componente}, Marca: {self.marca}, Cantidad: {self.cantidad}, Precio: {self.precio}, Subtotal: {self.subtotal}"