#x = None 
#print(x)  

#Uso de None:
#Indicar ausencia de valor: Muestra que una variable no tiene valor asignado.
#Inicializar variables: Para comenzar con un valor "vacío" antes de asignar un valor real.
#Valor predeterminado en funciones: Para manejar casos donde no se pasa un argumento.



#Ejemplo:
def mostrar_mensaje(mensaje=None):
    if mensaje is None:
        print("No se proporcionó mensaje")
    else:
        print("Mensaje:", mensaje)

mostrar_mensaje()       # No muestra nada basicamente porque el parametro de la funcion toma por defecto el none
mostrar_mensaje("Hola") # En este caso muestra el Hola, superpone el valor por defecto ya que estamos pasando un argumento
