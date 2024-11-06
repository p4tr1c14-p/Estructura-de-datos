#Genera un número aleatorio y hz que lo adivinen una solo vez.
from random import randint

numeros=randint(1,50)
variable=0

while variable!=numeros:
    variable=input("que número cres que es?:")
    if variable==numeros:
        print("El numero es el correcto")
    else:
        print(f"El numero es:{numeros}")