'''
Nombre:Patricia Pérez Cruz
Fecha: 24 de octubre de 2024
Descripción:
Ejercicio para poner en práctica mis conocimientos adquiridos sobre
los operadores lógicos
'''

print(" *** SISTEMA DE BONIFICACIÓN *** ")

#a) Solicite al usuario un número decimal con el valor de una compra.
cantidad = input("¿Compras mayores a $5,000.00? Ingrese su cantidad con decimales: ")

#b) Pregunte al usuario si la compra fue a MSI (Si/No).
cadena = input("¿Compras a MSI? (si/no): ")

total = float(cantidad) #➡️ Convertí a float
cadena = cadena.lower() == "si" #➡️ Aquí con solo esta línea de código logré convertir esto a booleano

#c) El usuario aplica a la bonificación si la compra fue mayor a 5000.00 y si la compra fue a MSI.
#Lo anterior lo voy a comprobar con la comparación (la cual es: var_bool>5000 and cadena) que haré dentro del print

#d) Muestre el resultado en consola como valor booleano (True/False).
print(f"¿Aplica bonificación?: {total>=5000 and cadena}") #➡️ Aquí comparo que las dos condiciones se deben de cumplir
#para que así me de "TRUE"