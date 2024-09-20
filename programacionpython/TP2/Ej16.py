#Clase Cadena:
class Cadena:
    #Constructor:
    def __init__(self,cadena=""):
        self.cadena=cadena
    #Metodos de la clase:
    def comprobar_si_contiene_numeros(self):
        resultado=False
        for caracter in self.cadena:#vamos a evaluar caracter por caracter basicamente porque queremos saber si 
            #al menos hay un digito, y el is digit comprueba si todos son digitos (no nos sirve para la cadena completa)
            if caracter.isdigit():
                resultado=True
                break
        return resultado
#Creamos una instancia de la clase Cadena:
frase=Cadena()
#Creamos una variable llamada cadena y le asignamos un valor por teclado:
cadena=input("Ingrese una palabra o frase:")
#Accedemos al atributo cadena y le damos un valor (La cadena previamente leida)
frase.cadena=cadena
print("La cadena ",end="")
if frase.comprobar_si_contiene_numeros():
    print("Contiene números")
else:
    print("No contiene numeros")
