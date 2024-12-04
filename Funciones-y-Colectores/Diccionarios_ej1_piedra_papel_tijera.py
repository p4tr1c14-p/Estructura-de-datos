"""
Nombre: Patricia Pérez Cruz
Fecha: 2 de diciembre de 2024
Descripción:
Este programa es una nueva versión del juego
realizado de piedra, papel y tijeras, pero
utilizando un diccionario para las reglas del juego.
"""
from random import choice

PIEDRA = "Piedra"
PAPEL = "Papel"
TIJERAS = "Tijeras"
JUGADOR = "Jugador"
EMPATE = "Empate"
CPU = "Gana la CPU"

def menu():
    print("1) Piedra.")
    print("2) Papel.")
    print("3) Tijera.")
    print("0) Salir.")
    print()
    opcion = int(input("Ingrese una opción: "))
    return opcion
    print()

def jugar(opcion):
    if opcion == 1:
        eleccion_usuario = PIEDRA
    elif opcion == 2:
        eleccion_usuario = PAPEL
    elif opcion == 3:
        eleccion_usuario = TIJERAS

    eleccion_cpu = choice([PIEDRA, PAPEL, TIJERAS])
    return eleccion_usuario, eleccion_cpu

piedra_papel_tijeras = {(PIEDRA, TIJERAS): JUGADOR,
                        (PIEDRA, PAPEL): CPU,
                        (TIJERAS, PAPEL): JUGADOR,
                        (TIJERAS, PIEDRA): CPU,
                        (PAPEL, PIEDRA): JUGADOR,
                        (PAPEL, TIJERAS): CPU
                        }

print(" ***  Juego de piedra, papel o tijeras  *** ")
opcion = None
while opcion != 0:
    opcion = menu()
    if opcion < 0 or opcion > 3: # ➡️Comprobé si la opción está fuera del rango permitido
        print("Opción no válida. Por favor, ingrese un número entre 0 y 3.")
        print()
    else:
        if opcion == 0:
            print("Gracias por jugar. ¡Hasta pronto!")
            break

        eleccion_usuario, eleccion_cpu = jugar(opcion)
        print(f"\nJugador eligió: {eleccion_usuario}")
        print(f"CPU eligió: {eleccion_cpu}")
        print()

        resultado = piedra_papel_tijeras.get((eleccion_usuario, eleccion_cpu), EMPATE)
        if resultado == JUGADOR:
            print("El ganador es el Jugador")
            print()
        elif resultado == CPU:
            print("El ganador es el CPU")
            print()
        else:
            print("Es un empate")
            print()