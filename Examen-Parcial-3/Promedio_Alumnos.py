"""
Nombre: Patricia Pérez Cruz
Fecha: 23 de enero de 2025
Descripción: Programa que permite ingresar las materias y calificaciones de un alumno, calcula
el promedio general y muestra el resultado
"""

def menu() -> int:
    """
    Muestra el menu principal al usuario para elegir una opcion
    Retorna:
        int: La opcion seleccionada por el usuario (0 o 1)
    """
    seguir = True
    while seguir:
        print("\n1. Ingresar materias")
        print("0. Salir")
        seleccion = input("Elige una opcion: ")
        if seleccion.isnumeric(): # Reviso si es un numero
            seleccion = int(seleccion)
            if seleccion in (0, 1):
                return seleccion
        print("Por favor, ingresa una opcion valida 😳")

def ingresar_calificaciones() -> None:
    """
    Permite ingresar las materias y calificaciones de un alumno de manera dinamica
    Calcula el promedio general y muestra los resultados
    """
    continuar = True
    while continuar:
        nombre = input("Ingresa el nombre del alumno (o 'fin' para terminar): ")

        if nombre.lower() == 'fin': # Convierto a minusculas para que no tenga problemas a futuro
            print("Ingreso de calificaciones terminado")
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
                    calificacion = float(input(f"Ingresa la calificacion de {nombre} en {materia}: "))
                    if 0 <= calificacion <= 10:
                        materias[materia] = calificacion
                        break
                    else:
                        print("La calificacion debe estar entre 0 y 10 porfi")
                except ValueError:
                    print("Ingresa un numero valido")

        if materias: # Con el .values solo agarro los valores y no las llaves
            promedio = sum(materias.values()) / len(materias)
            print(f"\n---- {nombre} ----")
            for materia, calificacion in materias.items():
                print(f"- {materia}: {calificacion}")
            print(f"El promedio fue de: {promedio:.2f}")
        else:
            print(f"{nombre}: Sin materias registradas")

def main() -> None:
    """
    Funcion principal que ejecuta el programa
    Permite seleccionar opciones y gestionar el flujo del programa
    """
    while True:
        opcion = menu()

        if opcion == 0:
            break
        elif opcion == 1:
            ingresar_calificaciones()

if __name__ == '__main__':
    main()
