'''
Nombre: Patricia Pérez Cruz
Fecha: 26 de octubre de 2024
Descripción:
Uso de la sentencia de control if.
'''

"""
La sentencia de control if es una estructura de control fundamental que permite ejecutar diferentes bloques de código
 dependiendo de si una condición se cumple o no.

Sintaxis:

if condición: ➡️ También, como su nombre lo dice en español, "Si", si se cumple su condición, se ejecutará; de lo contrario, no
    # Código a ejecutar si la condición es verdadera. Notar que hay que dejar un espacio de tabulador.

# Código que se continúa ejecutando. Notar que ya no hay espacio y está a la misma altura que el if.
"""

# Ejemplo en donde se imprime un mensaje si el usuario tiene la mayoría de edad.
print("  ***  Programa que determina si eres mayor de edad  ***")
numero = int(input("Ingresa tu edad: "))

if numero >= 18: #➡️ Comienza la evaluación de la condición si el usuario es mayor o igual a 18
    print("Eres mayor de edad.")

print("Este código se ejecuta después de evaluarse la sentencia if.") #➡️ Este cartel aparecerá después de evaluar la condición

# Probar qué pasa con espacios simples, no dejando una línea entre ambas funciones print()
# y que ambos print() se encuentren a la misma altura.

