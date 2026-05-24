from estudiante import Estudiante
from curso import Curso
from facultad import Facultad


facultad = Facultad()

while True:

    print("""
========== SISTEMA DE FACULTAD ==========

1. Agregar estudiante
2. Agregar curso
3. Inscribir estudiante
4. Dar de baja estudiante
5. Mostrar estado
6. Excepciones técnicas
7. Salir

=========================================
""")

    opcion = input("Seleccione una opción: ")

    # AGREGAR ESTUDIANTE
    if opcion == "1":

        try:

            nombre = input("Ingrese nombre: ")
            apellido = input("Ingrese apellido: ")
            matricula = input("Ingrese matrícula: ")
            carrera = input("Ingrese carrera: ")

            estudiante = Estudiante(
                nombre,
                apellido,
                matricula,
                carrera
            )

            facultad.agregar_estudiante(estudiante)

        except ValueError as e:
            print("ValueError:", e)

        except TypeError as e:
            print("TypeError:", e)

    # AGREGAR CURSO
    elif opcion == "2":

        try:

            nombre = input("Ingrese nombre del curso: ")
            codigo = input("Ingrese código del curso: ")
            profesor = input("Ingrese profesor: ")
            capacidad = int(input("Ingrese capacidad: "))

            curso = Curso(
                nombre,
                codigo,
                profesor,
                capacidad
            )

            facultad.agregar_curso(curso)

        except ValueError as e:
            print("ValueError:", e)

    # INSCRIBIR ESTUDIANTE
    elif opcion == "3":

        matricula = input("Ingrese matrícula del estudiante: ")
        codigo = input("Ingrese código del curso: ")

        facultad.inscribir(matricula, codigo)

    # DAR DE BAJA
    elif opcion == "4":

        matricula = input("Ingrese matrícula del estudiante: ")
        codigo = input("Ingrese código del curso: ")

        facultad.baja(matricula, codigo)

    # MOSTRAR ESTADO
    elif opcion == "5":

        facultad.mostrar_estado()

    # EXCEPCIONES TÉCNICAS
    elif opcion == "6":

        print("\n========== EXCEPCIONES TÉCNICAS ==========\n")

        # ATTRIBUTE ERROR
        try:

            estudiante = Estudiante("Juan", "Perez", "100", "Sistemas")
            print(estudiante.promedio)

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