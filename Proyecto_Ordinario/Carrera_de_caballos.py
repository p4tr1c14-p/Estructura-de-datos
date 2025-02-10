"""
Nombre: Patricia Pérez Cruz
Fecha: 09 de febrero de 2025
Descripción:
Este juego simula una carrera de caballos utilizando una baraja española
Cada jugador apuesta por un caballo, y el avance de cada uno se determina extrayendo cartas de la baraja
Dependiendo del valor o palo de la carta, un caballo avanzará o se quedará atrás
El primer caballo en llegar a la meta gana la partida
"""
import random

#Lista de cartas que pueden hacer retroceder a los caballos
cartas_horizontales = [
    "1 de Oros", "2 de Oros", "7 de Copas", "4 de Espadas", "5 de Espadas", "12 de Bastos"
]

#Mazo de cartas disponible para la carrera
mazo_cartas = [
    "3 de Oros", "4 de Oros", "5 de Oros", "6 de Oros", "7 de Oros", "10 de Oros", "12 de Oros",
    "1 de Copas", "2 de Copas", "3 de Copas", "4 de Copas", "5 de Copas", "6 de Copas", "10 de Copas", "12 de Copas",
    "1 de Espadas", "2 de Espadas", "3 de Espadas", "6 de Espadas", "7 de Espadas", "10 de Espadas", "12 de Espadas",
    "1 de Bastos", "2 de Bastos", "3 de Bastos", "4 de Bastos", "5 de Bastos", "6 de Bastos", "7 de Bastos",
    "10 de Bastos"
]

#Número de avances necesarios para ganar la carrera
meta = 6
#Límite para que una carta de retroceso sea activada
siguiente_limite = 1


def carta_payaso() -> str:
    """
    Selecciona aleatoriamente una carta de la lista de cartas que hacen retroceder
    a los caballos y la muestra en pantalla
    :return: La carta de retroceso seleccionada
    """
    payaso = random.choice(cartas_horizontales)
    print(f"\n¡La carta {payaso} se ha volteado! 🤡\n")
    return payaso


def sacar_carta() -> str:
    """
    Extrae una carta aleatoria del mazo, la elimina de la lista y la muestra en pantalla.
    :return: La carta extraída del mazo
    """
    carta = random.choice(mazo_cartas)
    mazo_cartas.remove(carta)
    print(f"\nLa carta seleccionada es: {carta}\n")
    return carta


def contar_cartas(carta: str, oro: int, espadas: int, copas: int, bastos: int) -> tuple:
    """
    Aumenta el contador del palo correspondiente según la carta extraída
    :param carta: Carta extraída del mazo
    :param oro: Contador de cartas de Oros
    :param espadas: Contador de cartas de Espadas
    :param copas: Contador de cartas de Copas
    :param bastos: Contador de cartas de Bastos
    :return: Tupla con los nuevos valores de los contadores
    """
    if "Oros" in carta:
        oro += 1
    elif "Espadas" in carta:
        espadas += 1
    elif "Copas" in carta:
        copas += 1
    elif "Bastos" in carta:
        bastos += 1
    return oro, espadas, copas, bastos


def retroceder_caballo(payaso: str, oro: int, espadas: int, copas: int, bastos: int) -> tuple:
    """
    Disminuye el contador del palo correspondiente si la carta seleccionada
    pertenece a una de retroceso
    :param payaso: Carta de retroceso seleccionada
    :param oro: Contador de cartas de Oros
    :param espadas: Contador de cartas de Espadas
    :param copas: Contador de cartas de Copas
    :param bastos: Contador de cartas de Bastos
    :return: Tupla con los nuevos valores de los contadores
    """
    if "Oros" in payaso and oro > 0:
        oro -= 1
    elif "Espadas" in payaso and espadas > 0:
        espadas -= 1
    elif "Copas" in payaso and copas > 0:
        copas -= 1
    elif "Bastos" in payaso and bastos > 0:
        bastos -= 1
    return oro, espadas, copas, bastos


def mostrar_tablero(oro: int, espadas: int, copas: int, bastos: int) -> None:
    """
    Muestra el estado actual de la carrera con la posición de los caballos en pantalla
    :param oro: Contador de cartas de Oros
    :param espadas: Contador de cartas de Espadas
    :param copas: Contador de cartas de Copas
    :param bastos: Contador de cartas de Bastos
    """
    print("-------------------------------🏁🏁🏁🚩")
    nombres = ["Espadas", "Oros", "Copas", "Bastos"]
    valores = [espadas, oro, copas, bastos]
    for indice in range(4):
        print(f"|       {nombres[indice]}")
        print("|       (o o)")
        print("|  /-----\\_/")
        print("|*  ||----||" + " " * (valores[indice] * 3) + "🐎")
    print("-------------------------------🏁🏁🏁🚩")


def jugar() -> None:
    """
    Función principal que controla la mecánica del juego, gestionando
    la extracción de cartas, el avance y retroceso de los caballos,
    y la determinación del ganador
    """
    oro, espadas, copas, bastos = 0, 0, 0, 0
    limite_actual = siguiente_limite
    no_ganador = True
    print("🃏🏇🏿 🃏🏇   Carrera de caballos con cartas españolas  🃏🏇🏿 🃏🏇🏿")
    mostrar_tablero(oro, espadas, copas, bastos)
    while no_ganador and mazo_cartas:
        opcion = input("Ingresa el número '5' para sacar cartas del mazo o '0' para salir: ")
        if opcion == '0':
            break
        elif opcion == '5':
            carta = sacar_carta()
            oro, espadas, copas, bastos = contar_cartas(carta, oro, espadas, copas, bastos)
            mostrar_tablero(oro, espadas, copas, bastos)

            if min(oro, espadas, copas, bastos) >= limite_actual:
                payaso = carta_payaso()
                oro, espadas, copas, bastos = retroceder_caballo(payaso, oro, espadas, copas, bastos)
                limite_actual += 1
                mostrar_tablero(oro, espadas, copas, bastos)

            if oro >= meta:
                ganador = "Oros"
            elif espadas >= meta:
                ganador = "Espadas"
            elif copas >= meta:
                ganador = "Copas"
            elif bastos >= meta:
                ganador = "Bastos"
            else:
                ganador = None

            if ganador:
                no_ganador = False
                print(f"\n¡El caballo {ganador} ha ganado la carrera! 🏆🎉\n")
                mostrar_tablero(oro, espadas, copas, bastos)
        else:
            print("\nOpción no válida, ingresa un número válido\n")


if __name__ == '__main__':
    jugar()
