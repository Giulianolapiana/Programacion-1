from entidad_plato import Plato
from entidad_ingrediente import Ingrediente

class MenuRestaurant:
    def __init__(self):
        self.platosMenu = []
    def main(self):
        while True:
            if input("Desea cargar un plato s/n: ") == "s":
                nombrePlato = str(input("Nombre del plato: "))
                precio = int(input("Precio plato: "))
                bebida = input("es bebida? s/n: ")
                plato = Plato(nombrePlato,precio,bebida)
                self.platosMenu.append(plato)
                if bebida == "n" or  bebida == "N":
                    while True:
                        nombre = input("ingrese  el nombre del ingrediente: ")
                        cantidad = int(input("ingrese la cantidad del ingrediente: "))
                        unidad_medida = input("ingrese la unidad de medida: ")
                        ingrediente = Ingrediente(nombre,cantidad,unidad_medida)
                        plato.cargarIngrediente(ingrediente)
                        if input("Desea agregar otro ingrediente s/n: ") == "n":
                            break
            else:
                #imprimir
                self.mostrar_menu()
                return
    
    def mostrar_menu(self):
        print("-----------MENÚ----------------")
        for plato in self.platosMenu:
            plato.imprimir()
    

mr =  MenuRestaurant()

mr.main()

