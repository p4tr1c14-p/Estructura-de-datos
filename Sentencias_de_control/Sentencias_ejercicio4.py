'''
Nombre: Patricia Pérez Cruz
Fecha: 26 de octubre de 2024
Descripción: Este programa determinará si te permiten el acceso al bar "La Negra"
Uso de la sentencia de control if - else
'''

print("*** Acceso al bar 'La negra' ***")

#a) Solicite al usuario su edad.
edad = int(input("Ingrese su edad: ")) #➡️ Convertí la edad a entero

#b) Solicite al usuario el dinero con el que cuenta.
presupuesto = float(input("Ingrese su presupuesto: ")) #➡️ Convertí su presupuesto a flotante


#c) Utilice la lógica adecuada para determinar el mensaje.
#⬆️ Como solo son dos condiciones utilizaré la sentencia de control if - else

#d) Muestre el mensaje adecuado en consola. ➡️ Los mensajes se imprimirán cuando se cumplan o no las condiciones
if edad >= 18 and presupuesto >= 250:
    print("¡Bienvenido a tu mejor bar!")
else:
    print("Lo sentimos, ya estamos por cerrar!")
