"""
Patricia Pérez Cruz
04 de noviembre de 2024.
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
opcion = "hola"
cpu_opcion = "hi"

while opcion != "Salir" and opcion != "salir": #➡️ Inicié el bucle principal que se ejecuta mientras la opción no sea 0
    print(f"Score 😎🎯: Victorias del jugador: {victoria_ju}, Partidos empatados: {empate}, Victorias del CPU: {victoria_cpu}")
    print()
    print("Piedra.")
    print("Papel.")
    print("Tijera.")
    print("Salir.")
    print()

    opcion = input("Ingrese una opción: ")

    if opcion == "Salir":
        opcion = "salir"
    if opcion == "piedra" or opcion == "papel" or opcion == "tijera":
        minusculas = 1

    # Verificar si la opción es válida
    if opcion != "Piedra" and opcion != "piedra" and opcion != "Papel" and opcion != "papel" and opcion != "Tijera" and opcion != "tijera" : # ➡️Comprobé si la opción está fuera del rango permitido
        print("Salir...")
    else:  #➡️ Regresar al inicio del bucle

        cpu = randint(1, 3) # ➡️Generé una opción aleatoria para el CPU

        # Mostrar qué eligió cada uno
        if cpu == 1:
            if minusculas == 1:
                cpu_opcion = "piedra"
            else:
                cpu_opcion == "Piedra"
        elif cpu == 2:
            if minusculas == 1:
                cpu_opcion = "papel"
            else:
                cpu_opcion == "Papel"
        elif cpu == 3:
            if minusculas == 1:
                cpu_opcion = "tijera"
            else:
                cpu_opcion == "Tijera"



        if opcion == cpu_opcion: #➡️ Verifiqué si el jugador y el CPU eligieron lo mismo
            empate += 1 #➡️ Incrementé el contador de empates
            print(f"Jugador: {opcion}, CPU: {cpu_opcion}, El resultado es empate")
        elif (cpu_opcion == "Tijera" or cpu_opcion == "tijera") and (opcion == "Piedra" or opcion == "piedra") or (cpu_opcion == "Papel" or cpu_opcion == "papel") and (opcion == "Tijera" or opcion == "tijera") or (cpu_opcion == "Piedra" or cpu_opcion == "piedra") and (opcion == "Papel" or opcion == "papel"): #➡️ Verifiqué si el jugador gana
            victoria_ju += 1 #➡️ Incrementé el contador de victorias del jugador
            print(f"Jugador: {opcion}, CPU: {cpu_opcion}, El ganador es el CPU")
        elif (cpu_opcion == "Piedra" or cpu_opcion == "piedra") and (opcion == "Tijera" or opcion == "tijera") or (cpu_opcion == "Tijera" or cpu_opcion == "tijera)" and (opcion == "Papel" or opcion == "papel") or (cpu_opcion == "Papel" or cpu_opcion == "papel") and opcion == "Piedra" or opcion == "piedra"): #➡️ Verifiqué si el CPU gana
            victoria_cpu += 1 #➡️ Incrementé el contador de victorias del CPU
            print(f"Jugador: {opcion}, CPU: {cpu_opcion}, El ganador es el jugador")

print("Gracias por jugar! 👋")
