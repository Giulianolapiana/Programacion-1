class Computadora:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.lista_componentes = [] 
    
    def cargarComponentes(self,cpu):
        self.lista_componentes.append(cpu)

    def imprimir(self,total):
        print("\n -------------------------------")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        for comp in  self.lista_componentes:
            print(comp)
        print("El total es de: ",total)
        if total > 50000:
            total = (total * 0.4) + total
        else:
            total = (total * 0.3) + total
        print("El precio sugerido de venta es: ", total)
        print("----------------------------------")