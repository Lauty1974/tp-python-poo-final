class Curso:

    def __init__(self, nombre, codigo, profesor, capacidad):

        if capacidad <= 0:
            raise ValueError("La capacidad debe ser mayor a 0")

        self.nombre = nombre
        self.codigo = codigo
        self.profesor = profesor
        self.capacidad = capacidad
        self.estudiantes = []

    def hay_cupo(self):

        return len(self.estudiantes) < self.capacidad