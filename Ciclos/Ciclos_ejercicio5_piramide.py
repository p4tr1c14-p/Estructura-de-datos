fila = int(input("Ingrese el número de filas que desee: "))
filauno = fila
contador = fila

print("Primer triángulo")
for i in range(1, filauno + 1) :
    asteriscos1 = " * " * i
    print(f" {asteriscos1}")

print()
print("Segundo triángulo")
for x in range(1, fila + 1) :
    asteriscos2 = " * " * fila
    fila = fila - 1
    print(f" {asteriscos2}")
print()
print()
print()
print("Tercer triángulo")
for z in range(1, fila + 1) :
    espacio = " " * z
    asteriscos3 = "*" * contador
    print(f" {espacio}{asteriscos3}")
    contador -= 1


