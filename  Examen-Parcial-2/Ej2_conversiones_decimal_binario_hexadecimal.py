"""
Nombre: Patricia Pérez Cruz
Fecha: 6 de diciembre de 2024
Descripción:
Este programa convierte números entre
las bases decimal, binaria y hexadecimal.
"""

def decimal_a_binario(decimal):
    binario = "" #➡️ Inicíe la variable binario como una cadena vacía, ya que se irá llenando a medida que se calculan los dígitos binarios
    numero = decimal

    #➡️ Convertí un número decimal a binario usando la operación de módulo 2
    while numero > 0:
        resto = numero % 2
        #➡️ Agregué el dígito binario al principio de la cadena
        if resto == 1:
            binario = "1" + binario
        else:
            binario = "0" + binario
        numero = numero // 2  #➡️ División entera entre el 2

    #➡️ Verifiqué si la variable binario está vacía después de la ejecución del bucle, y si lo esta significa que había un 0 y en binario es 0
    if binario == "":
        binario = "0"
    return binario

def decimal_a_hexadecimal(decimal):
    hexadecimal = ""
    hexa = "0123456789ABCDEF"  #➡️ En esta cadena puse los caracteres hexadecimales
    numero = decimal

    #➡️ Convertí un número decimal a hexadecimal dividiendo por 16
    while numero > 0:
        resto = numero % 16
        hexadecimal = hexa[resto] + hexadecimal  #➡️ Usé el resto para obtener el valor hexadecimal
        numero = numero // 16  #➡️ Dividí el número entre 16

    #➡️ Si el número es 0 se asigna "0" al hexadecimal
    if hexadecimal == "":
        hexadecimal = "0"
    return hexadecimal

def binario_a_decimal(binario):
    decimal = 0
    potencia = 0

    #➡️ Convertí un número binario a decimal sumando las potencias de 2
    for i in range(len(binario) - 1, -1, -1):
        if binario[i] == "1":
            decimal = decimal + (2 ** potencia)
        potencia = potencia + 1
    return decimal

def binario_a_hexadecimal(binario):
    #➡️ Convertí el binario a hexadecimal pasando por decimal
    decimal = binario_a_decimal(binario)
    return decimal_a_hexadecimal(decimal)

def hexadecimal_a_decimal(hexadecimal):
    hexa = "0123456789ABCDEF"
    decimal = 0
    potencia = 0

    #➡️ Convertí un número hexadecimal a decimal utilizando su posición en la base 16
    for i in range(len(hexadecimal) - 1, -1, -1): #➡️ Recorrí el número hexadecimal de derecha a izquierda, empezando por el último dígito
        for j in range(len(hexa)):
            if hexadecimal[i] == hexa[j]:
                decimal = decimal + (j * (16 ** potencia))  #➡️ Sumé el valor del dígito en base 16
                break
        potencia = potencia + 1
    return decimal

def hexadecimal_a_binario(hexadecimal):
    #➡️ Convertí hexadecimal a binario pasando por decimal
    decimal = hexadecimal_a_decimal(hexadecimal)
    return decimal_a_binario(decimal)

def mostrar_menu():
    print("***  Ejercicio 2. Conversión entre las bases decimal, binaria y hexadecimal.  ***")

    print("1) Convertir de decimal a binario y hexadecimal.")
    print("2) Convertir de binario a decimal y hexadecimal.")
    print("3) Convertir de hexadecimal a decimal y binario.")
    print("0) Salir.")
    elijio = int(input("Ingrese su elección: "))
    print("---------------------------------------------------")
    print()
    return elijio

#➡️ Aquí inicia mi bucle principal
opcion = None
while opcion != 0:
    opcion = mostrar_menu()

    if opcion == 0:
        print("¡Hasta luego!")
        break

    elif opcion == 1:
        #➡️ Aquí se realiza la conversión de decimal a binario y hexadecimal
        decimal = int(input("Ingresa un número decimal: "))
        binario = decimal_a_binario(decimal)
        hexadecimal = decimal_a_hexadecimal(decimal)
        print("\nDecimal", decimal)
        print("Binario:", binario)
        print("Hexadecimal:", hexadecimal)
        print("---------------------------------------------------")
        print()

    elif opcion == 2:
        #➡️ Aquí se realiza la conversión de binario a decimal y hexadecimal
        binario = input("Ingresa un número binario: ")
        decimal = binario_a_decimal(binario)
        hexadecimal = binario_a_hexadecimal(binario)
        print("Binario", binario)
        print("Decimal:", decimal)
        print("Hexadecimal:", hexadecimal)
        print("---------------------------------------------------")
        print()

    elif opcion == 3:
        #➡️ Aquí se realiza la conversión de hexadecimal a decimal y binario
        hexadecimal = input("Ingresa un número hexadecimal: ")
        decimal = hexadecimal_a_decimal(hexadecimal)
        binario = hexadecimal_a_binario(hexadecimal)
        print("Hexadecimal", hexadecimal)
        print("Decimal:", decimal)
        print("Binario:", binario)
        print("---------------------------------------------------")
        print()

    else:
        #➡️ Si la opción no es válida se muestra un mensaje de error
        print("Opción no válida.")
        print("---------------------------------------------------")
        print()
