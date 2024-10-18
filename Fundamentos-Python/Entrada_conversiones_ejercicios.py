"""
Alumna: Patricia Pérez Cruz
Fecha: 18 de octubre de 2024
Mi segundo ejercicio usando el input y el casting

Entrada_conversiones_ejercicio.py

Escribe un programa de nombre Entrada_conversiones_ejercicio.py que realice lo siguiente:

a) Pida los datos de los profesores utilizando nombres de variables adecuadas, la función input y el casting:
Nombre (cadena).
No. de cubículo (int).
Horas de que imparte clase a la semana (float con 3 decimales).
¿Tiene más de 5 años en la unsij? (booleno).
"""

print()
cadena = input("Ingrese su nombre: ")
cubo = input("Ingrese su número de cubo (con números): ")
horas = input("Ingrese su número de horas que imparte clase a la semana (con 3 decimales): ")
tiempo = input("¿Tiene más de 5 años en la unsij? (si/no): ")

num_cubo = int(cubo)
num_horas = float(horas)
tiempo = tiempo.lower() == "si"


"""
b) Muestre los datos en consola de forma adecuada.

Nota: Asuma que el usuario siempre va a ingresar números cuando se requiera.

"""

print()
print(f"Su nombre es: {cadena}")
print(f"No. de cubo: {num_cubo}")
print(f"Las horas de que imparte clase a la semana es: {num_horas}")
print(f" ¿Tiene más de 5 años en la unsij? {tiempo}")