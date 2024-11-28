print(" Se crean dos conjuntos ")

ConjuntoA = {11, 7, 10, 9, 5, 1, 15, 7}
ConjuntoB = {55, 70, 11,77, 66, 9 , 5}
print(ConjuntoA)
print(ConjuntoB)

print("- OPEREACIONES BÁSICAS -")

print("UNIÓN")
union = ConjuntoA | ConjuntoB
print(union)

print("INTERSECCÓN")
interseccion = ConjuntoA & ConjuntoB
print(interseccion)

print("A-B")
menosb = ConjuntoA - ConjuntoB
print(menosb)

print("B-A")
menosa =  ConjuntoB - ConjuntoA
print(menosa)

print(" ANIMALES 🐹")
animales = ["Gato", "Ratón", "Perro", "Rana", "Zombie", "Gato"]
print(f"Conjunto original: {animales}")

conjunto = set(animales)
lista_modificada = list(conjunto)
print(f"El conjunto es: {lista_modificada}")