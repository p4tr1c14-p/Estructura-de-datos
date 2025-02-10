import time

morado = "\033[38;5;128m"
azul = "\033[34m"
amarillo = "\033[33m"
verde = "\033[32m"
reset = "\033[0m"
colores = [morado, azul, amarillo, verde]
cantidad_colores = len(colores)

def mostrar_mensaje(mensaje):
    for i in range(len(mensaje) + 20): #Longitud del desplazamiento
        texto_coloreado = ""
        posicion = 0
        for letra in mensaje:
            texto_coloreado += colores[posicion] + letra
            posicion = (posicion + 1) % cantidad_colores #Ciclo de colores
        print("\r" + " " * i + texto_coloreado + reset, end="", flush=True)
        time.sleep(0.1)
    print()
mensaje = "BIENVENIDO (A)"
mostrar_mensaje(mensaje)