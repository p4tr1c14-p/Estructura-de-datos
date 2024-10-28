print("*** Progrma que calcula la suma acumulativa ***")

numero = int(input("Ingrese el número final: "))
print(f"La suma de 0 hasta {numero} es: ")

suma = 0
ayuda = 0

while ayuda <= numero:
    suma += ayuda
    ayuda += 1

print(suma)
print("Fin de suma")
