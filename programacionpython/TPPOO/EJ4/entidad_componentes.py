class ComponentesCPU:
    def __init__(self, componente, marca, cantidad, precio):
        self.componente = componente
        self.marca = marca
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.componente} {self.marca} {self.cantidad} {self.precio}"