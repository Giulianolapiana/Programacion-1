#Clase Cadena:
class Cadena:
    #Constructor:
    def __init__(self,cadena):
        self.cadena=cadena
    #Metodos de la clase:
    def calcular_tamano(self):
        return len(self.cadena)#se usa len para obtener la longitud y luego la retornamos

#Creamos una variable llamada cadena y le asignamos un valor:
cadena="La lluvia en Mendoza es escasa"
#Creamos una instancia de la clase Cadena y le pasamos por medio del constructor un valor para el atributo cadena
cadena=Cadena(cadena)
#Mostramos la longitud de la cadena con el metodo calcular_tamano por medio de el objeto creado(cadena)
print(f"El tamaño de la cadena es de:{cadena.calcular_tamano()}")