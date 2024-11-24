'''
Nombre: Patricia Pérez Cruz
Fecha: 29 de octubre de 2024
Descripción: Este programa es un ejercicio sobre los ciclos while
'''

#➡️ Función para mostrar el menú
def menu():
    print("Bienvenido al menú de triángulos 📐")
    print("0) Salir.")
    print("1) Primer triángulo.")
    print("2) Segundo triángulo.")
    print("3) Tercer triángulo.")
    print("4) Cuarto triángulo.")
    opcion = int(input("Ingrese su selección: "))  # Recibe la opción elegida por el usuario y la convierte a entero
    return opcion

#➡️ Función para el primer triángulo
def primer_triangulo():
    fila = int(input("Ingrese el número de filas que desee: "))
    filauno = fila
    contador = fila

    print("Primer triángulo")
    for i in range(1, filauno + 1):
        asteriscos1 = " * " * i  #➡️ Multiplico el asterisco por el i de mi for
        print(f" {asteriscos1}")
    print()

#➡️ Función para el segundo triángulo
def segundo_triangulo():
    fila = int(input("Ingrese el número de filas que desee: "))
    filauno = fila
    contador = fila

    print("Segundo triángulo")
    for x in range(1, fila + 1):
        asteriscos2 = " * " * fila
        fila = fila - 1  #➡️ Resto uno a las filas para que me diera el triángulo que quería
        print(f" {asteriscos2}")
    print()

#➡️ Función para el tercer triángulo
def tercer_triangulo():
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

#➡️ Función para el cuarto triángulo
def cuarto_triangulo():
    print("Cuarto triángulo")
    fila = int(input("Ingrese el número de filas que desee: "))
    filauno = fila
    contador = 0
    for z in range(1, filauno + 1):
        print(" " * (filauno - z) + "*" * z)
        print()

# ** Ciclo principal del programa **
print("*** Bienvenido a mi menú de triángulos ***")

opciones = None  #➡️ Inicializamos la variable de opciones

while opciones != 0:  #➡️ Mientras el usuario no ingrese 0, el ciclo continuará
    opciones = menu()  #➡️ Llamada a la función menu() para mostrar el menú y obtener la opción

    if opciones == 1:
        primer_triangulo()
    elif opciones == 2:
        segundo_triangulo()
    elif opciones == 3:
        tercer_triangulo()
    elif opciones == 4:
        cuarto_triangulo()
    elif opciones > 0:
        print("Opción inválida")
        print()

print("Gracias por usar mi programa 😎")
