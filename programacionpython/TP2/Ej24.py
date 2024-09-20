#Clase Recursividad:
class Recursividad:
    @staticmethod
    def recorrer_cadena(cadena,indice=0):
        #Caso base:
        if indice==len(cadena):
            #Salida no recursiva:
            return 
        else:
            #Salida recursiva:
            print(cadena[indice])
            Recursividad.recorrer_cadena(cadena,indice+1)
#Creamos una variable llamada cadena y le asignamos un valor por teclado:
cadena=input("Ingrese una palabra o frase:")
#accedemos al metodo recorrer_cadena mediante la clase a la que esta asosiado
Recursividad.recorrer_cadena(cadena)