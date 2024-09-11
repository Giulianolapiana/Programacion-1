""" Cree una clase FuncionesPrograma y codifique una función estática getFechaString
que reciba como parámetro una fecha y retorne la fecha como una cadena literal.
Ejemplo recibo 15/10/1900, la salida debe ser
Quince de Octubre de mil novecientos.
Cree una clase Principal que contenga un método main y haga uso de la función
getFechaString. """

""" pip install num2words  """

from num2words import num2words


class funcionesPrograma:
    def __init__(self,dia,mes,anio):
        self.dia = dia
        self.mes = mes
        self.anio = anio
    def getFechaString(dia,mes,anio):

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


fecha = input("Ingrese la fecha (dd/mm/yyyy): ")

# Separar la fecha en día, mes y año
partes_fecha = fecha.split('/')
dia = int(partes_fecha[0])
mes = int(partes_fecha[1])
anio = int(partes_fecha[2])

print(dia,mes,anio)

funcionesPrograma.getFechaString(dia,mes,anio)
