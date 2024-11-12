print(" *** Videos favoritos de YT ***")
print()

lista = []
opcion = -1
while opcion != 0:
    print("*** Bienvenido a mi mi menú, elige una opción 😎")
    print("1) Ver lista de videos por añadidos")
    print("2) Ver lista por orden A-Z")
    print("3) Ver lista por orden Z-A")
    print("4) Añadir video")
    print("5) Añadir varios videos")
    print("6) Eliminar video")
    print("0) Salir")
    opcion = int(input("Ingrese su opción: "))

    if opcion == 1:
        print(lista)
        print("------------------------------")
        print()
    elif opcion == 2:
        lista.sort()
        for i in lista:
            print(i)
            print("------------------------------")
            print()
    elif opcion == 3:
        lista.sort(reverse=True)
        for x in lista:
            print(x)
            print("------------------------------")
            print()
    elif opcion == 4:
        variable = input("Ingrese su nuevo video: ")
        lista.insert(-1, variable)
        print("------------------------------")
        print()
    elif opcion == 5:
        variables = int(input("Ingrese cuantos videos desea ingresar: "))
        i = 1
        while i <= variables:
            ingresar = input("Ingrese su nuevo video: ")
            lista.insert(-1, ingresar)
            i= i + 1
        print("------------------------------")
        print()
    elif opcion == 6:
        borrar = input("Ingrese el video a borrar")
        lista.remove(borrar)
        print()
print("Adiós 🤩")