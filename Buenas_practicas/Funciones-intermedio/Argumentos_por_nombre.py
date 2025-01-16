


def imprimir_alumno(nombre: str= "Hola", edad: int = 20, matr: int= 1243, grupo: int = 9, semestre: int= 8) -> None:
    print(f"Datos personales: \n nombre: {nombre} \n edad: {edad} \n matricula: {matr} \n grupo: {grupo} \n semestre: {semestre} " )

def main ()-> None:

    NOMBRE = "PATRICIA"
    EDAD = 19
    MATRICULA = 12345
    GRUPO = 303
    SEMESTRE = 3


    imprimir_alumno(semestre= SEMESTRE)
    #imprimir_alumno(nombre="Sofia", matr=456, edad=20, semestre=3)
    #imprimir_alumno(nombre="Sofia", 31, 123, grupo= 303, semestre= 3)


if __name__ == '__main__':
        main()


"""

def imprimir_alumno(nombre: str, edad: int, matr: int, grupo: int, semestre: int = 3) -> None:
    print(f"Datos personales: \n nombre: {nombre} \n edad: {edad} \n matricula: {matr} \n grupo: {grupo} \n semestre: {semestre} " )

def main ()-> None:
    NOMBRE = "PATRICIA"
    EDAD = 19
    MATRICULA = 12345
    GRUPO = 303
    

    imprimir_alumno(NOMBRE, EDAD, MATRICULA, GRUPO)


if __name__ == '__main__':
        main()

"""