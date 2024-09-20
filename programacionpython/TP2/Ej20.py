class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
        # Validación simple para evitar denominadores cero
        if self.denominador == 0:
            self.denominador = 1  # Asignar un denominador por defecto si es cero
        # Si el denominador es negativo, cambiar el signo al numerador
        if self.denominador < 0:
            self.numerador *= -1
            self.denominador *= -1
    
    def __str__(self):
        return f"{self.numerador}/{self.denominador}"
    
    @staticmethod
    def sumarFracciones(f1, f2):
        numerador = f1.numerador * f2.denominador + f2.numerador * f1.denominador
        denominador = f1.denominador * f2.denominador
        return Fraccion(numerador, denominador)

    @staticmethod
    def restarFracciones(f1, f2):
        numerador = f1.numerador * f2.denominador - f2.numerador * f1.denominador
        denominador = f1.denominador * f2.denominador
        return Fraccion(numerador, denominador)

    @staticmethod
    def multiplicarFracciones(f1, f2):
        numerador = f1.numerador * f2.numerador
        denominador = f1.denominador * f2.denominador
        return Fraccion(numerador, denominador)

    @staticmethod
    def dividirFracciones(f1, f2):
        if f2.numerador == 0:
            return Fraccion(0, 1)  # Retornar una fracción "0/1" en lugar de dividir por cero
        numerador = f1.numerador * f2.denominador
        denominador = f1.denominador * f2.numerador
        return Fraccion(numerador, denominador)

f1 = Fraccion(1, 2)
f2 = Fraccion(1, 3)

suma = Fraccion.sumarFracciones(f1, f2)
resta = Fraccion.restarFracciones(f1, f2)
multiplicacion = Fraccion.multiplicarFracciones(f1, f2)
division = Fraccion.dividirFracciones(f1, f2)

print("Suma:", suma)  
print("Resta:", resta)      
print("Multiplicación:", multiplicacion) 
print("División:", division) 
