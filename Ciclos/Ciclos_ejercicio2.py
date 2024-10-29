'''
Nombre: Patricia Pérez Cruz
Fecha: 28 de octubre de 2024
Descripción: Este programa es un ejercicio sobre los ciclos while
'''
print("*** Progrma que calcula la suma acumulativa entre 2 números ***")

numero_inicial = int(input("Ingrese su número inical: "))
numero_final = int(input("Ingrese su número final: "))

print(f"La suma de {numero_inicial} hasta {numero_final} es: ")

suma = 0

while numero_inicial <= numero_final:
    suma += numero_inicial
    numero_inicial += 1

print(suma)
print("Fin de suma")
