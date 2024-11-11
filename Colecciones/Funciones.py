"""
def hola (nombre):
    print(f"Hola {nombre}")
"""
def menu():
    print(" *** Seleccione una opción del menú *** : ")
    print("1) Suma.")
    print("2) Resta.")
    print("3) Multiplicación.")
    print("4) División")
    print("5) División entera.")
    print("6) Módulo.")
    print("7) Exponenciación.")
    seleccion = int(input("Ingrese su selección: "))
    return seleccion

def calculadora(opcion, numerouno, numerodos):
    if opcion== 1:
        print(numerouno + numerodos)
    elif opcion== 2:
        print(numerouno - numerodos)
    elif opcion == 3:
        print(numerouno * numerodos)
    elif opcion == 4:
        print(numerouno / numerodos)
    elif opcion == 5:
        print(numerouno // numerodos)
    elif opcion == 6:
        print(numerouno % numerodos)
    elif opcion == 7:
        print(numerouno ** numerodos)

numerouno = int(input("Ingrese un número: "))
numerodos = int(input("Ingrese otro número: "))
opcion = menu()
calculadora(opcion, numerouno, numerodos)