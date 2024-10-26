'''
Nombre: Patricia Pérez Cruz
Fecha: 26 de octubre de 2024
Descripción:
Uso de la sentencia de control if-else.
'''

"""
La sentencia if-else es una estructura de control fundamental que permite tomar decisiones en el código.
Dependiendo de si se cumple una determinada condición, el programa tomará un camino u otro.

Sintaxis:

if condición:
    # Código a ejecutar si la condición es verdadera.

else:
    # Código a ejecutar si la condición es falsa.

# Código que se ejecuta sin importar la condición.
"""

# Ejemplo en donde se determina si un número es par o impar.
print("  ***  Programa que determina si un número es par o impar  ***")
numero = int(input("Ingresa un número: "))  # Solicitamos el número. ➡️ También se convertió la cadena a entero

# lógica para determinar si es par o impar
print()
if numero % 2 == 0:  # Implica que es par. ➡️ Aquí se utilizó el operador módulo para  obtener el residuo y poder deducir si es par o impar
    print("El número es par.")  #➡️ Este cartel solo se imprimirá si se cumple la condición

else:
    print("El número es impar.")  # Implica que es impar. ➡️ De no cumplir con la condición de "if" se imprimirá este cartel