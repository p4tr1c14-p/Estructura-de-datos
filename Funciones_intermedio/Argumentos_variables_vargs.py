
def colores_favoritos(persona: str, *vargs):
    print(f"{persona}: {vargs}")


if __name__ == '__main__':
    colores_favoritos("Jennifer", "Morado", "Negro", "Blanco", "Rosa")
    colores_favoritos("Addi", "Azul", "Blanco", "Negro")
    colores_favoritos("Pati", "Verde")

def sumar(*vargs) -> int:
    resultado = 0
    for i in vargs:
        resultado = resultado + i
    return resultado


res = sumar(5, 3, 4)
print(f"El resultado es: {res}")



cadena = "Hola"
tupla = "Hola,"

print(cadena)
print(tupla)

