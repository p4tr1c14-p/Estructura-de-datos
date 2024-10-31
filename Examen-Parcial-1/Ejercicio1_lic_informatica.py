"""
Escribe un programa de nombre Ejercicio1_lic_informatica.py y sube el enlace de GitHub.

Este programa imprime en consola los números, separados por comas, del 1 hasta un número ingresado por el usuario.

Sin embargo, se deben sustituir los siguientes valores:

3 o sus múltiplos por la palabra "Licenciatura".
5 y sus múltiplos por la palabra "Informática".
Múltiplos de 3 y 5 por la frase "Licenciatura en Informática" y se imprima un salto de línea en lugar de la coma.

Para ello:

a) Solicite un número en consola.

b) Realizar la lógica adecuada para imprimir los números o mensajes adecuados.

c) Mostrar los resultados en consola.

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

