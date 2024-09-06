""" pip install num2words  """

from num2words import num2words


class funcionesPrograma:
    def __init__(self,dia,mes,anio):
        self.dia = dia
        self.mes = mes
        self.anio = anio
    def getFechaString(dia,mes,anio):

        numeroPalabras1 = num2words(dia, lang='es')
        numeroPalabras2 = num2words(anio, lang='es')
        print(f"El número {dia} en palabras es: {numeroPalabras1}")
        print(f"El número {anio} en palabras es: {numeroPalabras2}")

dia = int(input("dia => "))
mes = int(input("mes => "))
anio = int(input("anio => "))
funcionesPrograma(dia,mes,anio)
funcionesPrograma.getFechaString(dia,mes,anio)
