def menu() -> int | int:
    """
    Muestra el menú del programa
    :return: La selección del usuario
    """
    print("1. Sumar")
    print("2. Restar")
    print("0. Salir")
    seleccion = int(input("Elige una opción: "))

    # Verificar si la entrada es un número entero y está dentro de las opciones válidas
    if seleccion == 0 or seleccion == 1 or seleccion == 2:
        return seleccion
    else:
        print("Por favor, ingresa una opción válida 😳")

def sumar(uno, dos) -> int | int:
    total = uno + dos
    print(total)
    print()
    return total

def resta(tres, cuatro) -> int | int:
    resultado = tres - cuatro
    print(resultado)
    print()
    return resultado

def ingresar_numero() ->int | None:
    primer_numero = input("Ingresa un número: ")
    segundo_numero = input("Ingresa un número: ")
    print(f" {type(primer_numero)} y {type(segundo_numero)} ")
opcion = None #➡️ Aplique lo que me comento sobre la variable None
while opcion != 0:
    opcion = menu()
    if opcion == 1:
        numuno, numdos = ingresar_numero()
        sumar(numuno, numdos)
    if opcion == 2:
        numuno, numdos = ingresar_numero()
        resta(numuno, numdos)