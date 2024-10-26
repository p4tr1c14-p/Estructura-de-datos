'''
Nombre: Patricia Pérez Cruz
Fecha: 26 de octubre de 2024
Descripción:
Ejemplos de uso de los operadores relacionales.
'''

"""
Los operadores relacionales son símbolos que se utilizan en programación para comparar dos valores. 
Estos operadores devuelven un valor booleano (verdadero o falso) dependiendo del resultado de la comparación. 
Son fundamentales para tomar decisiones dentro de un programa, ya que permiten construir expresiones condicionales 
que determinan el flujo de ejecución.

Operadores Relacionales Comunes:
Operador	Significado
==	Igual a
!=	Diferente de
>	Mayor que
<	Menor que
>=	Mayor o igual que
<=	Menor o igual que
➡️ Por lo tanto se utilizan para comparar dos valores
"""

# Se solicitan dos números para realizar distintas operaciones relacionales.
# ➡️ Convertimos la entrada a float para permitir comparaciones de números decimales
numero1 = float(input("Ingresa un número decimal: "))
numero2 = float(input("Ingresa otro número decimal: "))

print()
print(f"¿Los números son iguales? {numero1 == numero2}")
print(f"¿Los números son diferentes? {numero1 != numero2}")
print(f"¿El número {numero1:.2f} es mayor que {numero2:.2f}? {numero1 > numero2}")
print(f"¿El número {numero1:.2f} es menor que {numero2:.2f}? {numero1 < numero2}")
print(f"¿El número {numero1:.2f} es mayor o igual que {numero2:.2f}? {numero1 >= numero2}")
print(f"¿El número {numero1:.2f} es menor o igual que {numero2:.2f}? {numero1 <= numero2}")


"""
➡️ Para comprender mejor todo lo anterior, en clase realizamos el siguiente ejercicio para familiarizarnos con los
operadores relacionales

num01 = input("Ingrese un numero: ")
num02 = input("Ingrese un numero: ")

num11 = float(num01)
num22 = float(num02)


print(f"¿El numero {num11:.2f} es mayor a {num22:.2f}?: {num11 > num22}")
print(f"¿El numero {num11:.2f} es mayor igual a {num22:.2f}?: {num11 >= num22}")
print(f"¿El numero {num11:.2f} es igual a {num22:.2f}?: {num11 == num22}")
print(f"¿El numero {num11:.2f} es menor a {num22:.2f}?: {num11 < num22}")
print(f"¿El numero {num11:.2f} es menor igual a {num22:.2f}?: {num11 <= num22}")
print(f"¿El numero {num11:.2f} es diferente a {num22:.2f}?: {num11 != num22}")
"""

# Nota: Es importante recordar que el tipo de datos de las variables afecta las comparaciones
# ➡️ Por lo tanto siempre hay que asegurarnos de que ambos valores sean del mismo tipo (en este caso, flotantes)
# ya que es importante para evitar errores 😀