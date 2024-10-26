'''
Nombre:Patricia Pérez Cruz
Fecha: 25 de octubre de 2024
Descripción:
Cuarto ejercicio para poner en práctica mis conocimientos adquiridos sobre
los operadores lógicos.
Este programa determinará True o False de acuerdo a la expresión (exp1 O exp2) Y (exp3 O exp4).
'''

print(" *** Expresión booleana (exp1 O exp2) Y (exp3 O exp4) ***")
print()
#a) Pida al usuario cuatro valores booleanos (V/F).
valor_uno = input("Ingrese si o no: ") #➡️ Aquí solicito si o no (El "si" para mí es mi "V" y el "no" es mi "F")
valor_dos = input("Ingrese si o no: ")
valor_tres = input("Ingrese si o no: ")
valor_cuatro = input("Ingrese si o no: ")

#b) Obtenga el resultado de la expresión booleana de acuerdo con los valores ingresados.
valor_one = valor_uno.lower() == "si" #➡️ Convierto la cadena de antes a minúsculas y las comparo para que, si es otro valor que no sea  "si", me dé "FALSE"
valor_two = valor_dos.lower() == "si"
valor_three = valor_tres.lower() == "si"
valor_four = valor_cuatro.lower() == "si"

#c) Muestre el resultado en consola como valor booleano (True/False).

expresion_uno = valor_one or valor_two #➡️ Primero lo comparo con un or
expresion_dos = valor_three or valor_four

print(f"El resultado de la expresión boolena es: {expresion_uno and expresion_dos}") #➡️ Aquí ya lo comparo con un and

