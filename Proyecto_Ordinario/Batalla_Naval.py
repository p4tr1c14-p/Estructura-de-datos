"""
Nombre: Patricia Pérez Cruz
Fecha: 09 de febrero de 2025
Descripción: Implementación del juego de Batalla Naval
Dos jugadores colocan estratégicamente sus barcos en un tablero y luego intentan hundir los barcos del oponente
adivinando sus posiciones
Cada jugador tiene un tablero donde marca sus propios barcos y otro tablero donde
registra los disparos realizados al enemigo. El objetivo es hundir todos los barcos del oponente antes de que
él hunda los tuyos
"""


import random

victorias_jugador = 0
derrotas_jugador = 0
victorias_jugador2 = 0
derrotas_jugador2 = 0
victorias_cpu = 0
derrotas_cpu = 0
#Estos son mks diccionarios.
letras_columnas = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E'}


def convertir_coordenadas(barcos):
    return [(fila, letras_columnas[columna]) for fila, columna in barcos]

"""
Crea un tablero vacío de 5x5 con símbolos '~', que representan el agua.

Returns:
 Tablero 5x5 con todas las celdas inicializadas en '~'.
"""

def crear_tablero():
    return [['~' for _ in range(5)] for _ in range(5)]

"""
Muestra el tablero en consola. Puede ocultar los barcos si así se solicita.

Args:
    tablero: Matriz 5x5 que representa el tablero.
    ocultar: Si es 1, oculta los barcos ('⛵') y los muestra como agua ('~').

Returns:
    None: Solo imprime el tablero en consola.
"""

def mostrar_tablero(tablero, ocultar):
    print("  A B C D E")
    fila_numero = 0
    for fila in tablero:
        print(fila_numero, end=' ')
        for celda in fila:
            if ocultar == 1 and celda == '⛵':
                print('~', end=' ')
            else:
                print(celda, end=' ')
        print()
        fila_numero += 1
"""
Solicita al jugador la cantidad de barcos a colocar (de 1 a 5) y asegura que la entrada sea válida.

Returns:
La cantidad de barcos que el jugador desea colocar (entre 1 y 5).
"""

def obtener_cantidad_barcos():
    cantidad = 0
    while cantidad < 1 or cantidad > 5:
        entrada = input("¿Cuántos barcos deseas colocar? (1-5): ")
        if entrada.isdigit():
            cantidad = int(entrada)
        if cantidad < 1 or cantidad > 5:
            print("Opción inválida. Ingresa un número entre 1 y 5,por favor.")
    return cantidad

"""
Coloca los barcos en el tablero en posiciones aleatorias.

Args:
tablero: El tablero en el que se colocarán los barcos.
cantidad: La cantidad de barcos a colocar en el tablero.

Returns:
Lista de coordenadas (fila, columna) donde los barcos fueron colocados.
"""

def colocar_barcos(tablero, cantidad):
    barcos = []
    while len(barcos) < cantidad:
        fila, columna = random.randint(0, 4), random.randint(0, 4)
        if tablero[fila][columna] == '~':
            tablero[fila][columna] = '⛵'
            barcos.append((fila, columna))
    return barcos
"""
Solicita al jugador que ingrese un número de fila válido (de 0 a 4).

Returns:
El número de fila elegido por el jugador.
"""

def obtener_fila():
    numero = -1
    while numero < 0 or numero > 4:
        entrada = input("Ingresa fila (0-4): ")
        if entrada.isdigit():
            numero = int(entrada)
        if numero < 0 or numero > 4:
            print("Opción inválida❌❌. Ingresa un número entre 0 y 4,por favor.")
    return numero

"""
Solicita al jugador que ingrese una letra correspondiente a una columna válida (de A a E).

Returns:
El número de columna correspondiente a la letra ingresada (0 para A, 1 para B, etc.).
"""

def obtener_columna():
    letras = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4}
    columna = None
    while columna is None:
        entrada = input("Ingresa la  columna de: (A-E): ").lower()  # Convertimos a minúsculas
        if entrada in letras:
            columna = letras[entrada]
        else:
            print("Opción inválida❌❌. Ingresa una letra entre A y E,por favor.")
    return columna

"""
Muestra el tablero con los barcos colocados en sus posiciones correspondientes.

Args:
    tablero: Matriz 5x5 que representa el tablero.
    barcos: Lista de coordenadas (fila, columna) de los barcos.

Returns:
    None: Solo imprime el tablero con los barcos en consola.
"""

def mostrar_tablero_con_barcos(tablero, barcos):
    """
    Muestra el tablero y coloca los barcos en sus posiciones
    utilizando el emoji ⛵.
    """
    for fila, columna in barcos:
        tablero[fila][columna] = '⛵'

    mostrar_tablero(tablero, ocultar=0)  # Mostrar el tablero completo (sin ocultar)
"""
Lleva a cabo una partida contra la CPU. El jugador trata de adivinar la ubicación de los barcos enemigos.

Returns:
    None: Controla el flujo principal del juego contra la CPU.
"""

def jugar_contra_pc():
    global victorias_jugador, derrotas_jugador, victorias_cpu, derrotas_cpu
    print("Modo: Contra la PC")
    tablero_jugador = crear_tablero()
    tablero_cpu = crear_tablero()
    num_barcos = obtener_cantidad_barcos()
    barcos_cpu = colocar_barcos(tablero_cpu, num_barcos)
    intentos = 5
    barcos_restantes = num_barcos
    print("")
    print("╏╠══[𝍖𝍖𝍖 𝚂𝚎 𝚑𝚊𝚗 𝚊ñ𝚊𝚍𝚒𝚍𝚘 𝚌𝚘𝚛𝚛𝚎𝚌𝚝𝚊𝚖𝚎𝚗𝚝𝚎 𝚝𝚞𝚜 𝚋𝚊𝚛𝚌𝚘𝚜 𝍖𝍖𝍖]      💦")
    print(" ")
    print("--------------------------------------------------------------------")
    print("¡Es momento de adivinar los barcos enemigos!")
    print("--------------------------------------------------------------------")
    while intentos > 0 and barcos_restantes > 0:
        print("\nTu tablero:")
        mostrar_tablero(tablero_jugador, 1)

        fila = obtener_fila()
        columna = obtener_columna()

        if tablero_jugador[fila][columna] != '~':
            print("Ya disparaste aquí. Intenta otra vez,por favor.")
        else:
            if (fila, columna) in barcos_cpu:
                print("¡Tocado y hundido!")
                tablero_jugador[fila][columna] = '⛵'
                barcos_restantes -= 1
            else:
                print("Aguaaaaa!")
                tablero_jugador[fila][columna] = 'X'
            intentos -= 1

    if barcos_restantes > 0:
        print("¡Perdisteeee😞! Los barcos estaban en:", convertir_coordenadas(barcos_cpu))
        derrotas_jugador += 1
        victorias_cpu += 1
    else:
        print("¡Ganasteeee😞! Hundiste todos los barcos.")
        victorias_jugador += 1
        derrotas_cpu += 1

    print("\nAquí están las posiciones finales de los barcos⛵:")
    mostrar_tablero_con_barcos(tablero_cpu, barcos_cpu)  # Mostrar tablero con los barcos
    volver_a_jugar("pc", barcos_cpu)

"""
Lleva a cabo una partida entre dos jugadores. Ambos intentan hundir los barcos del otro.

Returns:
    None: Controla el flujo principal del juego entre dos jugadores.
"""
def jugar_contra_jugador():
    global victorias_jugador, derrotas_jugador, victorias_jugador2, derrotas_jugador2
    print("Estas en el modo: Contra otro jugador🤩")
    tablero_jugador1 = crear_tablero()
    tablero_jugador2 = crear_tablero()
    num_barcos = obtener_cantidad_barcos()
    barcos_jugador1 = colocar_barcos(tablero_jugador1, num_barcos)
    barcos_jugador2 = colocar_barcos(tablero_jugador2, num_barcos)
    intentos = 5
    barcos_restantes_j1 = num_barcos
    barcos_restantes_j2 = num_barcos
    print("╏╠══[𝍖𝍖𝍖 𝚂𝚎 𝚑𝚊𝚗 𝚊ñ𝚊𝚍𝚒𝚍𝚘 𝚌𝚘𝚛𝚛𝚎𝚌𝚝𝚊𝚖𝚎𝚗𝚝𝚎 𝚝𝚞𝚜 𝚋𝚊𝚛𝚌𝚘𝚜 𝍖𝍖𝍖]      ⛵")
    print(" ")
    print("--------------------------------------------------------------------")
    print("¡Es momento de adivinar los barcos⛵ enemigos❌!")
    print("--------------------------------------------------------------------")

    while intentos > 0 and (barcos_restantes_j1 > 0 and barcos_restantes_j2 > 0):
        # Turno del Jugador 1
        print("\nTurno del Jugador 1️⃣:")
        mostrar_tablero(tablero_jugador2, 1)

        fila = obtener_fila()
        columna = obtener_columna()

        if tablero_jugador2[fila][columna] == '~':
            if (fila, columna) in barcos_jugador2:
                print("¡Tocado y hundido!")
                tablero_jugador2[fila][columna] = '⛵'
                barcos_restantes_j2 -= 1
            else:
                print("Aguaaaaa!")
                tablero_jugador2[fila][columna] = 'X'
        else:
            print("Ya disparaste🔫🔫 aquí.")

        if barcos_restantes_j2 == 0:
            print("¡Ganaste, Jugador 1! Hundiste todos los barcos del Jugador 2.")
            victorias_jugador += 1
            derrotas_jugador2 += 1
            break

        # Turno del Jugador 2
        print("\nTurno del Jugador 2️⃣:")
        mostrar_tablero(tablero_jugador1, 1)

        fila = obtener_fila()
        columna = obtener_columna()

        if tablero_jugador1[fila][columna] == '~':
            if (fila, columna) in barcos_jugador1:
                print("¡Tocado y hundido!")
                tablero_jugador1[fila][columna] = '⛵'
                barcos_restantes_j1 -= 1
            else:
                print("Aguaaaaa!")
                tablero_jugador1[fila][columna] = 'X'
        else:
            print("Ya disparaste🔫🔫 aquí.")

        if barcos_restantes_j1 == 0:
            print("¡Ganaste, Jugador 2! Hundiste todos los barcos del Jugador 1.")
            victorias_jugador2 += 1
            derrotas_jugador += 1
            break

        intentos -= 1

    print("\n⛵⛵⛵Aquí están las posiciones finales de los barcos⛵⛵⛵:")
    # Mostrar los barcos en sus posiciones finales para ambos jugadores
    print("\nTablero final del Jugador 1:")
    mostrar_tablero_con_barcos(tablero_jugador1, barcos_jugador1)
    print("\nTablero final del Jugador 2:")
    mostrar_tablero_con_barcos(tablero_jugador2, barcos_jugador2)

    volver_a_jugar("jugadores", barcos_jugador1, barcos_jugador2)


def volver_a_jugar(modo, barcos_jugador1=None, barcos_jugador2=None):
    if modo == "pc":
        print("\n📊📊Estadísticas📊📊:")
        print(f"Jugador - Victorias: {victorias_jugador}, Derrotas: {derrotas_jugador}")
        print(f"CPU - Victorias: {victorias_cpu}, Derrotas: {derrotas_cpu}")
    else:
        print("\n📊📊Estadísticas📊📊:")
        print(f"Jugador 1 - Victorias: {victorias_jugador}, Derrotas: {derrotas_jugador}")
        print(f"Jugador 2 - Victorias: {victorias_jugador2}, Derrotas: {derrotas_jugador2}")

        # Mostrar coordenadas de los barcos al final del juego
        print("\n🛳️🛳️Coordenadas de los barcos🛳️🛳️:")
        print(f"Jugador 1: {convertir_coordenadas(barcos_jugador1)}")
        print(f"Jugador 2: {convertir_coordenadas(barcos_jugador2)}")

    opcion = ""
    while opcion != '1' and opcion != '2':
        print("\n¿🎮🎮Quieres volver a jugar🎮🎮?")
        print("1. Sí")
        print("2. No (Salir)")
        opcion = input("Selecciona una opción (1 o 2): ")
        if opcion == '1':
            jugar()
        elif opcion == '2':
            print("🎮🎮Gracias por jugar🎮🎮. ¡Hasta la próxima!")
            return  # Aquí se termina la ejecución del programa de manera sencilla.
        else:
            print("Opción inválida❌. Ingresa 1 o 2.")

def jugar():
    print("Bienvenido a Batalla Naval")
    print("1. 🎮🎮Jugar contra la PC🎮🎮")
    print("2. 🙍‍♂️🙍‍♂️Jugar contra otro jugador🙍‍♂️🙍‍♂️")
    opcion = ""
    while opcion != '1' and opcion != '2':
        opcion = input("Selecciona una opción (1 o 2): ")
        if opcion == '1':
            jugar_contra_pc()
        elif opcion == '2':
            jugar_contra_jugador()
        else:
            print("Opción inválida❌. Ingresa 1 o 2.")


jugar()