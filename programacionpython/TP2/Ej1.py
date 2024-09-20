#Clase Casteo:
class Casteo:
    #Constructor:
    def __init__(self,valor_decimal):
        self.valor_decimal=valor_decimal
    #Metodos de la clase:
    def convertir_a_float(self):
        return float(self.valor_decimal)
    def convertir_a_int(self):
        return int(self.valor_decimal)
    def convertir_a_short(self):
        # Rango de un short: -32,768 a 32,767
        if -32768 <= self.valor_decimal <= 32767:
            return int(self.valor_decimal) 
        elif self.valor_decimal < -32768:
            return -32768
        else:  # self.valor_decimal > 32767
            return 32767
    def convertir_a_long(self):
        # En Python 3, simplemente convertir a int para manejar enteros grandes
        return int(self.valor_decimal)
#Metodo Principal:
valor_decimal=0  
#Creamos una variable y guardamos un dato de tipo float:
valor_decimal=float(input("Ingrese un valor decimal:"))
#Creamos una instancia de la clase Casteo:
castear=Casteo(valor_decimal)
#Por medio de sus metodos convertimos a los datos int,float,short,long:
print(f"En entero:{castear.convertir_a_int()}")
print(f"En float:{castear.convertir_a_float()}")
print(f"En short:{castear.convertir_a_short()}")
print(f"En long:{castear.convertir_a_long}")