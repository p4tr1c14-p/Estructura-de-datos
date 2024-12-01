"""
Nombre: Patricia Pérez Cruz
Fecha: 29 de noviembre de 2024
Descripción:
Este programa es una rifa, en donde se registra
el correo electrónico y solamente permite ingresar
un correo por participante.
"""

from random import choice  #➡️ Importo la función choice para seleccionar un ganador aleatoriamente

print("  ***  Rifa de una computadora  ***")
correos = set() #➡️ Aquí declaré mi conjunto

def menu(): #➡️Esta función es mi menú
    print("Bienvenido al menú de esta rifa")
    print("1) Ver correos de participantes.")
    print("2) Agregar correo de participante.")
    print("3) Eliminar correo de participante.")
    print("4) Seleccionar ganador.")
    print("0) Salir.")
    seleccion = int(input("Ingrese su selección: ")) #➡️ Convertí la selección en entero
    return seleccion

def  ver_correos(): #➡️ Mi menú para mostrar los correos que hay hasta el momento
    if len(correos) == 0: #➡️ Si no tiene nada entonces esta vacía
        print("La lista esta vacía")
        print("-------------------------")
    else: #➡️ De lo contrario muestro las que hay
        print("El conjunto de correos es: ")
        for correo in correos: #➡️ Iterar sobre cada correo
            print(f"-{correo}")
            print()

def agregar_nuevo():
    nuevo = input("Ingrese su correo: ")
    correos.add(nuevo) #➡️ Aquí agregué el nuevo correo con add
    print("Correo agregado correctamente")
    print("-------------------------")
    print()

def eliminar_correo():
    if len(correos) == 0:
        print("La lista esta vacía")
        print("-------------------------")
        print()
    else:
        ver_correos()
        print("-------------------------")
        eliminar = input("Ingrese el correo a eliminar: ")
        correos.remove(eliminar) #➡️ Elimino el correo deseado
        print("Correo eliminado correctamente")
        print("-------------------------")
        print()

def ganador():
    lista = list(correos)  # ➡️ Para poder sacar al ganador convertí mi conjunto a lista
    if len(lista) == 0:
        print("La lista está vacía")
        print("-------------------------")
        print()
    else:
        gano = choice(lista)  # ➡️ Con mi conjunto como lista ya puedo usar choice
        print(f"El correo gandor es: {gano}. Muchas felicidades! 🤩")
        print("-------------------------")
        print()

auxiliar = None
while auxiliar != 0: #➡️ Esto es para mantener el programa activo hasta que se elija salir
    auxiliar = menu()
    if auxiliar == 0:
        print("Adiós 🧚‍♀️")
    elif auxiliar == 1:
        ver_correos()
    elif auxiliar == 2:
        agregar_nuevo()
    elif auxiliar == 3:
        eliminar_correo()
    elif auxiliar == 4:
        ganador()
    else:
        print("Ingrese un número válido ")
        print()