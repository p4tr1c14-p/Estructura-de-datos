'''
Nombre: Patricia Pérez Cruz
Fecha: 21 de noviembre de 2024
Descripción:
Este programa es una playlist de videos de Youtube.
'''

print(" *** Videos favoritos de YT ***")
print()

lista = []
opcion = None
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

    if opcion == 1: #➡️ Mostrar lista de videos añadidos
        if len(lista) == 0: #➡️ Esto es para ver si la lista ya tiene algo o no
            print("La lista esta vacia")
            print()
        else:
            print(lista)
        print("------------------------------")
        print()
    elif opcion == 2: #➡️ Ordenar y mostrar lista de videos de A-Z
        if len(lista) == 0:
            print("La lista esta vacia")
            print()
        else:
            lista.sort()  #➡️ .sort() ordena la lista en orden ascendente
            for i in lista:
                print(i)
            print("------------------------------")
            print()
    elif opcion == 3: #➡️ Ordenar y mostrar lista de videos de Z-A
        if len(lista) == 0:
            print("La lista esta vacia")
            print()
        else:
            lista.sort(reverse=True) #➡️ Con reverse=True hago que salga a lo contrario del abecedario
            for x in lista:
                print(x)
            print("------------------------------")
            print()
    elif opcion == 4:
        variable = input("Ingrese su nuevo video: ")
        lista.append(variable)  #➡️ Agrega el video al final de la lista
        print("------------------------------")
        print()
    elif opcion == 5: #➡️ Añadir un video
        variables = int(input("Ingrese cuantos videos desea ingresar: ")) #➡️ Ocupe esta variable para iterar las veces que el usuario quiera
        i = 1
        while i <= variables:
            ingresar = input("Ingrese su nuevo video: ")
            lista.insert(-1, ingresar)
            i= i + 1
        print("------------------------------")
        print()
    elif opcion == 6: #➡️ Eliminar un video
        if len(lista) == 0:
            print("La lista esta vacia")
            print()
        else:
            borrar = input("Ingrese el video a borrar: ")
            lista.remove(borrar)
            print("Video eliminado correctamente")
        print()
print("Adiós 🤩")