"""
Nombre: Patricia Pérez Cruz
Fecha: 14 de octure de 2024
Descripción:
Mi primera información sobre como convertir de cadenas a int, float
y boolean mediante la interacción con consola.
"""

# Comentar sobre las funciones anidadas.
print("****   Datos de los alumnos    *****")
nombre = input("Ingresa el nombre: ") #⬅️Esto se dejo solo con el "input" ya que el "input" por si solo lo convierte a cadena
semestre = int(input("Ingresa el no. de semestre: ")) #⬅️Aquí si es necesario convertirlo a int ya que será un entero
promedio = float(input("Ingresa el promedio: ")) #⬅️También es necesario cambiarlo a flotante
es_mujer = input("¿Es mujer (Si/No)?: ")

# No es posible convertir directamente una cadena a un valor booleano.
# Por ello, utilizamos la misma variable, convertimos a  minúsculas y lo comparamos con la cadena "si".

es_mujer = es_mujer.lower() == "si" #⬅️Aquí ya se convierte correctamente

#⬆️ La conversión a un valor booleano no se puede hacer directamente, porque en lugar de tener un tipo
# de dato booleano que se pueda representar directamente como "True" o "False" se necesita evaluar la cadena ingresada
# (en cambio las conversiones a int y float son directas y se hacen con funciones)

# Se imprimen los datos del alumno.
# Comentar  qué es lo que realiza {promedio:.2f} probando con números diferentes.
print()
print(f"El alumno(a) {nombre} cursa el {semestre} semestre con un promedio de {promedio:.2f}. Además, es mujer: {es_mujer}.")