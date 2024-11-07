fila = int(input("Ingrese el número de filas que desee: "))
aux = 0

contador = fila
for x in range(1, fila + 1) :
    espacio = " " * x
    asteriscos = "*" * contador
    print(f" {espacio}{asteriscos}")
    contador -= 1