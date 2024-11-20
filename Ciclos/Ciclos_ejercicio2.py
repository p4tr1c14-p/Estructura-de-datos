'''
Nombre: Patricia Pérez Cruz
Fecha: 28 de octubre de 2024
Descripción: Este programa es un ejercicio sobre los ciclos while
'''
print("*** Progrma que calcula la suma acumulativa entre 2 números ***")

numero_inicial = int(input("Ingrese su número inical: ")) #➡️ Solicito el número inicial
numero_final = int(input("Ingrese su número final: ")) #➡️ Solicito el número final

print(f"La suma de {numero_inicial} hasta {numero_final} es: ")
suma = 0 #➡️ Variable donde se guardará la suma acumulativa

while numero_inicial <= numero_final: #➡️ En este caso el número inicial será mi iterador
    suma += numero_inicial #➡️ Aquí le voy sumando
    numero_inicial += 1

print(suma) #➡️ Imprimir el resultado final
print("Fin de suma")
