"""
Nombre: Patricia Pérez Cruz
Fecha: 6 de diciembre de 2024
Descripción:
Este programa determina la casa (Gryffindor, Slytherin, Hufflepuff y Ravenclaw) a la que perteneces,
de acuerdo a tus respuestas.
"""
import random

#➡️ En este diccionario almacené los puntajes de cada casa
#➡️ A medida que el usuario responde las preguntas los valores se incrementan según la casa asociada a cada respuesta
respuestas = {
    'Gryffindor': 0,
    'Slytherin': 0,
    'Hufflepuff': 0,
    'Ravenclaw': 0
}

#➡️ En esta lista estan las preguntas y opciones
preguntas = [
    ("¿Cuál de las siguientes opciones odiarías más que la gente te llamara?",
     ['Ordinario', 'Ignorante', 'Cobarde', 'Egoísta']),
    ("Después de tu muerte ¿qué es lo que más le gustaría que hiciera la gente cuando escuche su nombre?",
     ['Te extraña, pero sonríe.', 'Pide más historias sobre tus aventuras.', 'Piensa con admiración tus logros.',
      'No me importa lo que piensen de mí después de mi muerte, lo que piensen de mí ahora es lo que cuenta.']),
    ("Dada la opción, preferirías inventar una poción que garantizara:",
     ['Gloria.', 'Sabiduría.', 'Amor.', 'Poder.']),
    ("¿Cómo te definirías en una sola palabra?",
     ['Valiente.', 'Ambicioso.', 'Leal.', 'Curioso.']),
    ("¿Qué cualidad te describe mejor?",
     ['La fuerza.', 'La astucia.', 'La paciencia.', 'La inteligencia.']),
    ("¿Cuál es tu clase favorita?",
     ['Vuelo.', 'Defensa contra las artes oscuras.', 'Animales fantásticos.', 'Pociones.']),
    ("¿Cuál es tu lenguaje de programación favorito?",
     ['C.', 'Python.', 'C++.', 'JavaScript.'])
]


#➡️ Con esta función realizo las preguntas
def realizar_test():
    #➡️ Reinicio las respuestas
    respuestas['Gryffindor'] = 0
    respuestas['Slytherin'] = 0
    respuestas['Hufflepuff'] = 0
    respuestas['Ravenclaw'] = 0

    for i in range(len(preguntas)):  #➡️ Con lend mido el tamaño de las preguntas para realizarlas todas
        pregunta, opciones = preguntas[i]
        #➡️ i almacena el índice actual en la lista preguntas, usado para acceder a cada elemento
        #➡️ Pregunta guarda el texto de la pregunta, y opciones almacena la lista de respuestas posibles

        random.shuffle(opciones) #➡️ Investigando me encontré con shuffle lo que
        # me va a ayudar para cambiar las posiciones de las opciones

        while True:
            print(f"\n{pregunta}")
            for j in range(4):  # Mostrar las 4 opciones
                print(f"{j + 1}) {opciones[j]}") #➡️ Aquí itero sobre las opciones y mostrarlas enumeradas

            # Recoger la respuesta válida
            respuesta = input("\nElige una opción (1-4): ")
            if respuesta in ['1', '2', '3', '4']: #➡️ Checo si la opción que elijio esta
                indice = int(respuesta) - 1
                #➡️ Si coincide se suman puntos a la casa correspondiente según la opción seleccionada
                if opciones[indice] == 'Valiente.':
                    respuestas['Gryffindor'] += 1
                elif opciones[indice] == 'Ambicioso.':
                    respuestas['Slytherin'] += 1
                elif opciones[indice] == 'Leal.':
                    respuestas['Hufflepuff'] += 1
                else:
                    respuestas['Ravenclaw'] += 1
                break
            else:
                print("Opción no válida. Por favor, ingresa un número entre 1 y 4.")

    # Determinar la casa con más respuestas
    mayor_respuesta = 0
    casa = ""
    for casa_actual in respuestas:
        if respuestas[casa_actual] > mayor_respuesta: #➡️ Aquí se compara si es la mayor puntuación
            mayor_respuesta = respuestas[casa_actual]
            casa = casa_actual  #➡️ Y se guarda la casa con el puntaje más alto
    print(f"¡Felicidades! Te pertenece la casa de {casa}.")


#➡️ Esta es mi función principal que incluye el menú
def iniciar_programa():
    opcion = None
    while opcion != 0:
        print("***  Ejercicio 4. Test del sombrero seleccionador de Harry Potter.  ***")
        print(
            "Este programa determina la casa (Gryffindor, Slytherin, Hufflepuff y Ravenclaw) a la que perteneces, de acuerdo a tus respuestas.")
        print("1) Iniciar test.")
        print("0) Salir.")
        opcion = int(input("Elige una opción: "))

        if opcion == 1:
            realizar_test()
        elif opcion == 0:
            print("¡Hasta luego!")
            return  # Salir del programa
        else:
            print("Opción no válida.")


#➡️ Y para finalizar llamo a la función principal
iniciar_programa()