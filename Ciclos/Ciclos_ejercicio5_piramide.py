'''
Nombre: Patricia Pérez Cruz
Fecha: 29 de octubre de 2024
Descripción: Este programa es un ejercicio sobre los ciclos while
'''

print("*** Bienvenido a mi menú de triángulos ***")

opciones = None #➡️ Aplique mis nuevos conocimientos adquridos con respecto a la inicialización de este tipo de variables que uso en mis condiciones

while opciones != 0:
    print("Bienvenido al menú de triángulos 📐")
    print("0) Salir.")
    print("1) Primer triángulo.")
    print("2) Segundo triángulo.")
    print("3) Tercer triángulo.")
    print("4) Cuarto triángulo.")
    opciones = int(input("Ingrese su selección: ")) #➡️ Recibo la opción elegida por el usuario y la convierto a entero

    if opciones == 1:
        fila = int(input("Ingrese el número de filas que desee: "))
        filauno = fila
        contador = fila

        print("Primer triángulo")
        for i in range(1, filauno + 1):
            asteriscos1 = " * " * i #➡️Multiplico el asteristico por el i de mi for
            print(f" {asteriscos1}")
        print()
    elif opciones == 2:
        fila = int(input("Ingrese el número de filas que desee: "))
        filauno = fila
        contador = fila

        print("Segundo triángulo")
        for x in range(1, fila + 1):
            asteriscos2 = " * " * fila
            fila = fila - 1 #➡️Reste uno a las filas para que me diera el triangulo que quería
            print(f" {asteriscos2}")
        print()
    elif opciones == 3:
        print("Tercer triángulo")
        fila = int(input("Ingrese el número de filas que desee: "))
        filauno = fila
        contador = 0
        for y in range(1, fila + 1):
            espacio = " " * (fila - y)
            asteriscos3 = "*" * (contador + 1)
            contador += 2
            print(f" {espacio}{asteriscos3}")
            print()

    elif opciones == 4:
        print("Cuarto triángulo")
        fila = int(input("Ingrese el número de filas que desee: "))
        filauno = fila
        contador = 0
        for z in range(1, filauno + 1):
            print(" " * (filauno - z) + "*" * z)
            print()
    elif opciones > 0:
        print("Opción inválida")  # ➡️ Si la opción elegida por el usuario es mayor a cero significa que es una opción inválida
        print()
    else:
        print("Saliendo...")  # ➡️ De lo contrario si es cero termina mi programa

print("Gracias por usar mi programa 😎")
