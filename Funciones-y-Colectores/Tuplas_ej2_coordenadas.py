'''
Nombre: Patricia Pérez Cruz
Fecha: 21 de noviembre de 2024
Descripción:
Este programa almacena diversos puntos
como coordenadas y permite obtener la ecuación
de la recta entre dos de los puntos.
'''

print(" ***  Rectas a partir de puntos (coordenadas) en el plano cartesiano  *** ")
# Lista para almacenar coordenadas
coordenadas = []


def ver_coordenadas():
    if len(coordenadas) == 0: #➡️ Reviso si la lista esta vacia
        print("No hay coordenadas almacenadas.")
    else:
        indice = 1
        for coord in coordenadas: #➡️ Recorrí y muestré las coordenadas con índice
            print(f"Coordenada {indice} :{coord}")
            indice = indice + 1
    print()


def agregar_coordenada():  #➡️ Me permitió ingresar una nueva coordenada (x,y) a la lista

   x = float(input("Ingresa la coordenada x: "))
   y = float(input("Ingresa la coordenada y: "))
   coordenadas.append((x, y)) #➡️ Agregué la coordenada como una tupla
   print("Coordenada agregada con éxito")
   print("------------------------------------------------")


def calcular_pendiente_y_ecuacion():
    if len(coordenadas) < 2: #➡️ Verifiqué que haya al menos dos coordenadas
        print("No hay suficientes coordenadas para calcular la pendiente")
        print("------------------------------------------------")
    else:
        ver_coordenadas()
        print("Selecciona el índice de la primera coordenada:")
        i1 = int(input()) - 1  #➡️ Obtuve el índice de la primera coordenada
        print("Selecciona el índice de la segunda coordenada:")
        i2 = int(input()) - 1 #➡️ Obtuve el índice de la segunda coordenada

        x1, y1 = coordenadas[i1]
        x2, y2 = coordenadas[i2]

        if x1 == x2:
            print(f"La recta es vertical: x = {x1}, ")
        else:
            pendiente = (y2 - y1) / (x2 - x1)
            intercepto = y1 - pendiente * x1
            print(f"La pendiente entre la coordenada {coordenadas[i1]} y {coordenadas[i2]} es {pendiente}")
            print(f"La ecuación de la recta es: y = {pendiente} x + {intercepto}")
            print("------------------------------------------------")
def eliminar_coordenada():
    if len(coordenadas) == 0:
        print("No hay coordenadas para eliminar")
        print("------------------------------------------------")
    else:
        ver_coordenadas()
        i = int(input("Selecciona el índice de la coordenada a eliminar:"))
        i = i - 1
        if i >= 0 and i < len(coordenadas):
            eliminada = coordenadas[i]
            del coordenadas[i] #➡️ Elimina la coordenada seleccionada
            print(f"Coordenada {eliminada} eliminada con éxito")
            print("------------------------------------------------")
        else:
            print("Indice fuera de rango")
            print("------------------------------------------------")

def menu():
    condicion = None
    while condicion != 0:
        print("*** Rectas a partir de puntos (coordenadas) en el plano cartesiano ***")
        print("1) Ver coordenadas almacenadas")
        print("2) Agregar coordenada (x, y)")
        print("3) Calcular la pendiente y la ecuación de la recta entre dos coordenadas")
        print("4) Eliminar coordenada (x, y)")
        print("0) Salir")
        condicion = int(input("Ingresa una de las opciones:"))
        return condicion


auxiliar = None
while auxiliar != 0:
    auxiliar = menu() #➡️ LLamé a menú

    if auxiliar == 1:
        ver_coordenadas()
    elif auxiliar == 2:
        agregar_coordenada()
    elif auxiliar == 3:
        calcular_pendiente_y_ecuacion()
    elif auxiliar == 4:
        eliminar_coordenada()
    elif auxiliar > 4:
        print("Opción no válida ")

print("¡Hasta luego!")
