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
6. Salir

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

    # SALIR
    elif opcion == "6":

        print("Programa finalizado")
        break

    else:
        print("Opción inválida")

