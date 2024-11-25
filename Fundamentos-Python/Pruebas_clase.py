print(" *** PROMEDIOS DEL PARCIAL 1 *** ")

calificaciones = []  # Aquí guardo las calificaciones de todos los alumnos, como una lista de listas
materias = ["ESTRUCTURA DE DATOS", "DERECHO Y LEGISLACIÓN", "CONTABILIDAD", "ELECTRÓNICA", "ÁLGEBRA"]

def menu():
    print("Bienvenido a mi menú 😉")
    print("1) Ver calificaciones detalladas de un alumno")
    print("2) Ver promedio del Parcial 1 de todos los alumnos")
    print("3) Agregar alumno y sus calificaciones")
    print("4) Eliminar alumno y sus calificaciones")
    print("5) Ver promedio grupal del Parcial 1")
    print("6) Ver calificaciones de todos los alumnos")
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
            if alumno[0].lower() == nombre.lower():  # Accedo al nombre del alumno (índice 0)
                print(f"Calificaciones de {alumno[0]}:")  # Imprimo el nombre del alumno
                for i in range(1, len(alumno)):  # Empiezo desde el índice 1 para acceder a las calificaciones
                    print(f"{materias[i-1]}: {alumno[i]}")  # Las calificaciones empiezan desde el índice 1
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
            for i in range(1, len(alumno)):  # Empiezo desde el índice 1 para acceder a las calificaciones
                suma += alumno[i]
            promedio = suma / len(materias)
            print(f"{alumno[0]}: {promedio:.2f}")

def anadir_alumno():
    nombre = input("Ingrese el nombre del nuevo alumno: ")
    existe = 0
    for alumno in calificaciones:
        if alumno[0].lower() == nombre.lower():  # Accedo al nombre con el índice 0
            print(f"El alumno {nombre} ya está registrado.")
            existe = 1
            break

    if existe != 1:
        calificaciones_alumno = [nombre]  # Primero agregamos el nombre
        for materia in materias:
            valido = 0
            while valido == 0:
                cal = float(input(f"Ingrese la calificación de {materia}: "))
                if 0 <= cal <= 100:
                    calificaciones_alumno.append(cal)  # Añadimos las calificaciones
                    valido = 1
                else:
                    print("Ingrese un número válido entre 0 y 100.")
        calificaciones.append(calificaciones_alumno)  # Añadimos el alumno a la lista
        print(f"Alumno {nombre} añadido exitosamente.")

def eliminar_alumno():
    if len(calificaciones) == 0:
        print("No hay alumnos registrados.")
    else:
        nombre = input("Ingrese el nombre del alumno a eliminar: ")
        indice = -1

        for i in range(len(calificaciones)):
            if calificaciones[i][0].lower() == nombre.lower():  # Accedo al nombre con el índice 0
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
            for i in range(1, len(alumno)):  # Empiezo desde el índice 1 para acceder a las calificaciones
                suma_materias[i-1] += alumno[i]
        print("Promedio grupal por materia:")
        for i in range(len(materias)):
            promedio = suma_materias[i] / len(calificaciones)
            print(f"{materias[i]}: {promedio:.2f}")

def ver_calificaciones_todos():
    if len(calificaciones) == 0:
        print("No hay alumnos registrados.")
    else:
        print("Calificaciones de todos los alumnos:")
        for alumno in calificaciones:
            print(f"Alumno: {alumno[0]}")  # El nombre del alumno está en el índice 0
            for i in range(1, len(alumno)):  # Empiezo desde el índice 1 para acceder a las calificaciones
                print(f"{materias[i-1]}: {alumno[i]}")  # Las calificaciones están a partir del índice 1

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
    elif opcion == 6:
        ver_calificaciones_todos()
    elif opcion > 6:
        print("Opción inválida")

print("Adiós 🤓")
