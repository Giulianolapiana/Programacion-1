#Clase Cadena:
class Cadena:
    #Constructor:
    def __init__(self,cadena1="",cadena2=""):
        self.cadena1=cadena1#Atributo 1 
        self.cadena2=cadena2#Atributo 2
    #Metodos de la cadena:
    def evaluar_contenido(self):
        if(self.cadena1.count(self.cadena2)>0):#Usamos .count para determinar si la cadena 2 se encuentra en la primera
            return True
        else:
            return False
#Creamos una instancia de la clase Cadena:
frase=Cadena()
#Creamos dos variables y le asignamos un valor por teclado
cadena1=input("Ingrese una cadena de caracteres:")
cadena2=input("Ingrese otra cadena:")
#Le damos un valor manualmente a cada uno de los atributos de Cadena
frase.cadena1=cadena1
frase.cadena2=cadena2
print("La segunda cadena ",end="")
if(frase.evaluar_contenido()):#según el retorno de el metodo evaluar_contenido mostramos el mensaje que corresponda
    print(" se encuentra dentro de la primera")
else:
    print(" no se encuentra dentro de la primera")