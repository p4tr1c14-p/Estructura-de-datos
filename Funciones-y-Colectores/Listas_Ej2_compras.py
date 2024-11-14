print(" *** Lista de compras *** ")

opcion = -1
lista = []

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
        if lista:
            print("Lista de compras:")
            for producto in lista:
                print(f"{producto[0]} - Cantidad: {producto[1]}")
        else:
            print("La lista está vacía.")
        print("------------------------------")
        print()
    elif opcion == 2:
        nombre = input("Ingrese el nombre de su producto: ")
        cantidad = input("Ingrese la cantidad de productos: ")
        lista.append([nombre, cantidad])
        print("------------------------------")
        print()
    elif opcion == 3:
        print("Lista actual de productos:")
        for idx, producto in enumerate(lista):
            print(f"{idx + 1}) {producto[0]} - Cantidad: {producto[1]}")
        borrar = int(input("Ingrese el número del producto a eliminar: ")) - 1
        if 0 <= borrar < len(lista):
            lista.pop(borrar)
            print("Producto eliminado correctamente.")
        else:
            print("Número inválido.")
        print("------------------------------")
        print()

print("¡Gracias por usar el programa! 😊")
