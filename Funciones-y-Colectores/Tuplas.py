print("*** Ejemplo de tuplas ***")

#fechas_cumple= ('12-19', '12-27', '01-10', '10-18', '11-01', '09-30', '08-25', '01-06', '10-21',  '04-11', '03-06', '08-02')
#print(fechas_cumple)

pi_serie= (4, -4/3, 4/5, -4/7, 4/9, -4/11, 4/13, -4/15, 4/17, -4/19, 4/21, -4/23)


print(f" La suma de los 3 primeros es de: {sum(pi_serie[0:2])}")
print(f" La suma de los 5 primeros es de: {sum(pi_serie[0:4])}")
print(f" La suma de los 8 primeros es de: {sum(pi_serie[0:7])}")
print(f" La suma de los 10 primeros es de: {sum(pi_serie[0:9])}")
print(f" La suma de todos es de: {sum(pi_serie)}")

print()
print("*** Ejemplo con coordenadas ***")
punto1= (1,0)
punto2= (5,3)

#punto1[0]= 2
#punto1.append(2)


print(f"Coordenas en tuplas: {punto1}{punto2}")
x1, y1= punto1
x2, y2= punto2

print()
print("---------------------------------------")
pendiente = (y2-y1)/(x2-x1)
b = y1 - pendiente * x1
print(f"La ecuación de la recta es: y = {pendiente}x {b}")

"""for i in fechas_cumple:
    print(i, end= ' ')"""

'''
Nombre:
Fecha:
Descripción:
Ejemplos de uso de las Tuplas.
'''

"""
Una tupla es una colección ordenada e inmutable de elementos. Esto significa que:
 - Ordenada: Los elementos se almacenan en un orden específico, y cada elemento tiene un índice asociado.
 - Inmutable: Una vez creada, no se puede agregar, eliminar o cambiar elementos dentro de una tupla.
 - Heterogénea: Una tupla puede contener elementos de diferentes tipos de datos.

Sintaxis para crear una lista:
Se encierra los elementos entre paréntesis () y se separan por comas. 
Nota: el uso de los paréntesis es opcional.

"""

# Primer ejemplo de una tupla
print("  ***  Ejemplo de uso de una Tupla  ***")
fechas_nacimiento = ("2019-10-01", "2020-10-01", "2020-12-01", "2021-06-12", "2022-10-01", "2023-11-01")

print(f"Ejemplo de tupla: {fechas_nacimiento}")     # Se imprime toda la tupla.

print("Se imprime la tupla elemento por elemento:")
for fecha in fechas_nacimiento:     # Se imprime un elemento individual, de la misma forma que con ua lista.
    print(f"{fecha}", end = ", ")

print()
print()


# Ejemplo con la serie de Pi de Leibniz
print("  ***  Serie de pi de Leibniz  ***")

pi_serie = (4, -4/3, 4/5, -4/7, 4/9, -4/11, 4/13, -4/15, 4/17, -4/19, 4/21, -4/23)
print(f"Serie de Leibniz: {pi_serie}")

# La función sum() suma los elementos del parámetro que recibe.
print(f"El número Pi considerando los primeros 3 elementos es: {sum(pi_serie[0:2])}")
print(f"El número Pi considerando los primeros 5 elementos es: {sum(pi_serie[0:4])}")
print(f"El número Pi considerando los primeros 9 elementos es: {sum(pi_serie[0:8])}")
print(f"El número Pi considerando todos los elementos ({len(pi_serie)}) es: {sum(pi_serie)}")
print()


# Ejemplo con coordenadas.
print("  ***  Coordenadas con tuplas  ***")
punto1 = (1, 0)
punto2 = (5, 3)

print(f"Coordenadas en tupla (x, y): {punto1} y {punto2}")

# Desempaquetado de tuplas. Se asignan los valores de la tupla a varias variables.
# En este caso, para calcular una expresión de la recta.
x1, y1 = punto1
x2, y2 = punto2

# Se calcula la pendiente y el offset de la recta.
pendiente = (y2 - y1)/(x2 - x1)
b = y1 - pendiente*x1

print(f"Expresión de la recta: y = {pendiente}*x + {b}")

'''
Nombre:
Fecha:
Descripción:
Ejemplos del uso de una tupla dentro de una función.
'''

""" Función que recibe una tupla con las calificaciones del semestre (tres calificaciones parciales y ordinario)
    y devuelve una tupla con el promedio de los parciales, el promedio final y si está aprobado """
def determinar_promedio(calificaciones):
    # Se calculan los promedios y se determina si está aprobado (promedio final mayor o igual a 6).
    promedio_parcial = sum(calificaciones[0:3])/len(calificaciones[0:3])
    promedio_final = (promedio_parcial + calificaciones[3])/2
    esta_aprobado = promedio_final >= 6

    # Regresa los valores en forma de una tupla. Nota: recordar que no se requiere el uso de paréntesis.
    return promedio_parcial, promedio_final, esta_aprobado


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
print("  ***  Programa que determina el promedio utilizando funcioens y tuplas  ***")

# Se solicitan las calificaciones de los parciales y ordinario.
parcial1 = float(input("Ingresa la calificación del Parcial 1: ").strip())
parcial2 = float(input("Ingresa la calificación del Parcial 2: ").strip())
parcial3 = float(input("Ingresa la calificación del Parcial 3: ").strip())
ordinario = float(input("Ingresa la calificación del Ordinario: ").strip())
print()

# Se crea una tupla
calificaciones = (parcial1, parcial2, parcial3, ordinario)
print(calificaciones)
# Se utiliza la función para calcular los promedios y determinar si está o no aprobado.
# Para ello, se utiliza el desempaquetado de tuplas.
promedio_parcial, promedio_final, esta_aprobado = determinar_promedio(calificaciones)

if esta_aprobado:
    print("Felicidades, aprobaste!", end = " ")
else:
    print("Lo siento, no aprobaste.", end = " ")

print(f"El promedio de los parciales es: {promedio_parcial:.1f} y el promedio final es: {promedio_final:.1f}.")