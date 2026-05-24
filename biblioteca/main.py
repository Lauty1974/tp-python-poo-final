from libro import Libro
from miembro import Miembro
from biblioteca import Biblioteca


biblioteca = Biblioteca()

while True:

    print("""
========== SISTEMA DE BIBLIOTECA ==========

1. Agregar libro
2. Agregar miembro
3. Prestar libro
4. Devolver libro
5. Mostrar estado
6. Excepciones técnicas
7. Salir

===========================================
""")

    opcion = input("Seleccione una opción: ")

    # AGREGAR LIBRO
    if opcion == "1":

        try:

            titulo = input("Ingrese título: ")
            autor = input("Ingrese autor: ")
            isbn = input("Ingrese ISBN: ")

            libro = Libro(titulo, autor, isbn)

            biblioteca.agregar_libro(libro)

        except ValueError as e:
            print("ValueError:", e)

        except TypeError as e:
            print("TypeError:", e)

    # AGREGAR MIEMBRO
    elif opcion == "2":

        try:

            nombre = input("Ingrese nombre: ")
            dni = input("Ingrese DNI: ")

            miembro = Miembro(nombre, dni)

            biblioteca.agregar_miembro(miembro)

        except ValueError as e:
            print("ValueError:", e)

        except TypeError as e:
            print("TypeError:", e)

    # PRESTAR LIBRO
    elif opcion == "3":

        isbn = input("Ingrese ISBN del libro: ")
        dni = input("Ingrese DNI del miembro: ")

        biblioteca.prestar_libro(isbn, dni)

    # DEVOLVER LIBRO
    elif opcion == "4":

        isbn = input("Ingrese ISBN del libro: ")
        dni = input("Ingrese DNI del miembro: ")

        biblioteca.devolver_libro(isbn, dni)

    # MOSTRAR ESTADO
    elif opcion == "5":

        biblioteca.mostrar_estado()

    # EXCEPCIONES TÉCNICAS
    elif opcion == "6":

        print("\n========== EXCEPCIONES TÉCNICAS ==========\n")

        # ATTRIBUTE ERROR
        try:

            libro = Libro("Python", "Juan", "111")
            print(libro.precio)

        except AttributeError as e:
            print("AttributeError:", e)

        # INDEX ERROR
        try:

            lista = [1]
            print(lista[10])

        except IndexError as e:
            print("IndexError:", e)

        # MODULE NOT FOUND ERROR
        try:

            __import__("modulo_falso")

        except ModuleNotFoundError as e:
            print("ModuleNotFoundError:", e)

    # SALIR
    elif opcion == "7":

        print("Programa finalizado")
        break

    else:
        print("Opción inválida")