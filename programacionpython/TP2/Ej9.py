#Clase Cadena:
class Cadena:
    #Constructor:
    def __init__(self,cadena=""):
        self.cadena=cadena
    #Metodos de la clase:
    def transformar_a_ascci(self):
        for letra in self.cadena:
            print(f"{letra}:{ord(letra)}  ",end="")#hacemos uso del ord para mostrar el codigo assci de cada caracter
#Creamos una instancia de cadena:
frase= Cadena()
#Creamos una variable llamada cadena y le asignamos un valor por teclado:
cadena=input("Ingrese una cadena:")
#Accedemos al atributo cadena por el objeto creado y le damos un valor en este caso la cadena leida anteriormente
frase.cadena=cadena
#Llamamos al metodo transformar_a_ascci por el objeto (frase):
frase.transformar_a_ascci()