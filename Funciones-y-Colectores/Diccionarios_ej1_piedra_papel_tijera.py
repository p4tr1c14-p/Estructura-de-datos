"""
Nombre: Patricia Pérez Cruz
Fecha: 2 de diciembre de 2024
Descripción:
Este programa es una nueva versión del juego
realizado de piedra, papel y tijeras, pero
utilizando un diccionario para las reglas del juego.
"""
from random import choice #➡️ Siempre importar porque si no me marca error

#➡️ Estas son las constantes para representar las opciones del juego y los posibles resultados
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

#➡️ Este es mi diccionario que define las reglas del juego: las combinaciones ganadoras para el jugador o la CPU
piedra_papel_tijeras = {(PIEDRA, TIJERAS): JUGADOR,
                        (PIEDRA, PAPEL): CPU,
                        (TIJERAS, PAPEL): JUGADOR,
                        (TIJERAS, PIEDRA): CPU,
                        (PAPEL, PIEDRA): JUGADOR,
                        (PAPEL, TIJERAS): CPU
                        }
#➡️ Variables para llevar el conteo de victorias
vi_ju = 0
vi_cpu = 0
vi_empate = 0

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