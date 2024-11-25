'''
Nombre: Patricia Pérez Cruz
Fecha: 21 de noviembre de 2024
Descripción:
Este programa muestra el valor máximo y mínimo de una lista de números.
En este caso, la tupla se utiliza para devolver los valores máximo y mínimo de la función.
'''

print("***  Valor máximo y mínimo de una lista de números del usuario  ***")

def menu ():
    print("Bienvenido a mi menú")
    print("1) Ver lista de números.")
    print("2) Añadir número a la lista.")
    print("3) Determinar el valor máximo y mínimo de la lista de números.")
    print("0) Salir.")
    opcion = int(input("Ingrese su selección: "))
    return opcion

def determinar ():
    mayor = lista[0]
    for i in lista:
        if i > mayor:
            mayor = i
    menor = lista[0]
    for x in lista:
        if x < menor:
            menor = x
    return (mayor, menor)

lista = []
usuario_opcion = None
while usuario_opcion != 0:
    usuario_opcion = menu()

    if usuario_opcion == 1:
        if lista:
            print(f"La lista de números es: {lista}")
        else:
            print("La lista está vacía.")
        print("------------------------------")
        print()
    elif usuario_opcion == 2:
        nuevo_num= float(input("Ingrese el número a la lista: "))
        lista.append(nuevo_num)
        print("Se agrego el número correctamente 👩‍💻")
        print()

    elif usuario_opcion == 3:
        if lista:
            tupla = tuple(lista)
            mas, menos= determinar()
            print(f"El número mayor: {mas} y el número menor es: {menos}")
            print()
        else:
            print("La lista esta vacía")
            print()
    elif usuario_opcion > 3:
        print("Opción inválida")

print("Gracias por usar mi programa")