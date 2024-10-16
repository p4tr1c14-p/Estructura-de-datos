
#Se utiliza para comparar dos valores

num01 = input("Ingrese un numero: ")
num02 = input("Ingrese un numero: ")

num11 = float(num01)
num22 = float(num02)


print(f"¿El numero {num11:.2f} es mayor a {num22:.2f}?: {num11 > num22}")
print(f"¿El numero {num11:.2f} es mayor igual a {num22:.2f}?: {num11 >= num22}")
print(f"¿El numero {num11:.2f} es igual a {num22:.2f}?: {num11 == num22}")
print(f"¿El numero {num11:.2f} es menor a {num22:.2f}?: {num11 < num22}")
print(f"¿El numero {num11:.2f} es menor igual a {num22:.2f}?: {num11 <= num22}")
print(f"¿El numero {num11:.2f} es diferente a {num22:.2f}?: {num11 != num22}")