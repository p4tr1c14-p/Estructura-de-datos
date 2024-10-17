"""
ENTRADA CONSOLA EJERCICIO

a) Pida 2 números decimales por consola al usuario utilizando la función input.

b) Muestre los resultados de las operaciones básicas con esos números: suma, resta, multiplicación y división.

Nota: Asuma que el usuario siempre va a ingresar números y que el segundo número es diferente de cero.
"""

print()
var_float1 = input("Ingrese un número decimal: ")
var_float2 = input("Ingrese otro número decimal: ")

numero1 = float(var_float1)
numero2 = float(var_float2)

print("*** SUMA ***")
suma = numero1 + numero2
print(f"El resultado de la suma es = {suma:.2f}")
print()

print("*** RESTA ***")
resta = numero1 - numero2
print(f"El resultado de la resta es = {resta:.2f}")
print()

print("*** MULTIPLICACION ***")
multiplicacion = numero1 * numero2
print(f"El resultado de la multiplicación es = {multiplicacion:.2f}")
print()

print("*** DIVISIÓN ***")
division = numero1 / numero2
print(f"El resultado de la división es = {division:.2f}")
print()

