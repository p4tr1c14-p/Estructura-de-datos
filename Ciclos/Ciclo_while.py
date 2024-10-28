"""
print("*** Progrma que me imprime un ejemplo dke ciclo while ***")
numero = int(input("Ingrese un número: "))
print(f"Los números de 1 al {numero} son: ")
auxiliar = 1
while auxiliar <= numero:
    print(auxiliar,end= " " )
    auxiliar += 1
print()
print("Fin de cuenta")
"""

print("*** Progrma que me imprime los números pares ***")

numero = int(input("Ingrese un número: "))
print(f"Los números pares del 1 al {numero} son: ")
auxiliar = 1
while auxiliar <= numero:
    if auxiliar % 2 == 0:
        print(auxiliar,end= " ")
    auxiliar += 1
print()
print("Fin de cuenta")