#Un conjunto es desordenado y mutable

print("*** EJEMPLOS DE USO DE LOS CONJUNTOS ***")

conjunto_nombres = set()

print(f"El conjunto vacio es: {conjunto_nombres}")

#Se añaden valores al conjunto:

conjunto_nombres.add("Rebeca")
conjunto_nombres.add("Juan")
conjunto_nombres.add("Bryan")
conjunto_nombres.add("Jamileth")
conjunto_nombres.add("Galilea")
conjunto_nombres.add("Rosalinda")
conjunto_nombres.add("Jenni")
conjunto_nombres.add("Tania")
conjunto_nombres.add("Héctor")
conjunto_nombres.add("Patricia")
conjunto_nombres.add("Addi")
conjunto_nombres.add("Alberto")
print(f"El conjunto es: {conjunto_nombres}")

print("-----------------------------------------------")
conjunto_nombres.add("Galilea")
conjunto_nombres.add("Rosalinda")
conjunto_nombres.add("Tania")
conjunto_nombres.add("Jenni")
conjunto_nombres.add("Tania")
conjunto_nombres.add("Héctor")
print(f"El conjunto es: {conjunto_nombres}")

print("-----------------------------------------------")
#Se eleminan elemento del conjunto

conjunto_nombres.remove("Juan")
print(f"El conjunto es: {conjunto_nombres}")

print("-----------------------------------------------")
#Mostrar todos los elementos

for nombre in conjunto_nombres:
    print(nombre, end= " , ")

print()
print("-----------------------------------------------")
#Verificar si un elemento pertenece a un conjunto

print(f"El elemento Tania pertenece al conjunto? {"Tania" in conjunto_nombres}")
print(f"El elemento Juan pertenece al conjunto? {"Juan" in conjunto_nombres}")

print("-----------------------------------------------")
#Nuevo conjunto de números
conjunto_numeros = {12.1, 1.2, 3.2, -2.3, 4.1}

print("Funciones básicas: ")
print(f"Tamaño del conjunto: {len(conjunto_numeros)}")
print(f"Suma de todos los números: {sum(conjunto_numeros)}")