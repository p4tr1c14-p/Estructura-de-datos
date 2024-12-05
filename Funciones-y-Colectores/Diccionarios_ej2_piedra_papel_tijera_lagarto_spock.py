"""
Nombre: Patricia Pérez Cruz
Fecha: 2 de diciembre de 2024
Descripción:
Este programa es una versión mejorada del
juego de piedra, papel y tijeras.
"""

from random import choice #➡️ Siempre importar porque si no me marca error

#➡️ Estas son las constantes para representar las opciones del juego y los posibles resultados
PIEDRA = "Piedra"
PAPEL = "Papel"
TIJERAS = "Tijeras"
JUGADOR = "Jugador"
EMPATE = "Empate"
CPU = "Cpu"
LAGARTO = "Lagarto"
SPOCK = "Spock"

def menu():
    print("1) Piedra.")
    print("2) Papel.")
    print("3) Tijera.")
    print("4) Lagarto.")
    print("5) Spock.")
    print("6) Ver reglas.")
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
    elif opcion == 4:
        eleccion_usuario = LAGARTO
    elif opcion == 5:
        eleccion_usuario = SPOCK
    eleccion_cpu = choice([PIEDRA, PAPEL, TIJERAS, LAGARTO, SPOCK])

    return eleccion_usuario, eleccion_cpu

#➡️ Este es mi diccionario que define las reglas del juego: las combinaciones ganadoras para el jugador o la CPU
piedra_papel_tijeras = {(PIEDRA, TIJERAS): JUGADOR,
                        (PIEDRA, PAPEL): CPU,
                        (TIJERAS, PAPEL): JUGADOR,
                        (TIJERAS, PIEDRA): CPU,
                        (PAPEL, PIEDRA): JUGADOR,
                        (PAPEL, TIJERAS): CPU,
                        (PIEDRA, LAGARTO): JUGADOR,
                        (LAGARTO, PIEDRA): CPU,
                        (LAGARTO, SPOCK): JUGADOR,
                        (SPOCK, LAGARTO): CPU,
                        (SPOCK, TIJERAS): JUGADOR,
                        (TIJERAS, SPOCK): CPU,
                        (TIJERAS, LAGARTO): JUGADOR,
                        (LAGARTO, TIJERAS): CPU,
                        (LAGARTO, PAPEL): JUGADOR,
                        (PAPEL, LAGARTO): CPU,
                        (PAPEL, SPOCK): JUGADOR,
                        (SPOCK, PAPEL): CPU,
                        (SPOCK, PIEDRA): JUGADOR,
                        (PIEDRA, SPOCK): CPU,
                        }

"""
Reglas:
Selecciona una de las opciones de acuerdo a lo siguiente:
- Tijeras cortan papel.
- Papel cubre piedra.
- Piedra aplasta lagarto.
- Lagarto envenena Spock.
- Spock destruye tijeras.
- Tijeras decapitan lagarto.
- Lagarto come papel.
- Papel desaprueba Spock.
- Spock vaporiza piedra.
- Piedra aplasta tijeras.
La CPU va a elegir una de las opciones de manera aleatoria.
"""
