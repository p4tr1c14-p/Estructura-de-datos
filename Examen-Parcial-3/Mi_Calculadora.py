"""
Nombre: Patricia Pérez Cruz
Fecha: 22 de enero de 2025
Descripción: Función main con ingreso dinámico de números
"""

def menu() -> int:
    """
    Muestra un menu de opciones al usuario y solicita una seleccion
    Retorna:
        int: La opcion seleccionada por el usuario (0, 1 o 2)
    """
    seguir = True
    while seguir:
        print("1. Sumar")
        print("2. Multiplicar")
        print("0. Salir")
        seleccion = input("Elige una opcion: ")
        if seleccion.isnumeric(): # Reviso si es un numero, para lo de la validacion
            seleccion = int(seleccion)
            if seleccion in (0, 1, 2):
                seguir = False
                return seleccion
        print("Por favor, ingresa una opcion valida 😳")

def sumar(*args) -> float:
    """
    Realiza la suma de los numeros proporcionados
    Parametros:
        *args: Numeros a sumar
    Retorna:
        float: El resultado de la suma de los numeros
    """
    return sum(args)

def multiplicacion(*args) -> float:
    """
    Realiza la multiplicacion de los numeros proporcionados
    Parametros:
        *args: Numeros a multiplicar
    Retorna:
        float: El resultado de la multiplicacion de los numeros
    """
    resultado = 1
    for i in args:
        resultado = resultado * i
    return resultado

def ingresar_numeros() -> tuple:
    """
    Solicita al usuario ingresar una lista de numeros dinamicamente
    Los numeros pueden ser enteros o decimales. El usuario puede finalizar
    el ingreso escribiendo 'fin'
    Retorna:
        tuple: Una tupla con los numeros ingresados
    """
    numeros = []
    contador = 1
    while True:
        print("\nIngrese sus numeros")
        continuar = True
        while continuar:
            numero = input(f"Ingresa el numero {contador} (o 'fin' para terminar): ")

            if numero.lower() == 'fin':
                if numeros:
                    return tuple(numeros)
                else:
                    print("Debes ingresar al menos un numero")

            no_puntos = numero.count(".")
            no_guiones = numero.count("-")
            revisar_cadena = numero.lstrip("-").replace(".", "")

            if revisar_cadena.isnumeric() and no_guiones in (0, 1) and no_puntos in (0, 1):
                continuar = False # si mi entrada es valida se detiene el ciclo
                numeros.append(float(numero))
                contador = contador + 1
            else:
                print("Entrada no valida. Por favor ingrese un numero valido (entero o decimal) 😳")

def main() -> None:
    """
    Funcion principal que ejecuta el programa
    Permite al usuario seleccionar entre sumar o multiplicar numeros ingresados
    """
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
            print(f"Resultado de la multiplicacion: {resultado}")

if __name__ == '__main__':
    main()
