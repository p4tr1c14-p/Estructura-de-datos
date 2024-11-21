'''
Nombre: Patricia Pérez Cruz
Fecha: 28 de octubre de 2024
Descripción: Este programa es un ejercicio sobre los ciclos while
'''
print("*** Programa que calcula la suma acumulativa ***")

numero = int(input("Ingrese el número final: ")) #➡️ Ingreso un número y convertirlo a entero
suma = 0
ayuda = 0

while ayuda <= numero: #➡️ Mientras mi contador que es ayuda no llegue hasta el número que es mi paro se seguirá haceindo la suma
    suma += ayuda
    ayuda += 1

print(f"La suma de 0 hasta {numero} es: {suma}") #➡️ Imprimo un cartel que avisa hasta que número hará la suma acumulativa y el resultado
print("Fin de suma")