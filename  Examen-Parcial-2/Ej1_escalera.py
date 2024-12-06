"""
Nombre: Patricia Pérez Cruz
Fecha: 6 de diciembre de 2024
Descripción:
Este programa dibuja una escalera, en donde
el usuario ingresa el número de escalones.
Si el número es positivo, la escalera será ascendente.
Si el número es negativo, la escalera será descendente.
"""

def solicitar():
    #➡️ Solicité al usuario el número de escalones
    valor_ingresado = int(input("Ingresa el número de escalones (positivo - ascendente y negativo - descendente) o ingresa un cero para salir: "))
    print()
    return valor_ingresado

print(" *  Ejercicio 1. La escalera.  * ")
opcion = None

while opcion != 0:
    opcion = solicitar()  #➡️ Resivo el número de escalones

    if opcion == 0:
        #➡️ Si el usuario ingresa 0 se termina el programa
        print("Gracias por usar mi programa, adiós")
        break
    elif opcion > 0:
        #➡️ Si el número es positivo, la escalera será ascendente
        for i in range(1, opcion + 1):
            #➡️ Ajusté los espacios para que haya dos espacios entre cada escalón
            print(" " * (opcion - i) * 2 + "_|")  #➡️ Los espacios entre escalones son ahora de 2
    elif opcion < 0:
        #➡️ Si el número es negativo la escalera será descendente
        print("_" * 1)
        for i in range(1, -opcion + 1):
            #➡️ Para los escalones descendentes puse 2 espacios entre cada uno
            print(" " * (i * 2) + "|_")  #➡️ El espacio entre cada escalón lo multiplique por 2
    else:
        print("Opción inválida")  #➡️ En caso de que no se ingrese un número válido (aunque esto no debería ocurrir aquí)
