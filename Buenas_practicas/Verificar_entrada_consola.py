"""
Nombre: Patricia Pérez Cruz
Fecha: 7 de diciembre de 2024
Descripción:

"""


"""prueba_numero = int(input("Ingrese un número: "))
print()"""

"""cadena = input("Ingrese su cadena: ").strip()
print()
print("cadena.isalnum()")
print(cadena.isnumeric())
print("cadena.isalpha()")
print(cadena.isalpha())
print("cadena.isalnum()")
print(cadena.isalnum())"""

"""print()
numero = input("Ingrese un número: ")

while not numero.isnumeric():
    print("Opción no válida")
    numero = input("Intenta nuevamente: ")
print()
numero = int(numero)
print(f"El número {numero} es de tipo {type(numero)}")"""

def cadena_a_entero (cadena):
    no_guiones = cadena.count("-")
    revisar_cadena = cadena.lstrip("-")
    if revisar_cadena.isnumeric() and no_guiones in (0, 1):
        return int(cadena)
    else:
        return None

def cadena_a_flotante (cadena):
    no_puntos = cadena.count(".")
    no_guiones = cadena.count("-")
    revisar_cadena = cadena.lstrip("-").replace(".", "")
    if revisar_cadena.isnumeric() and no_guiones in (0, 1) and no_puntos in (0, 1):
        return float(cadena)
    else:
        return None

print()
num_cadena = input("Ingresa Z: ")
numero = cadena_a_flotante(num_cadena)

while numero is None:
    print("Opción inválida")
    num_cadena = input("Ingresa Z: ")
    numero = cadena_a_flotante(num_cadena)

print(f"El número {numero} es tipo {type(numero)}")
