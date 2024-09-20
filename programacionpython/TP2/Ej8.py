#CLase Cadena:
class Cadena:
    #Constructor:
    def __init__(self,cadena=""):
        self.cadena=cadena
    #Metodos de la clase:
    def remover_a_por_e(self):
        resultado=""#Creamos una variable local en donde vamos a guardar la nueva cadena
        for letra in self.cadena.lower():#Recorremos la cadena caracter por caracter
            if(letra=="a"):#En caso de ser a:
                resultado+="e"#a resultado se le asigna su valor y suma una e (True)
            else:
                resultado+=letra#a resultado se le asigna su valor y suma la letra que estabamos evaluando (False)

        return resultado
#Creamos una instancia de la clase Cadena:
frase= Cadena()
#Creamos una variable llamada cadena y le asignamos un valor por teclado:
cadena=input("Ingrese un frase o palabra:")
#Accedemos al atributo cadena por el objeto creado y le damos un valor en este caso la cadena leida anteriormente
frase.cadena=cadena
#Llamamos al metodo remover_a_por_e con el objeto (frase)  y mostramos el resultado 
print("Se cambiaron las a por e / Resultado:"+frase.remover_a_por_e())