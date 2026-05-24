class Biblioteca:

    def __init__(self):

        self.libros = {}
        self.miembros = {}

    def agregar_libro(self, libro):

        if libro.isbn in self.libros:
            print("Ya existe un libro con ese ISBN")

        else:
            self.libros[libro.isbn] = libro
            print("Libro agregado correctamente")

    def agregar_miembro(self, miembro):

        self.miembros[miembro.dni] = miembro
        print("Miembro agregado correctamente")

    def prestar_libro(self, isbn, dni):

        try:

            libro = self.libros[isbn]
            miembro = self.miembros[dni]

            if libro.disponible:

                libro.prestar(miembro)
                miembro.tomar_libro(libro)

                print("Libro prestado correctamente")

            else:
                print("Libro no disponible")

        except KeyError:
            print("Libro o miembro inexistente")

    def devolver_libro(self, isbn, dni):

        try:

            libro = self.libros[isbn]
            miembro = self.miembros[dni]

            libro.devolver()
            miembro.devolver_libro(libro)

            print("Libro devuelto correctamente")

        except KeyError:
            print("Error en devolución")

    def mostrar_estado(self):

        print("\n========== LIBROS ==========")

        for libro in self.libros.values():

            estado = "Disponible"

            if not libro.disponible:
                estado = f"Prestado a {libro.prestado_a.nombre}"

            print(f"""
Título: {libro.titulo}
Autor: {libro.autor}
ISBN: {libro.isbn}
Estado: {estado}
""")

        print("\n========== MIEMBROS ==========")

        for miembro in self.miembros.values():

            print(f"\nMiembro: {miembro.nombre}")

            if len(miembro.libros) == 0:

                print("No tiene libros prestados")

            else:

                print("Libros prestados:")

                for libro in miembro.libros:
                    print(f"- {libro.titulo}")