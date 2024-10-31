"""
Patricia Pérez Cruz
31 de octubre de 2024.
Descripción:
Este programa imprime en consola los números, separados por comas, del 1 hasta un número ingresado por el usuario.
"""

print("*** Licenciatura en Informática ***")

#a) Solicite un número en consola.
numero_final = int(input("Ingrese el número final de la cuenta: "))

#b) Realizar la lógica adecuada para imprimir los números o mensajes adecuados.
#c) Mostrar los resultados en consola.
#⬆️ Lo iré imprimiendo conforme se vayan cumpliendo las condiciones
aux = 1
while aux <= numero_final:
    if aux % 3 == 0 and aux % 5 == 0:
        print("Licenciatura en Informática", end=" ")
        print()
    elif aux % 3 == 0:
        print("Licenciatura,", end=" ")
    elif aux % 5 == 0:
        print("Informática", end=" ")
    else:
        print(aux, end=", ")
    aux += 1

print()

