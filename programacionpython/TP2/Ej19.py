class OperacionMatematica:
    def __init__(self,operacion,valor1,valor2):
        self.operacion=operacion
        self.valor1=float(valor1)
        self.valor2=float(valor2)
    def sumar_numeros(self):
        print(f"La suma de los números es de:{self.valor1+self.valor2}")
    
    def restar_numeros(self):
        print(f"La resta de los números es de:{self.valor1-self.valor2}")
    
    def multiplicar_numeros(self):
        print(f"La multiplicación de los numeros es de:{self.valor1*self.valor2}")
    def dividir_numeros(self):
        if self.valor2 != 0:
            print(f"La división de los números es de: {self.valor1 / self.valor2}")
        else:
            print("Error: División por cero")
    def aplicar_operacion(self):
        if(self.operacion=="+"):
            self.sumar_numeros()
        elif (self.operacion=="-"):
            self.restar_numeros()
        elif (self.operacion=="x"):
            self.multiplicar_numeros()
        elif (self.operacion=="/"):
            self.dividir_numeros()
        else:
            print("Operación invalida")

valor1=input("Ingrese el primer número:")
valor2=input("Ingrese el segundo número:")
opcion=input("Menú\n+)sumar\n-)restar\nx)Multiplicar\n/)dividir\n>")
operacion=OperacionMatematica(opcion,valor1,valor2)
operacion.aplicar_operacion()