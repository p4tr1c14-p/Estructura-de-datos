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
        encontrado = False
        for alumno in calificaciones:
            if alumno[0].lower() == nombre.lower():  # El nombre está en el índice 0
                print(f"Calificaciones de {alumno[0]}:")
                for i, materia in enumerate(materias):
                    print(f"{materia}: {alumno[1][i]}")  # Las calificaciones están en el índice 1 (como lista)
                encontrado = True
                break
        if not encontrado:
            print(f"Alumno {nombre} no encontrado.")

def ver_promedios_alumnos():
    if len(calificaciones) == 0:
        print("No hay alumnos registrados.")
    else:
        print("Promedios de los alumnos:")
        for alumno in calificaciones:
            suma = sum(alumno[1])  # Las calificaciones están en el índice 1
            promedio = suma / len(materias)
            print(f"{alumno[0]}: {promedio:.2f}")

def anadir_alumno():
    nombre = input("Ingrese el nombre del nuevo alumno: ")
    existe = False
    for alumno in calificaciones:
        if alumno[0].lower() == nombre.lower():
            print(f"El alumno {nombre} ya está registrado.")
            existe = True
            break

    if not existe:
        calificaciones_alumno = []
        for materia in materias:
            valido = False
            while not valido:
                cal = int(input(f"Ingrese la calificación de {materia}: "))
                if 0 <= cal <= 100:
                    calificaciones_alumno.append(cal)
                    valido = True
                else:
                    print("Ingrese un número válido entre 0 y 100.")
        calificaciones.append([nombre, calificaciones_alumno])
        print(f"Alumno {nombre} añadido exitosamente.")

def eliminar_alumno():
    if len(calificaciones) == 0:
        print("No hay alumnos registrados.")
    else:
        nombre = input("Ingrese el nombre del alumno a eliminar: ")
        indice = -1
        for i, alumno in enumerate(calificaciones): #🧐🧐🧐🧐
            if alumno[0].lower() == nombre.lower():  # El nombre está en el índice 0
                indice = i
                break
        if indice != -1:
            del calificaciones[indice]
            print(f"Alumno {nombre} eliminado exitosamente.")
        else:
            print(f"Alumno {nombre} no encontrado.")

def ver_promedio_grupal():
    if len(calificaciones) == 0:
        print("No hay alumnos registrados.")
    else:
        suma_materias = [0] * len(materias)
        for alumno in calificaciones:
            for i in range(len(materias)):
                suma_materias[i] += alumno[1][i]
        print("Promedio grupal por materia:")
        for i, materia in enumerate(materias): #🧐🧐🧐🧐
            promedio = suma_materias[i] / len(calificaciones)
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
