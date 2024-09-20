#Clase Cadena:
class Cadena:
    #Constructor:
    def __init__(self,cadena1="",cadena2=""):
        self.cadena1=cadena1
        self.cadena2=cadena2
    #Metodos de la clase:
    def comprobar_igualdad(self):
        print("Las cadenas ",end="")
        if(self.cadena1==self.cadena2):#Según el resultado de la expresion logica mostrar el mensaje correspondiente
            #True
            print("son iguales")
        else:
            #False
            print("no son iguales ")
#Creamos una instancia de la clase Cadena:
frase=Cadena()
#Creamos dos variables llamadas cadena1 y cadena2 y le damos un valor por teclado:
cadena1=input("Ingrese una palabra:")
cadena2=input("Ingrese otra palabra:")
#Accedemos a los atributos y les damos un valor
frase.cadena1=cadena1.lower()
frase.cadena2=cadena2.lower()
#llamamos al metodo comprobar igualdad por frase (objeto)
frase.comprobar_igualdad()
