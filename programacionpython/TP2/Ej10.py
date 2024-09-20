#Clase Cadena:
class Cadena:
    #Constructor:
    def __init__(self,cadena=""):
        self.cadena=cadena
    #Metodos de la clase:
    def convertir(self,opcion):
        if(opcion==1):
            return self.cadena.upper()#Convertimos a mayusculas
        else:
            return self.cadena.lower()#Convertimos a minusculas
#Creamos una instancia de la clase Cadena:
frase=Cadena()
#Creamos dos  variables llamadas cadena y opcion le asignamos un valor por teclado:
cadena=input("Ingrese una cadena:")
opcion=int(input("1)Pasar a mayusculas 2)pasar a minusculas:"))
#Accedemos al atributo cadena por el objeto creado y le damos un valor en este caso la cadena leida anteriormente
frase.cadena=cadena
#Procedemos a llamar al metodo convertir y pasamos como argumento el valor leido en opcion
print(f"Resultado:{frase.convertir(opcion)}")

