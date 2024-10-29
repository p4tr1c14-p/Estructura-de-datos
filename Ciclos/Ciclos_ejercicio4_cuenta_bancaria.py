'''
Nombre: Patricia Pérez Cruz
Fecha: 29 de octubre de 2024
Descripción: Este programa es un ejercicio sobre los ciclos while
'''
print("*** Bienvenido a Banco Azteca ***")

opciones = -1
saldo = 0
while opciones != 0:
    print("Bienvenido al menú de Banco Azteca 😎")
    print("0) Salir.")
    print("1) Consultar saldo.")
    print("2) Ingresar dinero.")
    print("3) Retira dinero.")
    opciones = int(input("Ingrese su selección: "))

    if opciones == 1:
        print(f"Su saldo es de: {saldo:.2f}")
        print()
    elif opciones == 2:
        money = float(input("Ingrese la canidad a depositar: "))
        saldo = saldo + money
        print("Dinero depositado correctamente 🤑")
        print()
    elif opciones == 3:
        sacar = float(input("Ingrese la canidad a retirar: "))
        if sacar > saldo:
            print("Dinero insuficiente trabaje! ")
            print()
        else:
            saldo = saldo - sacar
            print("Dinero retirado correctamente 🤑")
            print()
    else:
        print("Opción inválida")
        print()