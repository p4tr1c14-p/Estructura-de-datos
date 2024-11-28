from random import choice

print("  ***  Rifa de una computadora  ***")
correos = set()

def menu():
    print("Bienvenido al menú de esta rifa")
    print("1) Ver correos de participantes.")
    print("2) Agregar correo de participante.")
    print("3) Eliminar correo de participante.")
    print("4) Seleccionar ganador.")
    print("0) Salir.")
    seleccion = int(input("Ingrese su selección: "))
    return seleccion

def  ver_correos():
    if len(correos) == 0:
        print("La lista esta vacia")
        print("-------------------------")
    else:
        print("El conjunto de correos es: ")
        for correo in correos:
            print(f"-{correo}")
            print()

def agregar_nuevo():
    nuevo = input("Ingrese su correo: ")
    correos.add(nuevo)
    print("Correo agregado correctamente")
    print("-------------------------")

def eliminar_correo():
    ver_correos()
    print("-------------------------")
    eliminar = input("Ingrese el correo a eliminar: ")
    correos.remove(eliminar)
    print("Correo eliminado correctamente")
    print()
    print("-------------------------")

def ganador():
    lista = list(correos)
    if len(lista) == 0:
        print("La lista esta vacia")
        print("-------------------------")
    else:
        gano = choice(lista)
        print(f"El ganador es: {gano}")
        print("Felicidades 🤩")
        print("-------------------------")


auxiliar = None
while auxiliar != 0:
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
