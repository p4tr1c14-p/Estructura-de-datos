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

cartas_horizontales = [
    "1 de Oros", "2 de Oros", "7 de Copas", "4 de Espadas", "5 de Espadas", "12 de Bastos"
]

mazo_cartas = [
    "3 de Oros", "4 de Oros", "5 de Oros", "6 de Oros", "7 de Oros", "10 de Oros", "12 de Oros",
    "1 de Copas", "2 de Copas", "3 de Copas", "4 de Copas", "5 de Copas", "6 de Copas", "10 de Copas", "12 de Copas",
    "1 de Espadas", "2 de Espadas", "3 de Espadas", "6 de Espadas", "7 de Espadas", "10 de Espadas", "12 de Espadas",
    "1 de Bastos", "2 de Bastos", "3 de Bastos", "4 de Bastos", "5 de Bastos", "6 de Bastos", "7 de Bastos",
    "10 de Bastos"
]