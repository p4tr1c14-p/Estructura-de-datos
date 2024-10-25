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
valor_uno = input("Ingrese si o no: ")
valor_dos = input("Ingrese si o no: ")
valor_tres = input("Ingrese si o no: ")
valor_cuatro = input("Ingrese si o no: ")

#b) Obtenga el resultado de la expresión booleana de acuerdo con los valores ingresados.
valor_one = valor_uno.lower() == "si"
valor_two = valor_dos.lower() == "si"
valor_three = valor_tres.lower() == "si"
valor_four = valor_cuatro.lower() == "si"


"""
Este programa determinará True o False de acuerdo a la expresión (exp1 O exp2) Y (exp3 O exp4). Para ello:

a) Pida al usuario cuatro valores booleanos (V/F).

b) Obtenga el resultado de la expresión booleana de acuerdo con los valores ingresados.

c) Muestre el resultado en consola como valor booleano (True/False).
"""