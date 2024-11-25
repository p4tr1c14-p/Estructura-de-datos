print(" *** PROMEDIOS DEL PARCIAL 1 *** ")

calificaciones = []
materias = ["ESTRUCTURA DE DATOS", "DERECHO Y LEGISLACIÓN", "CONTABILIDAD", "ELECTRÓNICA", "ÁLGEBRA"]

def menu():
    print("Bienvenido a mi menú 😉")
    print("1) Ver calificaciones de alumno")
    print("2) Ver promedios de alumnos")
    print("3) Añadir alumno")
    print("4) Eliminar alumno")
    print("5) Ver promedio grupal")
    print("0) Salir")
    opcion = int(input("Ingrese su selección: "))
    return opcion

def ver_calificaciones_alumno():
    if len(calificaciones) == 0:
        print("No hay alumnos registrados.")
    else:
        nombre = input("Ingrese el nombre del alumno: ")
        encontrado = 0
        for alumno in calificaciones:
            if alumno["nombre"].lower() == nombre.lower():
                print(f"Calificaciones de {alumno["nombre"]}:")
                for materia in materias:
                    print(f"{materia}: {alumno["calificaciones"][materia]}")
                encontrado = 1
                break
        if encontrado != 1:
            print(f"Alumno {nombre} no encontrado.")

def ver_promedios_alumnos():
    if len(calificaciones) == 0:
        print("No hay alumnos registrados.")
    else:
        print("Promedios de los alumnos:")
        for alumno in calificaciones:
            suma = 0
            for materia in materias:
                suma = suma + alumno["calificaciones"][materia]
            promedio = suma / len(materias)
            print(f"{alumno["nombre"]}: {promedio:.2f}")

def anadir_alumno():
    nombre = input("Ingrese el nombre del nuevo alumno: ")
    existe = 0
    for alumno in calificaciones:
        if alumno["nombre"].lower() == nombre.lower():
            print(f"El alumno {nombre} ya está registrado.")
            existe = 1
            break

    if existe != 1:
        calificaciones_alumno = {}
        for materia in materias:
            valido = 0
            while valido == 0:
                cal = input(f"Ingrese la calificación de {materia}: ")
                if cal.isdigit() and 0 <= int(cal) <= 100:
                    calificaciones_alumno[materia] = int(cal)
                    valido = 1
                else:
                    print("Ingrese un número válido entre 0 y 100.")
        calificaciones.append({"nombre": nombre, "calificaciones": calificaciones_alumno})
        print(f"Alumno {nombre} añadido exitosamente.")


def eliminar_alumno():
    if len(calificaciones) == 0:
        print("No hay alumnos registrados.")
    else:
        nombre = input("Ingrese el nombre del alumno a eliminar: ")
        indice = -1
        for i in range(len(calificaciones)):
            if calificaciones[i]["nombre"].lower() == nombre.lower():
                indice = i
                break
        if indice != -1:
            del calificaciones[indice]
            print(f"Alumno {nombre} eliminado exitosamente.")
        else:
            print(f"Alumno {nombre} no encontrado.")

#
def ver_promedio_grupal():
    if len(calificaciones) == 0:
        print("No hay alumnos registrados.")
    else:
        suma_materias = {materia: 0 for materia in materias}
        for alumno in calificaciones:
            for materia in materias:
                suma_materias[materia] += alumno["calificaciones"][materia]
        print("Promedio grupal por materia:")
        for materia in materias:
            promedio = suma_materias[materia] / len(calificaciones)
            print(f"{materia}: {promedio:.2f}")

opcion = None

while opcion != 0:
    opcion = menu()
    if opcion == 1:
        ver_calificaciones_alumno()
    elif opcion == 2:
        ver_promedios_alumnos()
    elif opcion == 3:
        anadir_alumno()
    elif opcion == 4:
        eliminar_alumno()
    elif opcion == 5:
        ver_promedio_grupal()
    elif opcion > 5:
        print("Opción inválida")

print("Adiós 🤓")