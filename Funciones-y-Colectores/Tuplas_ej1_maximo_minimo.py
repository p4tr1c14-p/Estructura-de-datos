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

def mostrar ():
    if lista:
        print(f"La lista de números es: {lista}")
    else:
        print("La lista está vacía.")
    print("------------------------------")
    print()

def agregar ():
    nuevo_num = float(input("Ingrese el número a la lista: ")) #➡️ Solicité un número al usuario
    lista.append(nuevo_num) #➡️ Aquí lo agregué con el append
    print("Se agrego el número correctamente 👩‍💻")
    print()

def determinar ():
    mayor = lista[0] #➡️ Inicialicé el mayor con el primer elemento
    for i in lista:
        if i > mayor:
            mayor = i
    menor = lista[0] #➡️ Inicialicé el menor con el primer elemento
    for x in lista: #➡️ Recorrí la lista para encontrar el menor
        if x < menor:
            menor = x
    return (mayor, menor) #➡️ Retorné una tupla con el mayor y el menor

lista = []
usuario_opcion = None
while usuario_opcion != 0:  #➡️ Repite mientras el usuario no elija salir
    usuario_opcion = menu()

    if usuario_opcion == 1:
        mostrar()

    elif usuario_opcion == 2:
        agregar()

    elif usuario_opcion == 3:
        if lista: #➡️ Verifiqué que la lista no esté vacía antes de calcular
            tupla = tuple(lista) #➡️ Convertpi la lista a una tupla
            mas, menos= determinar() # <➡️ Obtuve el mayor y el menor de la lista
            print(f"El número mayor: {mas} y el número menor es: {menos}")
            print()
        else:
            print("La lista esta vacía")
            print()
    elif usuario_opcion > 3:
        print("Opción inválida")

print("Gracias por usar mi programa :D")