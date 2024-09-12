class funcionesPrograma:
    #damos inicio y cargamos el parametro self
    def __init__(self,dia,mes,anio):
        self.dia = dia
        self.mes = mes
        self.anio = anio
    def getFechaString(self):
        from num2words import num2words
        palabrasDia = num2words(self.dia, lang='es')
        palabraAnio = num2words(self.anio, lang='es')
        mesesLetras = {
            1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
        }
        if 1 <= self.mes <= 12:
            palabraMes = mesesLetras[self.mes]
        else:
            return "Número de mes inválido. Debe ser un número entre 1 y 12."
        
        print(f"El número en palabras es: {palabrasDia} de {palabraMes} del {palabraAnio}")
    #funcion para poner la fecha, importamos la libreria date
    def getFechaDate(self):
        from datetime import date
        return date(self.anio, self.mes, self.dia)



dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
anio = int(input("Ingrese el año: "))

fecha = funcionesPrograma(dia, mes, anio)
print(fecha.getFechaDate())