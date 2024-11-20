print("*** Calificacines del parcial ***")

def calificacion (calificaciones):
    promedio_parcial= (sum(calificaciones[0:3]))/3 #Sumo calificaciones de los tres parciales
    promedio_final = (promedio_parcial + calificaciones[3])/2 #Más el del ordinarip
    return promedio_parcial, promedio_final

calificaciones = (7,8,9,10)

promedio_parcial, promedio_final= calificacion(calificaciones)
print(f"El promedio de los parciales es: {promedio_parcial} y el promedio final es: {promedio_final}")