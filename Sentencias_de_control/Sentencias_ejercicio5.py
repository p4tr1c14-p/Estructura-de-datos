'''
Nombre: Patricia Pérez Cruz
Fecha: 26 de octubre de 2024
Descripción: Este programa determinará el promedio de una materia e indicará si el alumno aprobó o no la materia.
Uso de la sentencia de control if - else
'''
#⬆️ Como solo son dos condiciones utilizaré la sentencia de control if - else

print("*** Programa para calcular el promedio de una materia ***")

# a) Solicitar al usuario sus tres calificaciones parciales y la calificación del ordinario.
calificacion1 = float(input("Ingrese la calificación del primer parcial: "))
calificacion2 = float(input("Ingrese la calificación del segundo parcial: "))
calificacion3 = float(input("Ingrese la calificación del tercer parcial: "))
calificacion_ordinario = float(input("Ingrese la calificación del examen ordinario: "))

# b) Calcular el promedio y determinar si aprobó (calificación mínima de 6.0).
# Calcular el promedio: los parciales (50%) y el ordinario (50%) como en la vida real.
promedio_parciales = (calificacion1 + calificacion2 + calificacion3) / 3
promedio_final = (promedio_parciales * 0.5) + (calificacion_ordinario * 0.5)

# c) Mostrar el promedio y el mensaje correspondiente.

if promedio_final >= 6.0: #➡️ Si su calificación fue mayor o igual a 6 entra en este bloque
    print(f"Tu promedio es: {promedio_final:.1f}. ¡Felicidades! Aprobaste.")
else:
    print(f"Tu promedio es: {promedio_final:.1f}. Lo siento, no aprobaste.") #➡️ Si llego a este bloque quiere decir que no aprobo

#d) Muestre el promedio (utilizando un decimal) y el mensaje: "¡Felicidades! Aprobaste.", o el mensaje: "Lo siento, no aprobaste.", según sea el caso.
#⬆️ Los comentarios los mostraré en el print dependiendo de qué condición se haya cumplido
