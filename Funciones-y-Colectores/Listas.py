#Crear lista
alumnos = []
alumnos. append("Héctor")
alumnos. append("Addi")
alumnos. append("Jesús Alberto")
alumnos. append("Juan")
alumnos. append("Rosalinda")
alumnos. append("Tania")
alumnos. append("Rebeca")
alumnos. append("Bryan")
alumnos. append("Jamileth")
alumnos. append("Galilea")
alumnos. append("Jennifer")
alumnos. append("Patricia")

len(alumnos)
for i in alumnos:
    print(i)
print()
print("--------------------------------------------------")

alumnos.sort()
for a in alumnos:
    print(a)
print()
print("--------------------------------------------------")

alumnos.sort(reverse = True)
for e in alumnos:
    print(e)
print()
print("--------------------------------------------------")

"""
alumnos.insert(1, "Tania")
alumnos.remove("Héctor")
alumnos.pop(2)
del alumnos[2]

print(alumnos)
for alumno in alumnos:
    print(alumno, end= " ")
"""