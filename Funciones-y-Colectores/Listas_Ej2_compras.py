print(" *** Lista de compras *** ")
opcion = -1
lista = []
cesta = []
def menu():
    print("Bienvenido a mi menú 😉")
    print("1) Ver lista")
    print("2) Añadir producto a la lista")
    print("3) Eliminar producto de la lista")
    print("0) Salir")
    opcion = int(input("Ingrese su selección: "))
    return opcion


while opcion != 0:
    opcion = menu()
    if opcion == 1:
        print(lista)
        print("------------------------------")
        print()
    elif opcion == 2:
        nombre = input("Ingrese el nombre de su producto: ")
        cantidad = input("Ingrese la cantidad de productos: ")
        cesta.append(nombre)
        cesta.append(cantidad)
        lista.append(cesta)
        print("------------------------------")
        print()
    elif opcion == 3:
        borrar = int(input("Eliminar podructo de la lista: "))
        lista, cesta.pop(borrar)
        #lista.pop(borrar + 1)

