
def imprimir_alumno(nombre: str, edad: int, matr: int, grupo: int, semestre: int) -> None:
    print(f"Datos personales: \n nombre: {nombre} \n edad: {edad} \n matricula: {matr} \n grupo: {grupo} \n semestre: {semestre} " )

def main ()-> None:
    NOMBRE = "PATRICIA"
    EDAD = 19
    MATRICULA = 12345
    GRUPO = 303
    SEMESTRE = 3

    imprimir_alumno(NOMBRE, EDAD, MATRICULA, GRUPO, SEMESTRE)


if __name__ == '__main__':
        main()
