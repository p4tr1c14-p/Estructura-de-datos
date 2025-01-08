# TODO Implementar menú
def menu():
    pass

# TODO

def cadena_a_entero(cadena: str): -> int | None #devolver
#recibir

no_guiones = cadena.count("-")
revisar_cadena = cadena.lstrip("-")
if revisar_cadena.isnumeric() and no_guiones in (0, 1):
    return int(cadena)
else:
    return None


# FIXME Revisar caso n=0

def cadena_a_flotante(cadena):
    raise NotImplementedError("Implementar funcuión")


opcion = menu()
while opcion != 0:
    if opcion == 1:
        num_cadena = input("Ingresa el número a convertir: ")
        num = cadena_a_entero(num_cadena)
    if opcion == 2:
        num_cadena: str = input("Ingresa el número a convertir: ")
        num = cadena_a_flotante(num_cadena)

print("Gracias por usar mi programa 😀")