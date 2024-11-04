"""
Patricia Pérez Cruz
04 de noviembre de 2024.
Descripción:
Este programa es un juego en donde el usuario intente adivinar un número secreto.
"""
print("*** Juego del adivinador ***")
from random import randint  #➡️ Importé la función randint para generar un número aleatorio

# Inicializo el número secreto
adivina = 0
numero_secreto = 0



print("¡Bienvenido al juego de adivinanza! 🤩🎉")  #➡️ Mi mensaje de bienvenida
print("[F]- 10 intentos y números del 1-50")
print("[M]- 5 intentos y números del 1-100")
print("[D]- 4 intentos y números del 1-110")
nivel = input("Ingrese el nivel de dificultad deseado: ")

if nivel != "F" and nivel != "M" and nivel != "D":
    print("Opción no válida. Por favor, ingrese F, M o D")
else:
    if nivel == "F":
        numero_secreto = randint(1, 50)  # ➡️ Genero un número aleatorio entre 1 y 100
        intentos = 10
        intento_actual = 1
        while intento_actual <= intentos:  # ➡️ Mientras no se superen los intentos
            adivina = int(input(f"Número de intento {intento_actual}. Ingresa un número de 1-50: "))  # ➡️ Indico el intento actual y solicito el número
            if adivina == numero_secreto:  # ➡️ Compruebo si el número ingresado es igual al número secreto
                print(f"¡Felicidades!, adivinaste el número en {intento_actual} intentos.")
                intento_actual = intentos + 1  # ➡️ Salgo del bucle incrementando el contador para terminar el juego
            elif adivina < numero_secreto:  # ➡️ Si el número ingresado es menor que el número secreto
                print("El número a adivinar es mayor.")  # ➡️ Indico que el número es mayor
            else:  # ➡️ Si el número ingresado es mayor que el número secreto
                print("El número a adivinar es menor.")  # ➡️ Indico que el número es menor
            intento_actual = intento_actual + 1  # ➡️ Incremento el contador de intentos
        if adivina != numero_secreto:  # ➡️ Verifico si el número adivinado no es el secreto
            print(f"Perdiste. El número era: {numero_secreto}.")  # ➡️ Mensaje con el número secreto

    elif nivel == "M":
        numero_secreto = randint(1, 100)  # ➡️ Genero un número aleatorio entre 1 y 100
        intentos = 5
        intento_actual = 1
        while intento_actual <= intentos:  # ➡️ Mientras no se superen los intentos
            adivina = int(input(
                f"Número de intento {intento_actual}. Ingresa un número de 1-100: "))  # ➡️ Indico el intento actual y solicito el número
            if adivina == numero_secreto:  # ➡️ Compruebo si el número ingresado es igual al número secreto
                print(f"¡Felicidades!, adivinaste el número en {intento_actual} intentos.")
                intento_actual = intentos + 1  # ➡️ Salgo del bucle incrementando el contador para terminar el juego
            elif adivina < numero_secreto:  # ➡️ Si el número ingresado es menor que el número secreto
                print("El número a adivinar es mayor.")  # ➡️ Indico que el número es mayor
            else:  # ➡️ Si el número ingresado es mayor que el número secreto
                print("El número a adivinar es menor.")  # ➡️ Indico que el número es menor
            intento_actual = intento_actual + 1  # ➡️ Incremento el contador de intentos
        if adivina != numero_secreto:  # ➡️ Verifico si el número adivinado no es el secreto
            print(f"Perdiste. El número era: {numero_secreto}.")  # ➡️ Mensaje con el número secreto

    elif nivel == "D":
        numero_secreto = randint(1, 110)  # ➡️ Genero un número aleatorio entre 1 y 100
        intentos = 4
        intento_actual = 1
        while intento_actual <= intentos:  # ➡️ Mientras no se superen los intentos
            adivina = int(input(
                f"Número de intento {intento_actual}. Ingresa un número de 1-110: "))  # ➡️ Indico el intento actual y solicito el número
            if adivina == numero_secreto:  # ➡️ Compruebo si el número ingresado es igual al número secreto
                print(f"¡Felicidades!, adivinaste el número en {intento_actual} intentos.")
                intento_actual = intentos + 1  # ➡️ Salgo del bucle incrementando el contador para terminar el juego
            elif adivina < numero_secreto:  # ➡️ Si el número ingresado es menor que el número secreto
                print("El número a adivinar es mayor.")  # ➡️ Indico que el número es mayor
            else:  # ➡️ Si el número ingresado es mayor que el número secreto
                print("El número a adivinar es menor.")  # ➡️ Indico que el número es menor
            intento_actual = intento_actual + 1  # ➡️ Incremento el contador de intentos
        if adivina != numero_secreto:  # ➡️ Verifico si el número adivinado no es el secreto
            print(f"Perdiste. El número era: {numero_secreto}.")  # ➡️ Mensaje con el número secreto


