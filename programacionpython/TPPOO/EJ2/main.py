from entidad_alumno import Alumno
from entidad_nota import Nota
""" El algoritmo debe permitir cargar N cantidad de alumnos y para cada alumno N cantidad
de Notas. Al finalizar la carga de los alumnos y sus notas mostrar la información cargada y
para cada alumno mostrar el promedio de las notas que posee. Valide que se ingrese al
menos 1 nota. Agregue en la clase Alumno un método que calcule el promedio de las
notas que posee."""

class CargarNotas:
    def __init__(self):
        self.listaAlumnos = []
    
    def cargarAlumnos(self):
        alumno = input("ingrese el NOMBRE del alumno: ")
        legajo = int(input("ingrese el LEGAJO: "))
        nuevaLista = Alumno(alumno,legajo)
        self.listaAlumnos.append(nuevaLista)
        #cargar las notas de los alumnos
        while True:
            s = input("Desea cargar una nota SI/NO: \n")
            if s == "NO" or s == "no" and len(nuevaLista.listaNotas) >= 1:
                break
            else:
                catedra = input("ingrese la catedra: ")
                nuevaLista.listaNotas.append([catedra,int(input("Ingrese la nota a cargar: "))])
        
    def imprimir(self):
        print("----------------------------------------------------------------")
        for fila in self.listaAlumnos:
            print(f"Nombre Completo: {fila.nombre} -> Legajo: {fila.legajo}")


cn = CargarNotas()
while True:
    s = input("Desea cargar un alumno SI/NO: \n")
    if s == "NO" or s == "no":
        break
    else:
        h = cn.cargarAlumnos()

cn.imprimir()
