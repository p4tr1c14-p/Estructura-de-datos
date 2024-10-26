
'''
Nombre:Patricia Pérez Cruz
Fecha: 24 de octubre de 2024
Descripción:
Ejemplos de uso de los operadores relacionales.
'''

"""
Los operadores lógicos permiten combinar expresiones booleanas (verdadero o falso) para crear condiciones más complejas.
Estos operadores nos permiten realizar operaciones lógicas como "y", "o" y "no", lo que nos da la capacidad de tomar 
decisiones más sofisticadas dentro de nuestros programas.
"""

"""
➡️ Los siguientes operadores aritméticos ya los conocía:
 + SUMA
 - RESTA
 * MULTIPLICACIÓN
 / DIVISIÓN
 % MODULO
 ➡️ Pero estos dos fueron nuevos para mí 😀
 // DIVISIÓN QUE SOLO ME DA EL RESULTADO ENTERO
 ** ES PARA ELEVAR EL PRIMER NÚMERO A LA PONTENCIA DEL SEGUNDO NÚMERO
"""

# Se solicitan dos números enteros al usuario.
numero1 = int(input("Ingresa un número entero: "))
numero2 = int(input("Ingresa otro número entero: "))

# Se realizan las operaciones aritméticas.
print()
print("  ***   Ejemplos de uso de los operadores aritméticos   ***")

print(f"La suma de ({numero1} + {numero2}) es: {numero1 + numero2}") #➡️ Realiza la suma de los dos números
print(f"La resta de ({numero1} - {numero2}) es: {numero1 - numero2}") #➡️ Realiza la resta de los dos números
print(f"La multiplicación de ({numero1} * {numero2}) es: {numero1 * numero2}") #➡️ Multiplica los dos números
print(f"La división de ({numero1} / {numero2}) es: {(numero1 / numero2):.2f}")  #➡️ Muestra la división con dos decimales (Notar la forma para mostrar dos decimales)
print(f"La división entera de ({numero1} // {numero2}) es: {numero1 // numero2}") #➡️ Realiza la división entera
print(f"El módulo de ({numero1} % {numero2}) es: {numero1 % numero2}") #➡️ Calcula el residuo de la división
print(f"La exponenciación  de ({numero1} ** {numero2}) es: {numero1 ** numero2}") #➡️ Eleva el primer número a la potencia del segundo


"""
Ejercicio corto para repasar los conocimientos anteriores:

var_int = input("Ingrese su número entero: ")
var_int2 = input("Ingrese su otro número entero: ")

entero1 = int(var_int)
entero2 = int(var_int2)

multi = entero1 / entero2
print(f" El resultado: {multi: .2f}")
print(entero1 // entero2)
print(entero1 ** entero2)
"""