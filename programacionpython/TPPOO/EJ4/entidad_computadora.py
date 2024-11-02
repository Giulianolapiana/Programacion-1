class Computadora:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.lista_componentes = [] 
    def agregar_componentes(self, ingrediente):
        if not self.es_bebida:
            self.ingredientes.append(ingrediente)

    def imprimir(self):
        print(f"marca: {self.marca}")
        print(f"modelo: {self.modelo}")
        if self.ingredientes:
            print("Ingredientes:")
            for ingrediente in self.ingredientes:
                print(ingrediente)
        print("----------------------------------")
