'''
Nombre: Patricia Pérez Cruz
Fecha: 26 de octubre de 2024
Descripción: Este programa determinará el promedio de una materia e indicará si el alumno aprobó o no la materia.
Uso de la sentencia de control if - else
'''


print("*** Tour turístico Ecoturixtlán ***")

# a) Solicitar el nombre de la persona a cargo.
nombre_persona = input("Ingrese el nombre de la persona a cargo: ")

# b) Definir con valores constantes el precio del boleto del adulto y del niño.
PRECIO_ADULTO = 200.00 #➡️ Declaro las constantes
PRECIO_NINO = 100.00 #➡️ Declaro las constantes

# c) Solicitar el número de adultos y de niños.
num_adultos = int(input("Ingrese el número de adultos: "))  #➡️ Convertí a entero
num_ninos = int(input("Ingrese el número de niños: ")) #➡️ Convertí a entero

# d) Preguntar el día de la semana.
dia_semana = input("Ingrese el día de la semana: ") #➡️ Pregunto el día de la semana para saber si aplica a un descuento

# e) Calcular el costo total.
costo_total = (num_adultos * PRECIO_ADULTO) + (num_ninos * PRECIO_NINO) #➡️ Calculo el costo total

# Verificar si hay descuento
if dia_semana == "lunes" or dia_semana == "martes" or dia_semana == "jueves": #➡️ Si es uno de estos días aplica al descuento
    costo_total *= 0.9  # Aplicar descuento del 10%
# f) Mostrar los detalles del cliente, el día y el costo total.
print(f"Gracias por tu visita {nombre_persona} este día {dia_semana}. El costo total es {costo_total:.2f}")