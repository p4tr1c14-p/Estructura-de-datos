"""
Nombre: Patricia Pérez Cruz
Fecha: 22 de enero de 2025
Descripción: Función main con ingreso dinámico de números
"""

def menu() -> int:
    seguir = True
    while seguir:
        print("1. Sumar")
        print("2. Multiplicar")
        print("0. Salir")
        seleccion = input("Elige una opción: ")
        if seleccion.isnumeric(): #Reviso si es un número, para lo de la validación
            seleccion = int(seleccion)
            if seleccion in (0, 1, 2):
                seguir = False
                return seleccion
        print("Por favor, ingresa una opción válida 😳")

def sumar(*args) -> float:
    #Realizo la suma
    return sum(args)

def multiplicacion(*args) -> float:
    resultado = 1
    for i in args:
        resultado = resultado * i
    return resultado

def ingresar_numeros() -> tuple:
    #Regreso una tupla
    numeros = []
    contador = 1
    while True:
        print("\nIngrese sus números")
        continuar = True
        while continuar:
            numero = input(f"Ingresa el número {contador} (o 'fin' para terminar): ")

            if numero.lower() == 'fin':
                if numeros:
                    return tuple(numeros)
                else:
                    print("Debes ingresar al menos un número.")


            no_puntos = numero.count(".")
            no_guiones = numero.count("-")
            revisar_cadena = numero.lstrip("-").replace(".", "")

            if revisar_cadena.isnumeric() and no_guiones in (0, 1) and no_puntos in (0, 1):
                continuar = False # si mi entrada es válida se detiene el ciclo
                numeros.append(float(numero))
                contador = contador + 1
            else:
                print("Entrada no válida. Por favor ingrese un número válido (entero o decimal) 😳")

def main() -> None:
    opcion = None
    while opcion != 0:
        opcion = menu()

        if opcion == 1:
            numeros = ingresar_numeros()
            resultado = sumar(*numeros)
            print(f"Resultado de la suma: {resultado}")
        elif opcion == 2:
            numeros = ingresar_numeros()
            resultado = multiplicacion(*numeros)
            print(f"Resultado de la multiplicación: {resultado}")

if __name__ == '__main__':
    main()