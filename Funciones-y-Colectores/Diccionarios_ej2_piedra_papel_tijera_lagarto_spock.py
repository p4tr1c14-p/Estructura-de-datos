"""
Nombre: Patricia Pérez Cruz
Fecha: 2 de diciembre de 2024
Descripción:
Este programa es una versión mejorada del
juego de piedra, papel y tijeras.
"""

from random import choice #➡️ Siempre importar porque si no me marca error

#➡️ Estas son las constantes para representar las opciones del juego
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

#➡️ La función jugar devuelve la elección del jugador basada en su opción del menú
# y genera aleatoriamente la elección de la CPU
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
#➡️ Aquí ya solo agrugué las nuevas opciones que son lo del lagarto y spock
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

#➡️ Variables para llevar el conteo de victorias
vi_ju = 0
vi_cpu = 0
vi_empate = 0

print(" ***  Juego de piedra, papel, tijeras, lagarto, spock  *** ")
opcion = None
while opcion != 0:
    opcion = menu()
    if opcion < 0 or opcion > 6: #➡️ Comprobé si la opción está fuera del rango permitido
        print("Opción no válida. Por favor, ingrese un número entre 0 y 3.")
        print()
    elif opcion == 6: #➡️ Agregué esta opción para que el usuario conozca las reglas
        #➡️ Además, en el print tuve que utilizar tres """ para que se imprimiera correctamente
        print("""Reglas:
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
        La CPU va a elegir una de las opciones de manera aleatoria.""")

    else:
        if opcion == 0:
            print("Gracias por jugar. ¡Hasta pronto! 🤓")
            break

        #➡️ Aquí se obtienen las elecciones del jugador y de la CPU
        eleccion_usuario, eleccion_cpu = jugar(opcion)
        print(f"\nJugador eligió: {eleccion_usuario}")
        print(f"CPU eligió: {eleccion_cpu}")
        print()
        #➡️ Se determinó el resultado del juego con base en las reglas
        resultado = piedra_papel_tijeras.get((eleccion_usuario, eleccion_cpu), EMPATE)

        if resultado == JUGADOR:
            vi_ju = vi_ju + 1
            print("El ganador es el Jugador")
            #➡️ Muestro los resultados acumulados
            print(f"Victoras del jugador: {vi_ju}, Victorias del CPU: {vi_cpu}, Empates: {vi_empate}")
            print()
        elif resultado == CPU:
            vi_cpu = vi_cpu + 1
            print("El ganador es el CPU")
            # ➡️ Muestro los resultados acumulados
            print(f"Victoras del jugador: {vi_ju}, Victorias del CPU: {vi_cpu}, Empates: {vi_empate}")
            print()
        else:
            vi_empate = vi_empate + 1
            print("Es un empate")
            # ➡️ Muestro los resultados acumulados
            print(f"Victoras del jugador: {vi_ju}, Victorias del CPU: {vi_cpu}, Empates: {vi_empate}")
            print()