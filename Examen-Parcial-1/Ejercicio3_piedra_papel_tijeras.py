"""
Patricia Pérez Cruz
31 de octubre de 2024.
Descripción:
Este programa es el famoso juego de "piedra, papel o tijera", en donde el contrincante es la CPU.
La opción de la CPU se escogerá de forma aleatorio con la función randint().
El juego mostrará las victorias del jugador, los partidos empatados y las victorias del CPU.
"""

print("*** Juego de piedra, papel, tijera ***")
from random import randint #➡️ Importé la función randint para generar números aleatorios

victoria_ju = 0 #➡️ Inicialicé el contador de victorias del jugador, empate, victorias del CPU y la opción del jugador
empate = 0
victoria_cpu = 0
opcion = 1

while opcion != 0: #➡️ Inicié el bucle principal que se ejecuta mientras la opción no sea 0
    print(f"Score 😎🎯: Victorias del jugador: {victoria_ju}, Partidos empatados: {empate}, Victorias del CPU: {victoria_cpu}")
    print()
    print("1) Piedra.")
    print("2) Papel.")
    print("3) Tijera.")
    print("0) Salir.")
    print()

    opcion = int(input("Ingrese una opción: "))

    # Verificar si la opción es válida
    if opcion < 0 or opcion > 3: # ➡️Comprobé si la opción está fuera del rango permitido
        print("Opción no válida. Por favor, ingrese un número entre 0 y 3.")
    else:  #➡️ Regresar al inicio del bucle

        cpu = randint(1, 3) # ➡️Generé una opción aleatoria para el CPU

        # Mostrar qué eligió cada uno
        if cpu == 1:
            cpu_opcion = "Piedra"
        elif cpu == 2:
            cpu_opcion = "Papel"
        else:
            cpu_opcion = "Tijera"

        if opcion == 1:
            jugador_opcion = "Piedra"
        elif opcion == 2:
            jugador_opcion = "Papel"
        else:
            jugador_opcion = "Tijera"

        # Lógica del juego
        if cpu == opcion: #➡️ Verifiqué si el jugador y el CPU eligieron lo mismo
            empate += 1 #➡️ Incrementé el contador de empates
            print(f"Jugador: {jugador_opcion}, CPU: {cpu_opcion}, El resultado es empate")
        elif (cpu == 1 and opcion == 2) or (cpu == 2 and opcion == 3) or (cpu == 3 and opcion == 1): #➡️ Verifiqué si el jugador gana
            victoria_ju += 1 #➡️ Incrementé el contador de victorias del jugador
            print(f"Jugador: {jugador_opcion}, CPU: {cpu_opcion}, El ganador es el jugador")
        elif (cpu == 1 and opcion == 3) or (cpu == 2 and opcion == 1) or (cpu == 3 and opcion == 2): #➡️ Verifiqué si el CPU gana
            victoria_cpu += 1 #➡️ Incrementé el contador de victorias del CPU
            print(f"Jugador: {jugador_opcion}, CPU: {cpu_opcion}, El ganador es el CPU")

print("Gracias por jugar!")
