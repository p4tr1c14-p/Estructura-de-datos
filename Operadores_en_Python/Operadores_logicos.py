'''
Nombre:Patricia Pérez Cruz
Fecha: 24 de octubre de 2024
Descripción:
Ejemplos de uso de los operadores relacionales.
➡️  Los operadores relacionales son esenciales
para la lógica de programación en Python, ya que
permiten comparar y tomar decisiones basadas
en los resultados de esas comparaciones
'''

"""
Los operadores lógicos permiten combinar expresiones booleanas (verdadero o falso) para crear condiciones más complejas.
Estos operadores nos permiten realizar operaciones lógicas como "y", "o" y "no", lo que nos da la capacidad de tomar 
decisiones más sofisticadas dentro de nuestros programas.
"""

# Se solicita por consola que se ingresen dos valores (Si/No) para covnertirlas a expresiones booleanas.
expresion1 = input("Ingresa un valor (Si/No): ")
expresion2 = input("Ingresa otro valor (Si/No): ")

# Las cadenas se convierten a expresiones booleanas (ver Fundamentos-Python -> Entrada_conversiones.py).
expresion1 = expresion1.lower() == "si"
expresion2 = expresion2.lower() == "si"

# Se imprimen mensajes sobre operaciones lógicas.
print(f"¿Ambas expresiones fueron 'si'? {expresion1 and expresion2}")
print(f"¿Alguna expresión fue 'si'? {expresion1 or expresion2}")
print(f"Lo contrario de la primera expresión es: {not expresion1}")
print(f"Lo contrario de la segundo expresión es: {not expresion2}")

"""
➡️ Ahora para comprender mejor como funcionan realizamos un ejemplo el cual voy a desglozar a como yo entendí

cad_1 = input("Ingrese si/no: ") ➡️ Le pido al usuario que me digite un si o un no
cad_2 = input("Ingrese si/no: ")

cad_1 = cad_1.lower() == "si" ➡️ Ahora lo convierto a bool con la ayuda del ".lower()" ya que con eso solo si me 
ingresan "si" me dará como salida "TRUE"
cad_2 = cad_2.lower() == "si" ➡️ Hago lo mismo con la cadena dos

print(f" La expresion uno es {cad_1}") ➡️ Posteriormente, lo imprimo en la pantalla para así ver si el tipo de dato
que el usuario ingreso es "TRUE" o "FALSE"
print(f" La expresion dos es {cad_2}")
print()
print(f"¿Ambos fueron si?: {cad_1 and cad_2}")
print()
print(f"¿Ambos fueron si?: {cad_1 or cad_2}")
print()
print(f"¿Ambos fueron si?: {not cad_1}")
print(f"¿Ambos fueron si?: {not cad_2}")
"""