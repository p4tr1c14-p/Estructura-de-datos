'''
Nombre:Patricia Pérez Cruz
Fecha: 24 de octubre de 2024
Descripción:
Segundo ejercicio para poner en práctica mis conocimientos adquiridos sobre
los operadores lógicos
'''

print(" *** COMUNIDAD DE LA UNSIJ ***")

#a) Pregunte al usuario si es profesor de la UNSIJ (Si/No).
profesor = input("Es profesor de la UNSIJ (si/no): ")

#b) Pregunte al usuario si es alumno de la UNSIJ (Si/No).
alumno = input("Es alumno de la UNSIJ (si/no): ")

profesor = profesor.lower() == "si" #➡️ Convertí a booleano
alumno = alumno.lower() == "si" #➡️ Convertí a booleano

#c) La persona forma parte de la UNSIJ si es profesor o alumno de la UNSIJ. ➡️ La comparación la haré dentro del print

#d) Muestre el resultado en consola como valor booleano (True/False).
print(f"Forma parte de la UNSIJ?: {profesor or alumno}") #➡️ La comparación fue con el "or" ya que no importa si es
#alumno o profesor al final sigue siendo parte de la UNSIJ 😀