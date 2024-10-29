"""
Patricia Pérez Cruz
14 de octubre de 2024
Descripción: Este programa lo hice para practicar la conversión de tipos de
datos (casting) en Python, por lo que incluye ejercicios que demuestran cómo convertir valores
entre diferentes tipos de datos, como de cadenas a enteros, de cadenas a números flotantes,
de números a cadenas, y de valores a booleanos
"""

# a) Convierta los siguientes números en cadenas: 3.14159265, 12, 0.

print("*** Convertir números a cadenas ***")
print()

var_float = 3.14159265
print(f"El valor {var_float} será convertida a cadena: {str(var_float)}.")
print()
var_int = 12
print(f"El valor {var_int} será convertida a cadena: {str(var_int)}.")
print()
var_int = 0
print(f"El valor {var_int} será convertida a cadena: {str(var_int)}.")
print()


# b) De los números anteriores, indica su valor booleano.

print("*** Convertir números a booleno ***")
print()

var_int = 3.14159265
es_verdadero = bool(var_int)
print(f"¿El valor {var_int} es verdadero?: {es_verdadero}.")
print()

var_int = 12
es_verdadero = bool(var_int)
print(f"¿El valor {var_int} es verdadero?: {es_verdadero}.")
print()

var_int = 0
es_verdadero = bool(var_int)
print(f"¿El valor {var_int} es verdadero?: {es_verdadero}.")
print()


# c) Convierta las siguientes cadenas a números: "10002", "100.02", "0".

print("*** Convertir cadenas a números ***")
print()

var_cadena = "10002"
var_int = int(var_cadena)
print(f"La cadena {var_cadena} como número es: {var_int}.")
print()

var_cadena = "100.02"
var_float = float(var_cadena)
print(f"La cadena {var_cadena} como número es: {var_float}")
print()

var_cadena = "0"
var_int = int(var_cadena)
print(f"La cadena {var_cadena} como número es: {var_int}.")
print()

# d) De las cadenas anteriores, indica su valor booleano ("10002", "100.02", "0").
# Nota: especificar por qué el resultado de la cadena "0".
print("*** Convertir cadenas a booleano ***")
print()

var_cadena = "10002"
es_verdadero = bool(var_cadena)
print(f"¿El valor de la cadena {var_cadena} es verdadero?: {es_verdadero}")
print()

var_cadena = "100.02"
es_verdadero = bool(var_cadena)
print(f"El valor de la cadena {var_cadena} es verdadero?: {es_verdadero}")
print()

var_cadena = "0"
es_verdadero = bool(var_cadena)
print(f"El valor de la cadena {var_cadena} es verdadero?: {es_verdadero}")
print()

""" Explicación de lo arriba ⬆️:
De la cadena "0" sale True porque en Python cualquier cadena no vacía es 
considerada verdadera, incluso si su contenido es "0" la cadena no esta vacía
por lo que sale como salida True
"""