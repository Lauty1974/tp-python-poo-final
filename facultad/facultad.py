class Facultad:

    def __init__(self):

        self.estudiantes = {}
        self.cursos = {}

    def agregar_estudiante(self, estudiante):

        self.estudiantes[estudiante.matricula] = estudiante
        print("Estudiante agregado correctamente")

    def agregar_curso(self, curso):

        self.cursos[curso.codigo] = curso
        print("Curso agregado correctamente")

    def inscribir(self, matricula, codigo):

        try:

            estudiante = self.estudiantes[matricula]
            curso = self.cursos[codigo]

            if curso.hay_cupo():

                curso.estudiantes.append(estudiante)
                estudiante.inscribirse(curso)

                print("Inscripción realizada correctamente")

            else:
                print("No hay cupos disponibles")

        except KeyError:
            print("Curso o estudiante inexistente")

    def baja(self, matricula, codigo):

        try:

            estudiante = self.estudiantes[matricula]
            curso = self.cursos[codigo]

            curso.estudiantes.remove(estudiante)
            estudiante.baja_curso(curso)

            print("Baja realizada correctamente")

        except KeyError:
            print("Error en la baja")

    def mostrar_estado(self):

        print("\n========== CURSOS ==========")

        for curso in self.cursos.values():

            cupos = curso.capacidad - len(curso.estudiantes)

            print(f"""
Curso: {curso.nombre}
Código: {curso.codigo}
Profesor: {curso.profesor}
Cupos disponibles: {cupos}
""")

        print("\n========== ESTUDIANTES ==========")

        for estudiante in self.estudiantes.values():

            print(f"\nEstudiante: {estudiante.nombre} {estudiante.apellido}")
            print(f"Carrera: {estudiante.carrera}")

            if len(estudiante.cursos) == 0:

                print("No está inscripto en cursos")

            else:

                print("Cursos inscriptos:")

                for curso in estudiante.cursos:
                    print(f"- {curso.nombre}")