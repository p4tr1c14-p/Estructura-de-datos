'''
Nombre: Patricia Pérez Cruz
Fecha: 29 de octubre de 2024
Descripción: Este programa es un ejercicio sobre los ciclos while
'''

#➡️ Función para mostrar el menú y recibir la opción
def menu():
    print("Bienvenido al menú de mi calculadora 😀")
    print("0) Salir.")
    print("1) Suma.")
    print("2) Resta.")
    print("3) Multiplicación.")
    print("4) División.")
    print("5) División entera.")
    print("6) Exponenciación.")
    opcion = int(input("Ingrese una opción: "))
    return opcion

#➡️ Función para la operación de suma
def suma():
    numero_uno = float(input("Ingrese un número: "))
    numero_dos = float(input("Ingrese otro número: "))
    print(f"La suma de {numero_uno} y {numero_dos} es {numero_uno + numero_dos:.2f}.")
    print()

#➡️ Función para la operación de resta
def resta():
    numero_uno = float(input("Ingrese un número: "))
    numero_dos = float(input("Ingrese otro número: "))
    print(f"La resta de {numero_uno} y {numero_dos} es {numero_uno - numero_dos:.2f}.")
    print()

#➡️ Función para la operación de multiplicación
def multiplicacion():
    numero_uno = float(input("Ingrese un número: "))
    numero_dos = float(input("Ingrese otro número: "))
    print(f"La multiplicación de {numero_uno} y {numero_dos} es {numero_uno * numero_dos:.2f}.")
    print()

#➡️ Función para la operación de división
def division():
    numero_uno = float(input("Ingrese un número: "))
    numero_dos = float(input("Ingrese otro número: "))
    if numero_dos != 0:  #➡️ Verificar que no se divida por cero
        print(f"La división entre {numero_uno} y {numero_dos} es: {numero_uno / numero_dos:.2f}.")
    else:
        print("Error: No se puede dividir entre cero.")
    print()

#➡️ Función para la operación de división entera
def division_entera():
    numero_uno = float(input("Ingrese un número: "))
    numero_dos = float(input("Ingrese otro número: "))
    if numero_dos != 0:  #➡️ Verificar que no se divida por cero
        print(f"La división entera entre {numero_uno} y {numero_dos} es {numero_uno // numero_dos:.2f}.")
    else:
        print("Error: No se puede dividir entre cero.")
    print()

#➡️ Función para la operación de exponenciación
def exponenciacion():
    numero_uno = float(input("Ingrese un número: "))
    numero_dos = float(input("Ingrese otro número: "))
    print(f"La exponenciación de {numero_uno} a la {numero_dos} es {numero_uno ** numero_dos:.2f}.")
    print()

# ** El ciclo principal del programa **
print("*** Calculadora básica ***")
opcion = None  # Inicializamos la variable de opción

while opcion != 0:  #➡️ Mientras el usuario no ingrese 0, el ciclo continuará
    opcion = menu()  #➡️ Llamada a la función menu() para mostrar el menú y obtener la opción

    if opcion == 1:  #➡️ Opción 1: Suma
        suma()
    elif opcion == 2:  #➡️ Opción 2: Resta
        resta()
    elif opcion == 3:  #➡️ Opción 3: Multiplicación
        multiplicacion()
    elif opcion == 4:  #➡️ Opción 4: División
        division()
    elif opcion == 5:  #➡️ Opción 5: División entera
        division_entera()
    elif opcion == 6:  #➡️ Opción 6: Exponenciación
        exponenciacion()
    elif opcion > 0:  #➡️ Opción inválida
        print("Opción inválida")
        print()

print("Gracias por usar la calculadora 😎")  #➡️ Mensaje de despedida
