class Estudiante:

    def __init__(self, nombre, apellido, matricula, carrera):

        if nombre.isdigit():
            raise TypeError("El nombre no puede ser numérico")

        if matricula == "":
            raise ValueError("La matrícula no puede estar vacía")

        self.nombre = nombre
        self.apellido = apellido
        self.matricula = matricula
        self.carrera = carrera
        self.cursos = []

    def inscribirse(self, curso):

        self.cursos.append(curso)

    def baja_curso(self, curso):

        self.cursos.remove(curso)