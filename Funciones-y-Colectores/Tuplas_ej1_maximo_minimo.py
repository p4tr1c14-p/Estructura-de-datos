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


usuario_opcion = menu()
lista = []
while usuario_opcion != 0:
    if usuario_opcion == 1:
        if lista:
            print(f"La lista de números es: {lista}")
        else:
            print("La lista esta vacía. ")
        print("------------------------------")
        print()
    if usuario_opcion == 2:
        nuevo_num= float(input("Ingrese el número a la lista: "))
        lista[0]= nuevo_num
    else:
        print("adio")