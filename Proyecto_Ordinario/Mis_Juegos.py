import Ahorcado_Juego
import Gato_Juego
import Cuatro_en_raya
import Carrera_de_caballos
import Batalla_Naval
import Letrero

def mostrar_menu():
    while True:
        print("1. Ahorcado")
        print("2. Juego del Gato")
        print("3. 4 en Raya")
        print("4. Juego de caballos")
        print("5. Batalla Naval")
        print("0. Salir")

        eleccion = input("Ingresa tu selección: ")

        if eleccion.isnumeric():
            eleccion = int(eleccion)

            if eleccion == 1:
                print("Iniciando Ahorcado...")
                Ahorcado_Juego.jugar_ahorcado()
                break
            elif eleccion == 2:
                print("Iniciando Juego del Gato...")
                Gato_Juego.jugar_gato()
                break
            elif eleccion == 3:
                print("Iniciando 4 en Raya...")
                Cuatro_en_raya.jugar_4_en_raya()
                break
            elif eleccion == 4:
                print("Iniciando Juego de caballos...")
                Carrera_de_caballos.jugar()
                break
            elif eleccion == 5:
                print("Iniciando Batalla Naval...")
                Batalla_Naval.jugar_batalla()
                break
            elif eleccion == 0:
                print("¡Hasta luego!")
                break
            else:
                print("Seleccion no válida, por favor elige una opción entre 0 y 3")
        else:
            print("Por favor, ingresa un número válido")


if __name__ == "__main__":
    Letrero.mostrar_mensaje("~~ JUEGOS ~~")
    mostrar_menu()
