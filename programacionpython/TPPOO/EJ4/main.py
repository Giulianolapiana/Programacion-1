from entidad_computadora import Computadora
from entidad_componentes import ComponentesCPU

class CostoComputadora:
    def __init__(self):
        pass
    def main(self):
        marca = input("\nElija la marca de la computadora -> ")
        modelo  = input("Elija el modelo de la computadora -> ")
        computadora = Computadora(marca,modelo)
        total = 0
        #----
        while True:
            print("\nElija el tipo de componente que desea agregar a la computadora:")
            componente = input("componente a elegir -> ")
            marca = input("marca a elegir  -> ")
            cantidad = int(input("cantidad de componentes -> "))
            precio =  float(input("precio del componente -> "))
            cpu = ComponentesCPU(componente,marca,cantidad,precio)
            computadora.cargarComponentes(cpu)
            total += cpu.subtotal
            if input("quiere elegir otro componente? si/no -> ") == "no":
                break
        #imprimir
        computadora.imprimir(total)    


cc = CostoComputadora()
while True:
    cc.main()
    if input("quiere elegir otra computadora? si/no -> ") == "no":
        break