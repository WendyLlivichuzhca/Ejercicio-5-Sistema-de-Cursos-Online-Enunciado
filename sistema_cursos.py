"""
Ejercicio 5: Sistema de Cursos Online
Integrantes: Erick Chacón, Kenny Valdieiso, Wendy Llivichuzhca, Freddy Gomez
Descripcion:
Sistema para administrar instructores, estudiantes y cursos
en una plataforma educativa usando clases, listas, metodos
y manejo de excepciones.
"""

class Instructor:
    def __init__(self, nombre, especialidad):
        if not nombre.strip():
            raise ValueError("El nombre del instructor no puede estar vacio.")
        if not especialidad.strip():
            raise ValueError("La especialidad no puede estar vacia.")

        self.nombre = nombre.strip()
        self.especialidad = especialidad.strip()

    def __str__(self):
        return f"{self.nombre} - Especialidad: {self.especialidad}"


class Estudiante:
    def __init__(self, nombre, edad):
        if not nombre.strip():
            raise ValueError("El nombre del estudiante no puede estar vacio.")

        if isinstance(edad, str):
            edad = edad.strip()
            if not edad:
                raise ValueError("La edad no puede estar vacia.")
            edad = int(edad)

        if edad <= 0:
            raise ValueError("La edad debe ser mayor que cero.")

        self.nombre = nombre.strip()
        self.edad = edad

    def mostrar_estudiante(self):
        return f"Nombre: {self.nombre} | Edad: {self.edad}"

    def __str__(self):
        return self.mostrar_estudiante()


class Curso:
    def __init__(self, nombre, instructor):
        if not nombre.strip():
            raise ValueError("El nombre del curso no puede estar vacio.")
        if not isinstance(instructor, Instructor):
            raise TypeError("Debe asignarse un instructor valido al curso.")

        self.nombre = nombre.strip()
        self.instructor = instructor
        self.estudiantes = []

    def __str__(self):
        return f"{self.nombre} - Instructor: {self.instructor.nombre}"

    def inscribir_estudiante(self, estudiante):
        if not isinstance(estudiante, Estudiante):
            raise TypeError("Solo se pueden inscribir objetos de tipo Estudiante.")

        for inscrito in self.estudiantes:
            if inscrito.nombre.lower() == estudiante.nombre.lower():
                raise ValueError("El estudiante ya esta inscrito en este curso.")

        self.estudiantes.append(estudiante)

    def mostrar_detalle(self):
        detalle = [
            f"Curso: {self.nombre}",
            f"Instructor: {self.instructor.nombre} ({self.instructor.especialidad})",
        ]

        if self.estudiantes:
            detalle.append("Estudiantes inscritos:")
            for estudiante in self.estudiantes:
                detalle.append(f"  - {estudiante.mostrar_estudiante()}")
        else:
            detalle.append("Estudiantes inscritos: Ninguno")

        return "\n".join(detalle)


def pedir_texto(mensaje):
    texto = input(mensaje).strip()
    if not texto:
        raise ValueError("Este campo no puede estar vacio.")
    return texto


def pedir_entero(mensaje):
    valor = input(mensaje).strip()
    if not valor:
        raise ValueError("Debe ingresar un numero.")
    return int(valor)


def mostrar_menu():
    print("\n--- SISTEMA DE CURSOS ONLINE ---")
    print("1. Registrar instructor")
    print("2. Registrar estudiante")
    print("3. Crear curso")
    print("4. Inscribir estudiante en curso")
    print("5. Mostrar cursos y estudiantes inscritos")
    print("6. Salir")


def seleccionar_elemento(lista, tipo):
    if not lista:
        raise ValueError(f"No hay {tipo}s registrados.")

    for i, elemento in enumerate(lista, start=1):
        print(f"{i}. {elemento}")

    indice = pedir_entero(f"Seleccione un {tipo} por numero: ")
    if indice < 1 or indice > len(lista):
        raise IndexError(f"Debe escoger un numero entre 1 y {len(lista)}.")

    return lista[indice - 1]


def main():
    instructores = []
    estudiantes = []
    cursos = []

    while True:
        try:
            mostrar_menu()
            opcion = pedir_entero("Ingrese una opcion: ")

            if opcion == 1:
                nombre = pedir_texto("Nombre del instructor: ")
                especialidad = pedir_texto("Especialidad del instructor: ")
                instructor = Instructor(nombre, especialidad)
                instructores.append(instructor)
                print("Instructor registrado correctamente.")

            elif opcion == 2:
                nombre = pedir_texto("Nombre del estudiante: ")
                edad = pedir_entero("Edad del estudiante: ")
                estudiante = Estudiante(nombre, edad)
                estudiantes.append(estudiante)
                print("Estudiante registrado correctamente.")

            elif opcion == 3:
                nombre_curso = pedir_texto("Nombre del curso: ")
                print("\nInstructores disponibles:")
                instructor = seleccionar_elemento(instructores, "instructor")
                curso = Curso(nombre_curso, instructor)
                cursos.append(curso)
                print("Curso creado correctamente.")

            elif opcion == 4:
                print("\nCursos disponibles:")
                curso = seleccionar_elemento(cursos, "curso")
                print("\nEstudiantes disponibles:")
                estudiante = seleccionar_elemento(estudiantes, "estudiante")
                curso.inscribir_estudiante(estudiante)
                print("Estudiante inscrito correctamente.")

            elif opcion == 5:
                if not cursos:
                    raise ValueError("No hay cursos creados.")

                print("\n--- LISTA DE CURSOS ---")
                for curso in cursos:
                    print(curso.mostrar_detalle())
                    print("-" * 40)

            elif opcion == 6:
                print("Saliendo del sistema...")
                break

            else:
                raise ValueError("La opcion ingresada no es valida.")

        except ValueError as error:
            print(f"Error de valor: {error}")
        except IndexError as error:
            print(f"Error de seleccion: {error}")
        except TypeError as error:
            print(f"Error de tipo: {error}")
        except Exception as error:
            print(f"Ocurrio un error inesperado: {error}")


if __name__ == "__main__":
    main()
