"""
Nombre: Patricia Pérez Cruz
Fecha: 25 de enero de 2025
Descripción: Implementación del juego del "Gato"
Dos jugadores toman turnos para alinear tres marcas consecutivas en una fila, columna o diagonal
"""


import random

def imprimir_tablero(tablero):
    for i in range(3):
        fila = tablero[i][0] + " | " + tablero[i][1] + " | " + tablero[i][2]
        print(fila)
        if i < 2: #Para imprimir una línea divisoria después de cada fila excepto en la última
            print("---" * 5)  #Imprimir la línea divisoria
    print("\n")


def validar_entrada(tablero, fila, columna):
    #Verifico si la casilla está vacía
    disponible = True
    no_disponible = False
    if fila < 0 or fila > 2 or columna < 0 or columna > 2:
        print("Posición fuera de rango! Intenta de nuevo")
        return no_disponible
    elif tablero[fila][columna] != " ":
        print("La casilla ya está ocupada, intenta de nuevo")
        return no_disponible
    return disponible


def verificar_ganador(tablero, jugador):
    #Verifico si un jugador ha ganado
    #Comprobar filas
    for i in range(3):
        #Verificar renglones
        if tablero[i][0] == tablero[i][1] == tablero[i][2] == jugador:  #Este if comprueba si toda una fila está llena por el mismo jugador
            return True

        #Verificar columnas
        if tablero[0][i] == tablero[1][i] == tablero[2][i] == jugador: #Este if comprueba si toda una columna está llena por el mismo jugador
            return True

    #Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador or tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador: #Este if comprueba las dos diagonales del tablero
        return True

    return False


def obtener_jugada_cpu(tablero):
    #Para generar una jugada aleatoria para la CPU
    while True:
        fila = random.randint(0, 2) #Esto genera un número aleatorio entre 0 y 2 para fila
        columna = random.randint(0, 2) #Esto genera un número aleatorio entre 0 y 2 para columna
        if tablero[fila][columna] == " ":  #Verificar que la casilla esté vacía
            return fila, columna


def jugar_gato(modo_juego=None, jugador_1="X", jugador_2="O"):
    #Seleccionar modo de juego
    if modo_juego is None:
        while True:
            opcion = input("Elige modo (1: Dos personas, 2: Contra CPU): ").strip()
            if opcion == "1" or opcion == "2":
                break
            else:
                print("Opción inválida. Debes ingresar 1 o 2.")
        if opcion == "2":
            modo_juego = "cpu"
        else:
            modo_juego = "dos_personas"

    #Inicializar mi tablero y turno
    tablero = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    turno_jugador = jugador_1

    while True:
        imprimir_tablero(tablero)

        #Para el turno de la CPU
        if modo_juego == "cpu" and turno_jugador == jugador_2:
            fila, columna = obtener_jugada_cpu(tablero)
            print(f"Fila de la CPU: {fila+1} | Columna de la CPU: {columna+1}")

        #Para turno del jugador
        else:
            while True:
                #Pedir la fila y la columna
                fila = input("Fila (1-3): ")
                columna = input("Columna (1-3): ")

                #Verificar si las entradas son números y están dentro del rango
                if fila.isdigit() and columna.isdigit():
                    fila = int(fila) - 1
                    columna = int(columna) - 1

                    if fila < 0 or fila > 2 or columna < 0 or columna > 2:
                        print("¡Posición fuera de rango! Intenta de nuevo.")
                    elif tablero[fila][columna] != " ":
                        print("¡Esa casilla ya está ocupada! Intenta de nuevo.")
                    else:
                        break
                else:
                    print("Entrada no válida. Debes ingresar números del 1 al 3.")

        tablero[fila][columna] = turno_jugador

        #Verificar resultado
        if verificar_ganador(tablero, turno_jugador):
            imprimir_tablero(tablero)
            if turno_jugador == jugador_1:
                print("¡Jugador 1 (X) ha ganado!")
            else:
                print("¡Jugador 2 (O) ha ganado!")
            break

        empate = True
        for i in range(3):  #Recorrí las filas
            for j in range(3):  #Recorrí las columnas
                if tablero[i][j] == " ":  #Si se encuentra una casilla vacía
                    empate = False
                    break  #Para salir del bucle de columnas
            if not empate:  #Y si ya se encontro una casilla vacía, paro
                break

        if empate:  #Si no hay casillas vacías, es un empate
            imprimir_tablero(tablero)
            print("Es un empate")
            break

        #Para cambiar turno
        if turno_jugador == jugador_2:
            turno_jugador = jugador_1
        else:
            turno_jugador = jugador_2


if __name__ == "__main__":
    jugar_gato()
