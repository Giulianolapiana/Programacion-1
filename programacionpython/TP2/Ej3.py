#Metodos:
def evaluar_numero(numero):
    if(numero>=100 and numero<=999):
        return True
    else:
        return False

#Clase Digitos:
class Digitos:
    #Constructor:
    def __init__(self,numero):
        self.numero=numero
    #Metodos de la clase:
    def sumar_digitos(self):
        suma=0
        numero=self.numero
        while(numero>0):
            suma+=numero%10
            numero=int(numero/10)
        
        return suma


#Metodo Principal:
#Craar variable y leer un valor de tres cifras:
valor_tres_cifras=int(input("Ingrese un valor de 3 cifras:"))
#llamar a la funcion evaluar_numero y por medio de su resultado logico determinar la acción a ejecutar
#True:sumar digitos
#False:Mostrar mensaje de error
if(evaluar_numero(valor_tres_cifras)):
    #Creamos una Instancia de la clase digitos:
    digitos=Digitos(valor_tres_cifras)
    #Accedemos al metodo sumar_digitos por el objeto creado(digitos)
    print(f"La suma de los digitos es {digitos.sumar_digitos()}")
else:
    print("El valor ingresado no es de tres cifras")