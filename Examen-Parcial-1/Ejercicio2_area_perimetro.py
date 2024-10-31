PI = 3.1416 #➡️ Define una constante para el valor de pi
opcion = -1 #➡️ Inicialicé la variable opcion con un valor distinto de 0 para poder entrar en el ciclo
while opcion != 0: #➡️ Este ciclo se repetirá mientras la opción seleccionada no sea 0
    print("\nMenú:")
    print("1) Calcular el área de un rectángulo.")
    print("2) Calcular el perímetro de un rectángulo.")
    print("3) Calcular el área de un círculo.")
    print("4) Calcular el perímetro de un círculo.")
    print("0) Salir.")

    opcion = int(input("Seleccione una opción: ")) #➡️ Solicité al usuario que seleccione una opción del menú

    if opcion == 1: #➡️ Si la opción es 1, calculo el área del rectángulo
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        area = base * altura
        print(f"Área del rectángulo: {area:.3f}")
        print("------------------------------------------")
    #➡️ Si la opción es 2, calculo el perímetro del rectángulo
    elif opcion == 2:
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        perimetro = 2 * (base + altura)
        print(f"Perímetro del rectángulo: {perimetro:.3f}")
        print("------------------------------------------")
    #➡️ Si la opción es 3, calculo el área del círculo
    elif opcion == 3:
        radio = float(input("Ingrese el radio del círculo: "))
        area = PI * (radio ** 2)
        print(f"Área del círculo: {area:.3f}")
        print("------------------------------------------")
    #➡️ Si la opción es 4, calculo el perímetro del círculo
    elif opcion == 4:
        radio = float(input("Ingrese el radio del círculo: "))
        perimetro = 2 * PI * radio
        print(f"Perímetro del círculo: {perimetro:.3f}")
        print("------------------------------------------")
    #➡️ Si la opción es 0 termina mi programa
    elif opcion == 0:
        print("Saliendo....")
        print("------------------------------------------")
    else:
        print("Opción no válida 😓")
        print("------------------------------------------")