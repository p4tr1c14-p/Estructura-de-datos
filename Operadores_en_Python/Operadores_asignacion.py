'''
Nombre: Patricia Pérez Cruz
Fecha: 26 de octubre de 2024
Descripción:
Ejemplos de uso de los operadores de asignación.
'''

"""
En programación, las operaciones de asignación se utilizan para almacenar un valor en una variable. 
Es decir, se establece una relación entre un nombre (la variable) y un valor en la memoria de la computadora.
"""

# Asignación múltiple.
print("   ***   Asignación múltiple   ***")
nombre, primer_apellido, segundo_apellido = "Patricia", "Pérez", "Cruz"  #➡️ Asignamos múltiples cadenas en una sola línea
print(f"Asignación múltiple de cadenas: {nombre} {primer_apellido} {segundo_apellido}")

entero1, entero2 = 1, 2  #➡️ Asignación múltiple de enteros
print(f"Asignación múltiple de enteros: {entero1} y {entero2}")

decimal1, decimal2, decimal3, decimal4 = 3.14, 3.1416, 3.14159, 3.141592 #➡️ Asignación múltiple de decimales
print(f"Asignación múltiple de decimales: {decimal1}, {decimal2}, {decimal3} y {decimal4}")

#➡️ Es posible combinar diferentes tipos de datos en una sola asignación múltiple
nombre, entero1, decimal4 = "Patricia", 12, 3.1415926            # Es posible combinar tipos de datos.
print(f"Asignación múltiple: {nombre}, {entero1} y {decimal4}")

#➡️ Se pueden asignar resultados de operaciones a variables en una sola línea
suma, resta = entero1 + entero2, decimal1 - decimal2            # Es posible asignar distintas operaciones.
print(f"Asignaciones de operaciones: suma {suma} y resta {resta:.4f}")


# Asignación encadenada.
print()
print("   ***   Asignación encadenada   ***")

#➡️ Se les asigna el mismo valor a varias variables en una sola línea
entero3 = entero4 = entero5 = 10    # Se les asigna el mismo valor a todas las variables.
print(f"Asignación encadenada de: {entero3} = {entero4} = {entero5} = 10")


# Intercambio de variables.
print()
print("   ***   Intercambio de variables   ***")


entero5, entero6 = 5, 6  #➡️ Asignamos valores iniciales a entero5 y entero6
print(f"Valores asignados: entero5 = {entero5} y entero6 = {entero6}")
entero6, entero5 = entero5, entero6  #➡️ Se intercambian los valores de entero5 y entero6 utilizando una asignación múltiple
print(f"Valores intercambiados: entero5 = {entero5} y entero6 = {entero6}")

variable_prueba1, variable_prueba2 = 100, "Hola mundo"
variable_prueba1, variable_prueba2 = variable_prueba2, variable_prueba1 # Es posible porque las variables son dinámicas.
print(f"Valores asignados: variable_prueba1 = {variable_prueba1} y variable_prueba2 = {variable_prueba2}")
print(f"Valores intercambiados: variable_prueba1 = {variable_prueba1} y variable_prueba2 = {variable_prueba2}")


"""
Ejercicio realizado en clase para complementar los conocimientos adquiridos anteriormente:

print("*** ASIGNACIÓN ENCADENADA ***")
print()

v1,v2 = 5,10
print(v1,v2)

v3, v4 = 9.14, "Chuy"
print(v3,v4)

v5,v6 = v1 + v2, v1-v2
print(v5,v6)

v7 = v8=v9=10
print(v7)
print(v8)
print(v9)

v10, v11 = "Alberto", "Geto"
print(v10, v11)

v11,v10 = v10, v11
print(v10, v11)

nombre,apellido = input("Ingrese nombre: "), input("Ingrese apellido: ")
print(nombre,apellido)
"""

"""
📎Mini notas:
La asignación múltiple permite escribir menos líneas de código y agrupar la inicialización de variables relacionadas
La asignación encadenada es útil para inicializar varias variables con el mismo valor
El intercambio de variables es una técnica común y permite cambiar los valores de dos variables sin usar una variable temporal
Python permite la asignación de diferentes tipos de datos a una misma variable 👍
"""