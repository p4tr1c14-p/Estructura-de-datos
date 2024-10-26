'''
Nombre: Patricia Pérez Cruz
Fecha: 26 de octubre de 2024
Descripción: Este programa determinará cuál de dos números ingresados por el usuario es menor o si son iguales
Uso de la sentencia de control if - else.
'''

print("*** Programa que determina cuál de los números es menor ***")

#a) Solicite al usuario dos números decimales.
numero_uno, numero_dos = float(input("Ingrese un número decimal: ")), float(input("Ingrese otro número decimal: "))

#b) Utilice la lógica adecuada para determinar cuál de los dos números es menor o si es que son iguales.
#⬆️ En este caso utilizaré la sentencia de control if - else ya que me parece más adecuada

if numero_uno < numero_dos: #➡️ Primero comparo el primer número con el segundo
    #c) Muestre el número menor (o que son iguales) en consola.
    print(f"El número {numero_uno} es menor que {numero_dos}.") #➡️ Si se cumple la condición anterior se imprimirá este cartel

elif numero_dos < numero_uno:
    # c) Muestre el número menor (o que son iguales) en consola.
    print(f"El numero {numero_dos} es menor que {numero_uno}.")  # ➡️ Se imprime este cartel si la condición de "if" no se cumplió

else: #➡️ Si no se cumplió la condición de "if" ni "elif" este bloque se ejecutará
    #c) Muestre el número menor (o que son iguales) en consola.
    print("Son iguales") #➡️ Se imprime este cartel si son iguales