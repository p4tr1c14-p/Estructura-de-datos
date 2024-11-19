print(" * Lista de compras * ")
opcion = None
lista = []
contador = 0
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
            num = 0
            for producto in lista:
                print(f"{num}) {producto[0]} -- Cantidad: {producto[1]}")
                num = num + 1
        else:
            print("La lista está vacía")
        print("------------------------------")
        print()
    elif opcion == 2:
        nombre = input("Ingrese el nombre de su producto: ")
        cantidad = input("Ingrese la cantidad de productos: ")
        lista.append([nombre, cantidad])
        contador = contador + 1
        #print(contador)
        print("------------------------------")
        print()
    elif opcion == 3:
        print("Lista previa...")
        cont = 0
        for producto in lista:
            print(f"{cont}) {producto[0]} -- Cantidad: {producto[1]}")
            cont = cont + 1
        borrar = int(input("Ingrese el número del producto a eliminar: "))
        if borrar > contador:
            print(f"No hay {contador} productos 🧐")
            print("------------------------------")
            print()
        else:
            borrar = borrar
            lista.pop(borrar)
            contador = contador - 1
            #print(contador)
            print("Producto eliminado correctamente.")


print("Gracias por usar el programa 😊")