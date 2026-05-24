class Libro:

    def __init__(self, titulo, autor, isbn):

        if titulo.isdigit():
            raise TypeError("El título no puede ser numérico")

        if not isinstance(autor, str):
            raise TypeError("El autor debe ser texto")

        if isbn == "":
            raise ValueError("El ISBN no puede estar vacío")

        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True
        self.prestado_a = None

    def prestar(self, miembro):

        if self.disponible:

            self.disponible = False
            self.prestado_a = miembro

        else:
            print("El libro ya está prestado")

    def devolver(self):

        self.disponible = True
        self.prestado_a = None