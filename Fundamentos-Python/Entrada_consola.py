'''
Nombre: Patricia Pérez Cruz
Fecha: 14 de octubre de 2024
Descripción:
Mi primera información sobre la entrada de datos por consola
en Python para interactuar con el usuario con valores dinámicos.
'''

# Comentar sobre la función input.

#⬇️La función input me permite pedir información al usuario y usarla en mi código,
# yo lo tome como que es un asistente para mi y además me ayuda a poder interactuar
# con el usuario 😀

numero1_cadena = input("Introduce un número decimal: ")
numero2_cadena = input("Introduce otro número decimal: ")
resultado_cadena = numero1_cadena + numero2_cadena # Verificar qué es lo que realiza esta instrucción (ver el print).
print()
print(" ****  Recibir número sin un casting de varibles  ****")
print(f"El resultado de {numero1_cadena} y {numero2_cadena} es: {resultado_cadena}")
#⬆️ Por lo que pude observar con lo anterior los resultados se concatenan lo cual no es correcto
# y se tendrá que realizar un "Casting"


# Comentar por qué se realiza el casting de variables.
# ⬆️ El casting se debe de hacer ya que la funcion input() siempre devuelve una cadena de texto (string)

numero1_float = float(numero1_cadena)
numero2_float = float(numero2_cadena)
resultado_float = numero1_float + numero2_float # Verificar qué es lo que realiza de esta manera y compáralo.
print()
print(" ****  Casting de varibles  ****")
print(f"El resultado de {numero1_float} y {numero2_float} es: {resultado_float}")

# ⬆️ Al usar la función input() en Python se obtienen cadenas de texto, lo que significa que
# cualquier operación entre ellas resultará en concatenación en lugar de una suma normal
# Para realizar operaciones matemáticas correctamente es necesario convertir estas cadenas a su tipo
# numérico correspondiente como float o int, ya que esto asegurará que el programa funcione de la
# manera deseada permitiendo obtener resultados correctos