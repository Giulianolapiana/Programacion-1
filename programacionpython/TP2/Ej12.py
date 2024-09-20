#Clase Cadena:
class Cadena:
    #Contructor:
    def __init__(self,cadena=""):
        self.cadena=cadena
    #Metodos de la clase:
    def extraer_letras(self):
        return self.cadena[3:5]#Hacemos uso del slicing para extraer las porcion de caracteres que necesitamos(subcadena)
#Creamos una instancia de Cadena y mediante el contructor mismo pasamos una valor al atributo cadena
frase=Cadena("hipopotamo")
#Llamamos a extraer_letras por el objeto creado(frase)
print(f"La cuarta y quinta letra son:{frase.extraer_letras()}")