"""
Patricia Pérez Cruz
31 de octubre de 2024.
Descripción:
Este programa es un juego en donde el usuario intente adivinar un número secreto.
"""
print("*** Juego del adivinador ***")
from random import randint  #➡️ Importé la función randint para generar un número aleatorio

# Inicializo el número secreto
numero_secreto = randint(1, 100)  #➡️ Genero un número aleatorio entre 1 y 100
intentos = 5  #➡️ Establezco el número de intentos permitidos
intento_actual = 1  #➡️ Inicializo el contador de intentos


print("¡Bienvenido al juego de adivinanza! 🤩🎉")  #➡️ Mi mensaje de bienvenida
#➡️ Inicio con e bucle de intentos
while intento_actual <= intentos:  # ➡️ Mientras no se superen los intentos
    adivina = int(input(f"Número de intento {intento_actual}. Ingresa un número de 1-100: "))  #➡️ Indico el intento actual y solicito el número

# Verifico si el número ingresado es correcto
    if adivina == numero_secreto:  #➡️ Compruebo si el número ingresado es igual al número secreto
        print(f"¡Felicidades!, adivinaste el número en {intento_actual} intentos.")
        intento_actual = intentos + 1  # ➡️ Salgo del bucle incrementando el contador para terminar el juego
    elif adivina < numero_secreto:  # ➡️ Si el número ingresado es menor que el número secreto
        print("El número a adivinar es mayor.")  #➡️ Indico que el número es mayor
    else:  #➡️ Si el número ingresado es mayor que el número secreto
        print("El número a adivinar es menor.")  #➡️ Indico que el número es menor
    intento_actual = intento_actual + 1  #➡️ Incremento el contador de intentos


if adivina != numero_secreto:  #➡️ Verifico si el número adivinado no es el secreto
    print(f"Perdiste. El número era: {numero_secreto}.")  #➡️ Mensaje con el número secreto
