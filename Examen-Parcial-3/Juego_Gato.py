"""
Nombre: Patricia Pérez Cruz
Fecha: 25 de enero de 2025
Descripción: Implementación del juego del "Gato"
Dos jugadores toman turnos para alinear tres marcas consecutivas en una fila, columna o diagonal
"""

import random

def imprimir_tablero(tablero):
    """Muestra el estado actual del tablero en la consola"""
    for i in range(3):
        fila = tablero[i][0] + " | " + tablero[i][1] + " | " + tablero[i][2]
        print(fila)
        if i < 2:  # Imprime una línea divisoria después de cada fila excepto la última
            print("---" * 5)  # Línea divisoria entre filas
    print("\n")

def validar_entrada(tablero, fila, columna):
    """Verifica si la casilla seleccionada está vacía y dentro del rango permitido"""
    if fila < 0 or fila > 2 or columna < 0 or columna > 2:
        print("Posición fuera de rango! Intenta de nuevo")
        return False
    elif tablero[fila][columna] != " ":
        print("La casilla ya está ocupada, intenta de nuevo")
        return False
    return True

def verificar_ganador(tablero, jugador):
    """Comprueba si el jugador ha ganado verificando filas, columnas y diagonales"""
    #Verificar filas y columnas
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] == jugador:
            return True  # Gana por fila
        if tablero[0][i] == tablero[1][i] == tablero[2][i] == jugador:
            return True  # Gana por columna

    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador or tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        return True  #Gana por diagonal

    return False

def obtener_jugada_cpu(tablero):
    """Genera una jugada aleatoria para la CPU en una casilla vacía"""
    while True:
        fila = random.randint(0, 2)
        columna = random.randint(0, 2)
        if tablero[fila][columna] == " ":
            return fila, columna

def jugar_gato(modo_juego=None, jugador_1="X", jugador_2="O"):
    """Ejecuta el juego del gato en modo de dos jugadores o contra la CPU"""
    #Selección de modo de juego
    if modo_juego is None:
        while True:
            opcion = input("Elige modo (1: Dos personas, 2: Contra CPU): ").strip()
            if opcion in ["1", "2"]:
                break
            print("Opción inválida. Debes ingresar 1 o 2.")
        modo_juego = "cpu" if opcion == "2" else "dos_personas"

    #Inicializar tablero
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    turno_jugador = jugador_1

    while True:
        imprimir_tablero(tablero)

        # Turno de la CPU
        if modo_juego == "cpu" and turno_jugador == jugador_2:
            fila, columna = obtener_jugada_cpu(tablero)
            print(f"Fila de la CPU: {fila+1} | Columna de la CPU: {columna+1}")
        else:
            while True:
                fila = input("Ingresa tu fila (1-3): ")
                columna = input("Ingresa tu columna (1-3): ")
                if fila.isdigit() and columna.isdigit():
                    fila, columna = int(fila) - 1, int(columna) - 1
                    if validar_entrada(tablero, fila, columna):
                        break
                print("Entrada no válida. Intenta de nuevo")

        #Colocar la jugada en el tablero
        tablero[fila][columna] = turno_jugador

        #Verificar si hay un ganador
        if verificar_ganador(tablero, turno_jugador):
            imprimir_tablero(tablero)
            print(f"¡El jugador {turno_jugador} ha ganado!")
            break

        #Verificar empate
        if all(tablero[i][j] != " " for i in range(3) for j in range(3)):
            imprimir_tablero(tablero)
            print("Es un empate.")
            break

        #Cambiar turno
        turno_jugador = jugador_2 if turno_jugador == jugador_1 else jugador_1

if __name__ == "__main__":
    jugar_gato()
