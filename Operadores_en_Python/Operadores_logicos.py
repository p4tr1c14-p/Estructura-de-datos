
cad_1 = input("Ingrese si/no: ")
cad_2 = input("Ingrese si/no: ")


cad_1 = cad_1.lower() == "si"
cad_2 = cad_2.lower() == "si"


print(f" La expresion uno es {cad_1}")
print(f" La expresion dos es {cad_2}")
print()
print(f"¿Ambos fueron si?: {cad_1 and cad_2}")
print()
print(f"¿Ambos fueron si?: {cad_1 or cad_2}")
print()
print(f"¿Ambos fueron si?: {not cad_1}")
print(f"¿Ambos fueron si?: {not cad_2}")