# Ejercicio4_juego_adivinador.py

from random import randint  # ➡️ Importé la función randint para generar un número aleatorio

# Inicializo el número secreto
numero_secreto = randint(1, 100)  # ➡️ Genero un número aleatorio entre 1 y 100
intentos = 5  # ➡️ Establezco el número de intentos permitidos
intento_actual = 1  # ➡️ Inicializo el contador de intentos

print("¡Bienvenido al juego de adivinanza! 🎉")  # ➡️ Mensaje de bienvenida
print("Tienes 5 intentos para adivinar un número entre 1 y 100.")  # ➡️ Indico al jugador cuántos intentos tiene

# Inicio del bucle de intentos
while intento_actual <= intentos:  # ➡️ Mientras no se superen los intentos
    adivina = int(input(f"Número de intento {intento_actual}. Ingresa un número de 1-100: "))  # ➡️ Indico el intento actual y solicito el número

# Verifico si el número ingresado es correcto
    if adivina == numero_secreto:  # ➡️ Compruebo si el número ingresado es igual al número secreto
        print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intento_actual} intentos.")  # ➡️ Mensaje de felicitación
        break  # ➡️ Salgo del bucle si el jugador adivina correctamente
    elif adivina < numero_secreto:  # ➡️ Si el número ingresado es menor que el número secreto
        print("El número a adivinar es mayor.")  # ➡️ Indico que el número es mayor
    else:  # ➡️ Si el número ingresado es mayor que el número secreto
        print("El número a adivinar es menor.")  # ➡️ Indico que el número es menor

    intento_actual += 1  # ➡️ Incremento el contador de intentos

# Si el jugador no adivina el número después de los 5 intentos
if adivina != numero_secreto:  # ➡️ Verifico si el número adivinado no es el secreto
    print(f"Perdiste. El número era: {numero_secreto}.")  # ➡️ Mensaje con el número secreto
