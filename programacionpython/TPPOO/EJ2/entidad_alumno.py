class Alumno:
    def __init__(self,nombre,legajo):
        self.nombre = nombre
        self.legajo = legajo
        self.listaNotas = []

    def __repr__(self):
        return f"Alumno(nombre= {self.nombre}, legajo= {self.legajo}, notas= {self.listaNotas})"