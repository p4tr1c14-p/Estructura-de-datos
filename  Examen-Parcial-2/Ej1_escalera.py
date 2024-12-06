"""
Nombre: Patricia Pérez Cruz
Fecha: 6 de diciembre de 2024
Descripción:
Este programa dibuja una escalera, en donde
el usuario ingresa el número de escalores.
Si el número es positivo, la escalera será ascendente.
Si el número es negativo, la escalera será descendente.
"""


def solicitar():
    valor_ingresado= int(input("Ingresa el numero de escalones (positivo - ascendente y negativo descendente) o ingresa un cero para salir: "))
    print()
    return valor_ingresado


print(" ***  Ejercicio 1. La escalera.  *** ")
opcion = None

while opcion != 0:
    opcion = solicitar()

    if opcion == 0:
        print("Gracias por usar mi programa, adiós")
        break
    elif opcion > 0:
        for i in range(1, opcion + 1):
            ascendente = "_|" * i
            print(ascendente)
            print()
    elif opcion < 0:
        for d in range(1, opcion + 1):
            descendente = "|_" * i
            print(descendente)
    else:
        print("Opción inválida")