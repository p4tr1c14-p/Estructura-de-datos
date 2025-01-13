#funcion que se llame saludar que reciba nombre string nbo regresa nada, imprimir hola y nombre

def saludar(love) -> str | None:
    print(f"Hola, {love}")


if __name__ == '__main__':
    usuario = input("Ingresa nombre del usuario: ")
    saludar(usuario)