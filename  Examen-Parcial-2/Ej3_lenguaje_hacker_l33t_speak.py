"""
Nombre: Patricia Pérez Cruz
Fecha: 6 de diciembre de 2024
Descripción:
Este programa convierte un texto al lenguaje hacker (lenguaje leet o 1337).
Esta escritura se caracteriza por reemplazar las letras por números y símbolos.
"""

def convertir_basico(texto):
    # ➡️ Creé mi diccionario de conversión para vocales, donde cada clave es una vocal
    # y su valor es su equivalente en el lenguaje básico
    vocales_basico = {
        'a': '4',
        'e': '3',
        'i': '1',
        'o': '0',
        'u': '(_)',
        'A': '4',
        'E': '3',
        'I': '1',
        'O': '0',
        'U': '(_)'
    }
    # Convertir texto
    texto_convertido = "" #➡️ Aquí lo inicialicé como cadena solo para poder concatenar
    for letra in texto: #➡️ Se recorre cada letra y reemplazá con el valor correspondiente del diccionario
        texto_convertido = texto_convertido + vocales_basico.get(letra, letra) #➡️ Si la letra no está en el diccionario se deja tal cual
    return texto_convertido


def convertir_intermedio(texto):
    #➡️ Este es mi diccionario de conversión para vocales y consonantes del lenguaje intermedio
    conversiones_intermedio = {
        'a': '4',
        'b': 'I3',
        'c': '[',
        'd': ')',
        'e': '3',
        'f': '|=',
        'g': '&',
        'h': '#',
        'i': '1',
        'j': ',_|',
        'k': '>|',
        'l': '1',
        'm': r'/\/\\', #➡️ En esta parte, no logré poner solo esto "/\/\" porque me marcaba error, entonces lo tuve que dejar así
        'n': r'|\|', #➡️ La r antes es solo para que no lo interprete como un carácter especial, sino como un símbolo cualquiera
        'o': '0',
        'p': '|*',
        'q': '(_,)',
        'r': 'I2',
        's': '5',
        't': '7',
        'u': '(_)',
        'v': r'\/',
        'w': r'\/\/',
        'x': '><',
        'y': 'j',
        'z': '2',

        #➡️ Mayúsculas
        'A': '4',
        'B': 'I3',
        'C': '[',
        'D': ')',
        'E': '3',
        'F': '|=',
        'G': '&',
        'H': '#',
        'I': '1',
        'J': ',_|',
        'K': '>|',
        'L': '1',
        'M': r'/\/\\',
        'N': r'|\|',
        'O': '0',
        'P': '|*',
        'Q': '(_,)',
        'R': 'I2',
        'S': '5',
        'T': '7',
        'U': '(_)',
        'V': r'\/',
        'W': r'\/\/',
        'X': '><',
        'Y': 'j',
        'Z': '2'
    }

    # Convertir texto
    texto_convertido = ""
    for letra in texto:
        texto_convertido = texto_convertido + conversiones_intermedio.get(letra, letra)  #➡️ De igual forma si la letra no está en el diccionario, se deja tal cual
        #➡️ Arriba ya concatené
    return texto_convertido

def mi_menu():
    print("*** Ejercicio 3. Lenguaje hacker (l33t sp34k) ***")
    print("1) Convertir un texto a lenguaje básico.")
    print("2) Convertir un texto a lenguaje intermedio.")
    print("0) Salir.")
    seleccion = int(input("Introduzca una opción: "))
    print("---------------------------------------------------")
    print()
    return seleccion


opcion = None
while opcion != 0:
    opcion = mi_menu()
    # Procesar opción
    if opcion == 1: #➡️ Si la opción es 1, convertir a lenguaje básico
        texto = input("Introduzca el texto a convertir a lenguaje básico: ")
        resultado = convertir_basico(texto)
        print("Texto convertido:", resultado)
        print("---------------------------------------------------")
        print()

    elif opcion == 2:  #➡️ Si la opción es 2, convertir a lenguaje intermedio
        texto = input("Introduzca el texto a convertir a lenguaje intermedio: ")
        resultado = convertir_intermedio(texto)
        print("Texto convertido:", resultado)
        print("---------------------------------------------------")
        print()

    elif opcion == 0:
        print("Saliendo del programa 👩‍💻...")
        print("---------------------------------------------------")
        print()

    else:
        print("Opción no válida, por favor intente de nuevo.")
        print("---------------------------------------------------")
        print()
