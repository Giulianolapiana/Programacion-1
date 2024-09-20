#Clase Cadena:
class Cadena:
    #Constructor:
    def __init__(self,cadena=""):
        self.cadena=cadena
    #Metodos de la clase:
    def calculartamano(self):
        print(f"El tamaño de la cadena es: {len(self.cadena)}")
    def contarVocales(self):
        cantidad_vocales=0
        cadena=self.cadena.lower()#Pasamos la cadena a minusculas para una comparacion más efectiva
        for letra in cadena:#Recorremos la cadena caracter por caracter.
            if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
                cantidad_vocales+=1#Incrementamos contador en caso de coincidir con una vocal

        print(f"La cantidad de vocales que tiene la frase o palabra es:{cantidad_vocales}")
#Creamos una instancia de la clase Cadena
frase=Cadena()
#creamos una variable llamada cadena y le asignamos un valor por teclado:
cadena=input("Ingrese una frase o palabra:")
#Accedemos al atributo cadena por el objeto creado y le damos un valor en este caso la cadena leida anteriormente
frase.cadena=cadena
#Llamar a metodos de la clase cadena:
#Mostramos el tamaño de la cadena:
frase.calculartamano()
#Mostramos la cantidad de vocales que tiene la cadena:
frase.contarVocales()
