"""
Nombre: Patricia Pérez Cruz
Fecha: 6 de enero de 2025
Descripción:
Este programa es una nueva versión del juego
realizado de piedra, papel y tijeras, pero
basada en la serie coreana "El juego del calamar".
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
    opcion_dos = int(input("Ingrese otra opción: "))
    print()
    return opcion, opcion_dos

def jugar(opcion, opcion_dos):
    if opcion == 1 :
        eleccion = PIEDRA
    elif opcion == 2 :
        eleccion = PAPEL
    elif opcion == 3:
        eleccion = TIJERAS

    if opcion_dos == 1:
        segunda_eleccion = PIEDRA
    elif opcion_dos == 2:
        segunda_eleccion = PAPEL
    elif opcion_dos == 3:
        segunda_eleccion = TIJERAS




    eleccion_cpu = choice([PIEDRA, PAPEL, TIJERAS])
    cpu_segunda = choice([PIEDRA, PAPEL, TIJERAS])
    return eleccion,segunda_eleccion, eleccion_cpu, cpu_segunda

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

print(" ***  Juego de piedra, papel o tijeras basado en 'El juego del calamar 🦑🦑🦑'  *** ")
opcion = None
opcion_dos = None
while opcion != 0 or opcion_dos != 0:
    opcion, opcion_dos = menu()

    if opcion == 0 or opcion_dos == 0:
        print("Gracias por jugar. ¡Hasta pronto!")
        break

    else:
        if 0 < opcion < 4 or 0 < opcion_dos < 4:  # ➡️Comprobé si la opción está fuera del rango permitido
            print("Opción no válida. Por favor, ingrese un número entre 0 y 3.")
            print()

        #➡️ Aquí se obtienen las elecciones del jugador y de la CPU

        eleccion_usuario, segunda_eleccion_usuario, eleccion_cpu, segunda_cpu = jugar(opcion, opcion_dos)
        print(f"\nJugador eligió: {eleccion_usuario,segunda_eleccion_usuario}")
        print(f"CPU eligió: {eleccion_cpu, segunda_cpu}")
        print()


        print("Jugador 06 es hora de elegir una opción 💀🦑")
        print()
        print(f"Sus opciones para elegir son: \n 1-{eleccion_usuario} \n2-{segunda_eleccion_usuario}")
        seleccion = int(input("Ingresa tu decisión: "))
        print()

        if seleccion == 1:
            seleccion_final = eleccion_usuario
        else:
            seleccion_final = segunda_eleccion_usuario


        print("Es turno de la CPU para elegir una opción...")
        seleccion_cpu = choice([eleccion_cpu, segunda_cpu])
        print(f"\n La CPU eligió: {seleccion_cpu} 🦑")
        print()

        #➡️ Se determinó el resultado del juego con base en las reglas
        resultado = piedra_papel_tijeras.get((seleccion_final, seleccion_cpu), EMPATE)

        if resultado == JUGADOR:
            vi_ju = vi_ju + 1
            print("🗝️ El ganador es el Jugador")
            #➡️ Muestro los resultados acumulados
            print(f"Victoras del jugador: {vi_ju}, Victorias del CPU: {vi_cpu}, Empates: {vi_empate}")
            print()
        elif resultado == CPU:
            vi_cpu = vi_cpu + 1
            print("🗝️ El ganador es el CPU")
            # ➡️ Muestro los resultados acumulados
            print(f"Victoras del jugador: {vi_ju}, Victorias del CPU: {vi_cpu}, Empates: {vi_empate}")
            print()
        else:
            vi_empate = vi_empate + 1
            print("🗝️ Es un empate")
            # ➡️ Muestro los resultados acumulados
            print(f"Victoras del jugador: {vi_ju}, Victorias del CPU: {vi_cpu}, Empates: {vi_empate}")
            print()