'''
Nombre: Patricia Pérez Cruz
Fecha: 29 de octubre de 2024
Descripción: Este programa es un ejercicio sobre los ciclos while
'''

print("*** Calculadora básica ***")
opcion = None #➡️ Aplique lo que me comento sobre la variable None
while opcion != 0: #➡️ Mientras el usuario no me ingrese 0 mi programa seguirá continuando
    print("Bienvenido al menú de mi calculadora 😀")
    print("0) Salir.")
    print("1) Suma.")
    print("2) Resta.")
    print("3) Multiplicación.")
    print("4) División")
    print("5) División entera.")
    print("6) Exponenciación.")
    opcion = int(input("Ingrese una opción: "))

    if opcion == 1: #➡️Opción 1 suma
        numero_uno, numero_dos = float(input("Ingrese un número: ")), float(input("Ingrese otro número: "))
        print(f"La suma de {numero_uno} y {numero_dos} es {numero_uno + numero_dos:.2f}.")
        print()
    elif opcion == 2: #➡️Opción 2 resta
        numero_uno, numero_dos = float(input("Ingrese un número: ")), float(input("Ingrese otro número: "))
        print(f"La resta de {numero_uno} y {numero_dos} es {numero_uno - numero_dos:.2f}.")
        print()
    elif opcion == 3: #➡️Opción 3 multiplicación
        numero_uno, numero_dos = float(input("Ingrese un número: ")), float(input("Ingrese otro número: "))
        print(f"La multiplicación de {numero_uno} y {numero_dos} es {numero_uno * numero_dos:.2f}.")
        print()
    elif opcion == 4: #➡️Opción 4 división
        numero_uno, numero_dos = float(input("Ingrese un número: ")), float(input("Ingrese otro número: "))
        print(f"La división entre {numero_uno} y {numero_dos} es: { numero_uno / numero_dos:.2f}.")
        print()
    elif opcion == 5: #➡️Opción 5 división entera
        numero_uno, numero_dos = float(input("Ingrese un número: ")), float(input("Ingrese otro número: "))
        print(f"La división entera entre {numero_uno} y {numero_dos} es {numero_uno // numero_dos:.2f}.")
        print()
    elif opcion == 6: #➡️Opción 6 exponenciación
        numero_uno, numero_dos = float(input("Ingrese un número: ")), float(input("Ingrese otro número: "))
        print(f"La exponenciación de {numero_uno} a la {numero_dos} es {numero_uno ** numero_dos:.2f}.")
        print()
    else:
        print("Opción inválida")
        print()