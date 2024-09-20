#Clase Cajero:
class Cajero:
    #Constructor:
    def __init__(self,monto=0):
        self.monto=monto
    #Metodos de la clase:
    def contar_billetes(self,billete):
        cantidad_de_billetes=0
        while(self.monto>=billete):
            self.monto-=billete
            cantidad_de_billetes+=1

        return cantidad_de_billetes
    def contar_monedas(self,moneda):
        cantidad_de_monedas=0
        while(self.monto>=moneda):
            self.monto-=moneda
            cantidad_de_monedas+=1
        return cantidad_de_monedas
    
    def mostrar_informacion(self,billetes_disponibles):
        print("--Cantidad de billetes de--")
        for valor in billetes_disponibles:
            if(valor>=1):
                print(f"{valor}:{self.contar_billetes(valor)} billetes")
            else:
                print(f"{valor}:{self.contar_monedas(valor)} monedas")
        print(f"Sobran:{self.monto}")
#Metodo Principal:
#Creamos una instancia de la clase Cajero:
cajero= Cajero()

#Creamos un arreglo con los billetes y monedas(solo es para facilitar mostrar posteriormente en pantalla)
billetes_disponibles=[200,100,50,20,10,5,2,1,0.50,0.25,0.10,0.05]

#leemos un monto de dinero y los parseamos a float para permitir decimales:
monto=float(input("Ingrese la cantidad de dinero que desea contar:"))

#Le asignamos un valor a nuestro atributo monto por medio de nuestro objeto creado:

cajero.monto=monto

#Llamamos al metodo mostrar_información de la clase Cajero con cajero(Objeto) 

cajero.mostrar_informacion(billetes_disponibles)#Pasamos por parametro el arreglo billetes_disponibles

