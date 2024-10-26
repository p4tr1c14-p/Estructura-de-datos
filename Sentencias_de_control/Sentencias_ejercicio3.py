'''
Nombre: Patricia Pérez Cruz
Fecha: 26 de octubre de 2024
Descripción: Este programa determinará un descuento en compras en "La cona"
Uso de la sentencia de control if - else
'''

print("*** Descuentos por ser miembros de 'La cona' ***")

#a) Solicite al usuario la cantidad comprada en la tienda.
total = float(input("Ingrese la cantidad comprada: "))

#b) Pregunte al usuario si cuenta con la membresía (Si/No).
membresia = input("¿Cuenta con la membresía? (Si/No) : ")
membresia = membresia.lower() == "si"
#c) Utilice la lógica adecuada para determinar el total a pagar. ➡️ En este caso utilizaré la sentencia de control if - else
# ya que no son tantas opciones y será fácil con el uso de "if-else"

#d) Muestre el descuento y el total a pagar en consola utilizando dos decimales.
#⬆️ Lo anteriormente mencionado lo iré mostrando conforme entre en las condiciones

if membresia:
    if total >= 1000:
        descuento = (total * 8)/100 #➡️ Calculé el descuento
        total_a_pagar = total - descuento #➡️ Apliqué el descuento restándolo del total a pagar
        print("Tu descuento es del 8 %.")
        print(f"El total es de: {total_a_pagar:.2f}")
    else:
        descuento = (total * 5)/100 #➡️ Calculé el descuento
        total_a_pagar = total - descuento #➡️ Apliqué el descuento restándolo del total a pagar
        print("Tu descuento es del 5 %.")
        print(f"El total es de: {total_a_pagar:.2f}")
else: #➡️ En caso de que ninguna de las condiciones anteriores se cumpla, se imprimirá el siguiente mensaje
    print("Se te invita a ser miembro de la tienda para obtener un descuento de hasta el 8 %.")
    print(f"El total es de: {total:.2f}")