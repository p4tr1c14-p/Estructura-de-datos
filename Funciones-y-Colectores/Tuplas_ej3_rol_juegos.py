'''
Nombre: Patricia Pérez Cruz
Fecha: 21 de noviembre de 2024
Descripción:
Este programa deja como pivote el 1
y los demás números se recorren
'''
print(" ***  Generación de Jornadas  *** ")

def generar_jornadas():
    equipos = [1, 2, 3, 4, 5, 6, 7, 8]  #➡️ La lista inicial de equipos

    for jornada in range(8):  #➡️ Hay 8 jornadas por eso el 8
        print(f"Jornada {jornada + 1}:")

        #➡️ Creé los partidos de la jornada
        partidos = [
            [equipos[0], equipos[4]],
            [equipos[1], equipos[5]],
            [equipos[2], equipos[6]],
            [equipos[3], equipos[7]]
                    ]

        #➡️ Imprimí los partidos de la jornada
        for partido in partidos:
            print(f"[{partido[0]} vs {partido[1]}]")

        #➡️ Roté los equipos para poder intercambiarlos según lo explicado en la clase lo del pivote)
        #----------------Esto es para la primera columna------------------# #----------------Esto es para la segunda columna-------------#
        equipos = [equipos[0]] + [equipos[4]] + [equipos[1]] + [equipos[2]] + [equipos[5]] + [equipos[6]] + [equipos[7]] + [equipos[3]]

#➡️ Ya fuera de la función la llamé para generar y mostrar las jornadas
generar_jornadas()

print("Disfruta de los partidos ⛹️‍♀️")
