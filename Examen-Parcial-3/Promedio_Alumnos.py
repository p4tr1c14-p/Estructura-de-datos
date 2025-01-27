"""
Nombre: Patricia Pérez Cruz
Fecha: 23 de enero de 2025
Descripción: Programa que permite ingresar las materias y calificaciones de un alumno, calcula
el promedio general y muestra el resultado
"""


def menu() -> int:
    seguir = True
    while seguir:
        print("\n1. Ingresar materias")
        print("0. Salir")
        seleccion = input("Elige una opción: ")
        if seleccion.isnumeric(): #Reviso si es un número
            seleccion = int(seleccion)
            if seleccion in (0, 1):
                return seleccion
        print("Por favor, ingresa una opción válida 😳")

def ingresar_calificaciones() -> None:
    continuar = True
    while continuar:
        nombre = input("Ingresa el nombre del alumno (o 'fin' para terminar): ")

        if nombre.lower() == 'fin': #Convierto a minusculas para que no tenga problemas a futuro
            print("Ingreso de calificaciones terminado.")
            break

        materias = {}
        pasar = True
        while pasar:
            materia = input(f"Ingresa materia para el alumno {nombre} (o 'fin' para terminar): ")

            if materia.lower() == 'fin':
                break

            si_seguir = True
            while si_seguir:
                try:
                    calificacion = float(input(f"Ingresa la calificación de {nombre} en {materia}: "))
                    if 0 <= calificacion <= 10:
                        materias[materia] = calificacion
                        break
                    else:
                        print("La calificación debe estar entre 0 y 10 porfi")
                except ValueError:
                    print("Ingresa un número válido.")

        if materias: #Con el .values solo agarro los valores y no las llaves
            promedio = sum(materias.values()) / len(materias)
            print(f"\n---- {nombre} ----")
            for materia, calificacion in materias.items():
                print(f"- {materia}: {calificacion}")
            print(f"El promedio fue de: {promedio:.2f}")
        else:
            print(f"{nombre}: Sin materias registradas")

def main() -> None:
    while True:
        opcion = menu()

        if opcion == 0:
            break
        elif opcion == 1:
            ingresar_calificaciones()

if __name__ == '__main__':
    main()
