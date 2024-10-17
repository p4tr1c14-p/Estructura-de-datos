
cantidad = input("¿Compras mayores a $5,000.00? Ingrese su cantidad con decimales: ")
cadena = input("¿Compras a MSI? (si/no): ")

total = float(cantidad)
var_bool = bool(total)

cadena = cadena.lower() == "si"

print(f"¿Aplica bonificación?: {var_bool>5000 and cadena}")