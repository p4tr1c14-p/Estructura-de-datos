
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
➡️ Los siguientes operadores aritméticos ya los conicía
 + SUMA
 - RESTA
 * MULTIPLICACIÓN
 / DIVISIÓN
 % MODULO
 
 ➡️ Pero estos dos fueron nuevos para mi 😀
 // DIVISIÓN QUE SOLO ME DA EL RESULTADO ENTERO
 ** ES PARA ELEVAR A UN NÚMERO (FUNCIONA COMO ESTE SIMBOLO "^")
"""

