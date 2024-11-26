'''
Nombre: Patricia Pérez Cruz
Fecha: 21 de noviembre de 2024
Descripción:
Este programa es una lista de compras para el súper.
La lista está conformado por varios productos.
Cada producto tiene un nombre y cantidad, por lo que también se sugiere utilizar una lista.
'''
print(" * Lista de compras * ")
opcion = None
lista = []  #➡️ Mi lista para almacenar los productos
contador = 0  #➡️ Mi contador de productos en la lista

def menu():
    #➡️ Muestra el menú de opciones y devuelve la opción seleccionada
    print("Bienvenido a mi menú 😉")
    print("1) Ver lista")
    print("2) Añadir producto a la lista")
    print("3) Eliminar producto de la lista")
    print("0) Salir")
    opcion = int(input("Ingrese su selección: "))
    return opcion

def ver_lista():
    #➡️ Muestra la lista de productos con sus cantidades
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

def añadir_producto(contador):
    #➡️ Añadí un nuevo producto a la lista y devolví el contador actualizado
    nombre = input("Ingrese el nombre de su producto: ")
    cantidad = input("Ingrese la cantidad de productos: ")
    lista.append([nombre, cantidad])
    contador += 1  #➡️ Incrementa mi contador
    print("------------------------------")
    print()
    return contador  #➡️ Se devuelve el contador actualizado


def eliminar_producto():
    # ➡️ Permite eliminar un producto de la lista
    if len(lista) == 0:
        print("La lista está vacía, no se puede eliminar ningún producto.")
        print("------------------------------")
        print()
    else:
        print("Lista previa...")
        ver_lista()  #➡️ Mostre la lista previa si no estaba vacía
        borrar = int(input("Ingrese el número del producto a eliminar: "))

        if borrar < 0 or borrar >= len(lista):  #➡️ Verifique si el índice es válido
            print(f"Índice no válido, elija un número entre 0 y {len(lista) - 1}")
            print("------------------------------")
            print()
        else:
            lista.pop(borrar)  ##➡️ Eliminé el producto en el índice indicado
            print("Producto eliminado correctamente.")
            print()

while opcion != 0:
    opcion = menu()  ##➡️ Llamé al menú para seleccionar opción
    if opcion == 1:
        ver_lista()  ##➡️ Llamé para ver la lista
    elif opcion == 2:
        contador = añadir_producto(contador)  ##➡️ Llamé para añadir un producto y actualizar el contador
    elif opcion == 3:
        eliminar_producto()
    elif opcion > 3:
        print("Opción no válida. Por favor, elija una opción del menú.")

print("Gracias por usar el programa 😊")
