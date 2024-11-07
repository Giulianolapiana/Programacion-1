class Plato:
    def __init__(self,nombrePlato,precio,esBebida):
        self.nombrePlato = nombrePlato
        self.precio = precio
        self.esBebida = esBebida
        self.lista_ingredientes = []
        
    def cargarIngrediente(self,ingrediente):
        self.lista_ingredientes.append(ingrediente)


    def imprimir(self):
        print(f"{self.nombrePlato}")
        print(f"Precio $ {self.precio}")
        for ing in  self.lista_ingredientes:
            print(ing)
        print("----------------------------------")


