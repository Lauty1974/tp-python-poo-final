class Miembro:

    def __init__(self, nombre, dni):

        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser texto")

        if not dni.isdigit():
            raise ValueError("El DNI debe ser numérico")

        self.nombre = nombre
        self.dni = dni
        self.libros = []

    def tomar_libro(self, libro):

        self.libros.append(libro)

    def devolver_libro(self, libro):

        self.libros.remove(libro)