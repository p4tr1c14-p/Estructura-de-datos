import Juego_Ahorcado
import Juego_Gato
import Juego_4_en_raya


def mostrar_menu():
    while True:
        print("\n𝓔𝓵𝓲𝓳𝓮 𝓾𝓷𝓸 𝓭𝓮 𝓶𝓲𝓼 𝓳𝓾𝓮𝓰𝓸𝓼 🎳")
        print("1. Ahorcado")
        print("2. Juego del Gato")
        print("3. 4 en Raya")
        print("0. Salir")

        eleccion = input("Ingresa tu selección: ")

        if eleccion.isnumeric():
            eleccion = int(eleccion)

            if eleccion == 1:
                print("Iniciando Ahorcado...")
                Juego_Ahorcado.jugar_ahorcado()
                break
            elif eleccion == 2:
                print("Iniciando Juego del Gato...")
                Juego_Gato.jugar_gato()
                break
            elif eleccion == 3:
                print("Iniciando 4 en Raya...")
                Juego_4_en_raya.jugar_4_en_raya()
                break
            elif eleccion == 0:
                print("¡Hasta luego!")
                break
            else:
                print("Seleccion no válida, por favor elige una opción entre 0 y 3")
        else:
            print("Por favor, ingresa un número válido")


if __name__ == "__main__":
    mostrar_menu()
