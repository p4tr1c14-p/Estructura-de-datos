"""
Nombre: Patricia Pérez Cruz
Fecha: 29 de noviembre de 2024
Descripción:
Este es un juego que se puede jugar de manera grupal,
en donde el objetivo es decir palabras de un tema en específico
y los jugadores deben tratar de no repetir la misma palabra.
Nota: no se debe mostrar las palabras en ningún caso.
Además, se debe llevar un contador de la cantidad de palabras que llevan.
"""

print("  ***  Juego sin repetir  ***")
print(" Este es un juego que se puede jugar de manera grupal,\n"
      " en donde el objetivo es decir palabras de un tema en específico\n"
      " y los jugadores deben tratar de no repetir la misma palabra.\n")


juego = set() #➡️ Declaré mi conjunto
tema = input("Ingrese el tema del juego: ") #➡️ Solicito el tema


continuar = 1  #➡️ Para tener el control del bucle

while continuar:
    numero = len(juego) + 1  #➡️ Para saber el número de palabra actual y +1 para que no de 0 al inicio
    palabra = input(f"Ingrese la palabra {numero} del tema '{tema}': ").strip().lower() #➡️ Para impiar espacios al inicio
    #y final con .strip() y convierte el texto a minúsculas con .lower()

    for revisar in juego:  #➡️ Reviso si hay palabras diferentes
        if revisar == palabra:
            continuar = 0  #➡️ Si hay se detiene el bucle
    else:
        juego.add(palabra)  #➡️ Si no lo agrego al conjunto

print(f"El juego ha terminado! Han dicho {numero} palabras diferentes 🤓") #➡️ Al final imprimir el cartel requerido
print(f"Las palabras del tema {tema} fueron: {juego}")