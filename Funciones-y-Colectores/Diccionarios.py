print("*** Ejemplos de uso ***")

diccionario_profesor = {'nombre': 'Alberto', 'primer_apellido': 'Martinez', 'edad': 31, 'correo': 'alberto@unsij.com', 'cubo': 12}
#Se añaden elementos
diccionario_alumno = {}
diccionario_alumno['nombre'] = 'Patricia'
diccionario_alumno['apellido'] = 'Pérez'
diccionario_alumno['grupo'] = 303
diccionario_alumno['segundo_apellido'] = 'Cruz'
diccionario_alumno['materia'] = 'Estructura'

print(diccionario_profesor)
print(diccionario_alumno)

nombre_alumno = diccionario_alumno.get('nombre') #Primera forma
apellido_alumno = diccionario_alumno['apellido'] #Segunda forma
grupo_alumno = diccionario_alumno['grupo'] #Tercera forma
print()
print(nombre_alumno)
print(apellido_alumno)
print(grupo_alumno)
print()

print("*** Se modifican los elementos ***")
diccionario_alumno['nombre'] = "Cristal"
diccionario_alumno['grupo'] = 403
print()
print(diccionario_alumno)

print("*** Se eliminan los elementos 🦉🦉🦉***")
del diccionario_alumno['segundo_apellido']
diccionario_alumno.pop('grupo')
print("MODIFICACIÓN ******************")
print(diccionario_alumno)
print()

print("*** Se accede al por clave-valor, para acceder a ambos 👻👻***")
for clave, valor in diccionario_alumno.items():
    print(f"Clave: {clave} y Valor: {valor}")
    print()
print("*** Se accede al por valor 🐹🐹***")
for valor in diccionario_alumno.values():
    print(f"Valor: {valor}")
    print()
print("*** Se accede al por clave 🗝️🗝️***")
for clave in diccionario_alumno.keys():
    print(f"Clave: {clave}")
    print()
print("*** Combinacioones  con tuplas 🦄***")
diccionario_egresado = {}
diccionario_egresado = {'nombre': 'Marisol', ('primer_a', 'segundo_a'): "Ramirez y Cruz", 'edad': 23}

for clave, valor in diccionario_egresado.items():
    print(f"🐔🐔🐔Clave: {clave} y Valor: {valor}")
    print()

print("*** Diccionario informática 🐼🐼🐼***")
diccionario_informatica = {}
diccionario_informatica = {'grupo_303': {'no_alumnos': 12, 'no_materias': 5, 'promedio_grupal': 7.99}, 'grupo_503': {'no_alumnos': 8, 'no_materias': 5, 'promedio_grupal': 6.99},'grupo_703': {'no_alumnos': 5, 'no_materias': 5, 'promedio_grupal': 7.5}, 'grupo_903': {'no_alumnos': 2, 'no_materias': 5, 'promedio_grupal': 10} }

for grupo in enumerate(diccionario_informatica):
    print(f"Grupo: {grupo}")
    print()
#Acceder a lo elemnetos

promedio_303 = diccionario_informatica['grupo_303']['promedio_grupal']
promedio_503 = diccionario_informatica['grupo_503']['promedio_grupal']
promedio_703 = diccionario_informatica['grupo_703']['promedio_grupal']
promedio_903 = diccionario_informatica['grupo_903']['promedio_grupal']

print(promedio_303)
print(promedio_503)
print(promedio_703)
print(promedio_903)




