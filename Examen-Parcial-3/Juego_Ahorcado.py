"""
Nombre: Patricia Pérez Cruz
Fecha: 24 de enero de 2025
Descripción: Los jugadores deben adivinar una palabra secreta antes de quedarse sin intentos
"""

import random

def jugar_ahorcado():
    """
    Implementa el juego del ahorcado donde los jugadores deben adivinar una palabra
    antes de agotar sus intentos. Las palabras se agrupan por categorias, y el
    jugador tiene 6 intentos antes de perder
    """
    palabras = {
        "Frutas 🍉": ["manzana", "platano", "uva", "kiwi", "cereza"],
        "Animales 🦊": ["gato", "perro", "elefante", "jirafa", "tigre"],
        "Colores 🎨": ["rojo", "azul", "verde", "amarillo", "morado"]
    }
    max_intentos = 6

    categoria = random.choice(list(palabras.keys())) # Selecciono una categoria aleatoria
    palabra = random.choice(palabras[categoria]) # Selecciono una palabra aleatoria de esa categoria
    letras_correctas = set() # Letras acertadas
    letras_incorrectas = set() # Letras falladas
    partes_cuerpo = 0 # Contador de errores

    print(f"\n¡Juego del Ahorcado! Ls categoria es, tan tan tan 🤔🥁: {categoria}")
    print()

    while partes_cuerpo < max_intentos:
        palabra_mostrada = ""
        for letra in palabra:
            if letra in letras_correctas:
                palabra_mostrada += letra
            else:
                palabra_mostrada += "_"

        print(f"\n{palabra_mostrada}") # Muestra la palabra con guiones bajos y letras adivinadas

        # Dibujo del ahorcado segun los errores cometidos
        if partes_cuerpo == 0:
            print("  ------\n   |    |\n   |    \n   |    \n   |    \n   |    \n  ---")
        elif partes_cuerpo == 1:
            print("  ------\n   |    |\n   |    O\n   |    \n   |    \n   |    \n  ---")
        elif partes_cuerpo == 2:
            print("  ------\n   |    |\n   |    O\n   |    |\n   |    \n   |    \n  ---")
        elif partes_cuerpo == 3:
            print("  ------\n   |    |\n   |    O\n   |   /|\n   |    \n   |    \n  ---")
        elif partes_cuerpo == 4:
            print("  ------\n   |    |\n   |    O\n   |   /|\\\n   |    \n   |    \n  ---")
        elif partes_cuerpo == 5:
            print("  ------\n   |    |\n   |    O\n   |   /|\\\n   |   /\n   |    \n  ---")
        elif partes_cuerpo == 6:
            print("  ------\n   |    |\n   |    O\n   |   /|\\\n   |   / \\\n   |    \n  ---")

        # Muestra las letras incorrectas usadas
        if letras_incorrectas:
            incorrectas = ""
            for letra in letras_incorrectas:
                incorrectas += letra + " "
            print(f"Letras incorrectas: {incorrectas.strip()}")

        # Solicita al jugador ingresar una letra
        letra = input("Introduce una letra: ").lower()

        if len(letra) != 1 or not letra.isalpha(): # Validacion del input
            print("Por favor, introduce una letra valida")

        if letra in letras_correctas or letra in letras_incorrectas:
            print("Ya has intentado esa letra")

        if letra in palabra:
            letras_correctas.add(letra) # Agrega la letra correcta
            print("Letra correcta!")
        else:
            letras_incorrectas.add(letra) # Agrega la letra incorrecta
            partes_cuerpo = partes_cuerpo + 1
            print("Letra incorrecta")

        # Verifica si todas las letras han sido adivinadas
        if set(palabra) <= letras_correctas:
            print(f"¡Felicidades! Has adivinado la palabra: {palabra}")
            return

    print(f"Perdiste! La palabra era: {palabra}") # Muestra la palabra si se pierde

if __name__ == "__main__":
    jugar_ahorcado()
