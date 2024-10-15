print()
print("*** ASIGNACIÓN ENCADENADA ***")
print()
v1,v2 = 5,10
print(v1,v2)
v3, v4 = 9.14, "Chuy"
print(v3,v4)
v5,v6 = v1 + v2, v1-v2
print(v5,v6)
v7 = v8=v9=10
print(v7)
print(v8)
print(v9)

v10, v11 = "Alberto", "Geto"
print(v10, v11)

v11,v10 = v10, v11
print(v10, v11)

nombre,apellido = input("Ingrese nombre: "), input("Ingrese apellido: ")
print(nombre,apellido)