'''
Nombre: Patricia Pérez Cruz
Fecha: 26 de octubre de 2024
Descripción: Este programa determinará la estación del año de acuerdo al número de mes ingresado por el usuario
Uso de la sentencia de control if - elif - else
'''
print("*** Programa que determina la estación del año ***")
print()

#a) Solicite al usuario un número que representa al mes.
numero_de_estacion = int(input("Ingrese el número del mes: ")) #➡️ Solicitar un número y convertirlo a "int"

#b) Utilice la lógica adecuada para determinar la estación del año de acuerdo con:
#➡️ En este caso, utilizaré la sentencia de control if - elif - else, ya que hay más de dos opciones y esta estructura me ayudará mucho

#c) Muestre la estación correspondiente en consola. ➡️ Todos los mensajes los imprimiré con print después de que se cumpla alguna condición
if numero_de_estacion == 3 or numero_de_estacion == 4 or numero_de_estacion == 5:
    print("La estación es: Primavera.")
elif numero_de_estacion == 6 or numero_de_estacion == 7 or numero_de_estacion == 8: #➡️ Evaluar condición
    print("La estación es: Verano.")
elif numero_de_estacion == 9 or numero_de_estacion == 10 or numero_de_estacion == 11:
    print("La estación es: Otoño.")
elif numero_de_estacion == 12 or numero_de_estacion == 1 or numero_de_estacion == 2:
    print("La estación es: Invierno.")
else: #➡️ En caso de que ninguna de las condiciones anteriores se cumpla, se imprimirá el siguiente mensaje 😊
    print("Mes incorrecto.")
