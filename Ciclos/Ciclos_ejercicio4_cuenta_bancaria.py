'''
Nombre: Patricia Pérez Cruz
Fecha: 29 de octubre de 2024
Descripción: Este programa es un ejercicio sobre los ciclos while
'''
print("*** Bienvenido a Banco Azteca ***")

opciones = None #➡️ Aplique mis nuevos conocimientos adquridos con respecto a la inicialización de este tipo de variables que uso en mis condiciones
saldo = 0 #➡️ Inicialicé saldo en cero para que no tenga nada
while opciones != 0:
    print("Bienvenido al menú de Banco Azteca 😎")
    print("0) Salir.")
    print("1) Consultar saldo.")
    print("2) Ingresar dinero.")
    print("3) Retira dinero.")
    opciones = int(input("Ingrese su selección: ")) #➡️ Recibo la opción elegida por el usuario y la convierto a entero

    if opciones == 1:
        print(f"Su saldo es de: {saldo:.2f}") #➡️ Imprimo el saldo con dos décimales
        print()
    elif opciones == 2:
        money = float(input("Ingrese la canidad a depositar: ")) #➡️ Convierto a décimal
        saldo = saldo + money #➡️ Le asigno la nueva cantidad a mi variable que va a almacenar el saldo en este caso
        print("Dinero depositado correctamente 🤑")
        print()
    elif opciones == 3:
        sacar = float(input("Ingrese la canidad a retirar: ")) #➡️ Solicito la cantidad a retirar
        if sacar > saldo: #➡️ Condición para saber si hay suficiente saldo para retirar
            print("Dinero insuficiente trabaje! ")
            print()
        else:
            saldo = saldo - sacar #➡️ Le resto el dinero que se solicito retirar
            print("Dinero retirado correctamente 🤑")
            print()
    elif opciones > 0:
        print("Opción inválida") #➡️ Si la opción elegida por el usuario es mayor a cero significa que es una opción inválida
        print()
    else:
        print("Saliendo...") #➡️ De lo contrario si es cero termina mi programa
print("Gracias por usar mi programa 😎")