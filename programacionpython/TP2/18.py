""" #18- En la clase FuncionesPrograma codifique una método getFechaDate estática que
reciba como parámetro 3 valores enteros, día, mes, anio y retorne la fecha de tipo
date correspondiente.
En la clase Principal creada en el punto anterior haga uso de la función getFechaDate. """ 

class funcionesPrograma:
    def __init__(self,dia,mes,anio):
        self.dia = dia
        self.mes = mes
        self.anio = anio
    def getFechaString(dia,mes,anio):
        from num2words import num2words
        palabrasDia = num2words(dia, lang='es')
        palabraAnio = num2words(anio, lang='es')
        mesesLetras = {
            1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
        }
        if 1 <= mes <= 12:
            palabraMes = mesesLetras[mes]
        else:
            return "Número de mes inválido. Debe ser un número entre 1 y 12."
        
        print(f"El número en palabras es: {palabrasDia} de {palabraMes} del {palabraAnio}")
    
    def getFechaDate(dia,mes,anio):
        from datetime import date
        return date(anio, mes, dia)





dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
anio = int(input("Ingrese el año: "))

fecha = funcionesPrograma.getFechaDate(dia, mes, anio)
print(fecha)