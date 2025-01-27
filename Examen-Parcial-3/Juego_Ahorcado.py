"""
Nombre: Patricia Pérez Cruz
Fecha: 24 de enero de 2025
Descripción: Los jugadores deben adivinar una palabra secreta antes de quedarse sin intentos
"""

import random

def jugar_ahorcado():
    palabras = {
        "Frutas 🍉": ["manzana", "platano", "uva", "kiwi", "cereza"],
        "Animales 🦊": ["gato", "perro", "elefante", "jirafa", "tigre"],
        "Colores 🎨": ["rojo", "azul", "verde", "amarillo", "morado"]
    }
    max_intentos = 6

    categoria = random.choice(list(palabras.keys()))
    palabra = random.choice(palabras[categoria])
    letras_correctas = set()
    letras_incorrectas = set()
    partes_cuerpo = 0

    print(f"\n¡Juego del Ahorcado! Categoría: {categoria}")

    while partes_cuerpo < max_intentos:
        palabra_mostrada = ""
        for letra in palabra:
            if letra in letras_correctas:
                palabra_mostrada += letra
            else:
                palabra_mostrada += "_"

        print(f"\n{palabra_mostrada}")

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

        if letras_incorrectas:
            incorrectas = ""
            for letra in letras_incorrectas:
                incorrectas += letra + " "
            print(f"Letras incorrectas: {incorrectas.strip()}")

        letra = input("Introduce una letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, introduce una letra válida")

        if letra in letras_correctas or letra in letras_incorrectas:
            print("Ya has intentado esa letra")

        if letra in palabra:
            letras_correctas.add(letra)
            print("Letra correcta!")
        else:
            letras_incorrectas.add(letra)
            partes_cuerpo = partes_cuerpo + 1
            print("Letra incorrecta")

        if set(palabra) <= letras_correctas:
            print(f"¡Felicidades! Has adivinado la palabra: {palabra}")
            return

    print(f"Perdiste! La palabra era: {palabra}")

if __name__ == "__main__":
    jugar_ahorcado()