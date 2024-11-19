print("*** Ejemplo de tuplas ***")

#fechas_cumple= ('12-19', '12-27', '01-10', '10-18', '11-01', '09-30', '08-25', '01-06', '10-21',  '04-11', '03-06', '08-02')
#print(fechas_cumple)

pi_serie= (4, -4/3, 4/5, -4/7, 4/9, -4/11, 4/13, -4/15, 4/17, -4/19, 4/21, -4/23)


print(f" La suma de los 3 primeros es de: {sum(pi_serie[0:2])}")
print(f" La suma de los 5 primeros es de: {sum(pi_serie[0:4])}")
print(f" La suma de los 8 primeros es de: {sum(pi_serie[0:7])}")
print(f" La suma de los 10 primeros es de: {sum(pi_serie[0:9])}")
print(f" La suma de todos es de: {sum(pi_serie)}")

print()
print("*** Ejemplo con coordenadas ***")
punto1= (1,0)
punto2= (5,3)

#punto1[0]= 2
#punto1.append(2)


print(f"Coordenas en tuplas: {punto1}{punto2}")
x1, y1= punto1
x2, y2= punto2

print()
print("---------------------------------------")
pendiente = (y2-y1)/(x2-x1)
b = y1 - pendiente * x1
print(f"La ecuación de la recta es: y = {pendiente}x {b}")

"""for i in fechas_cumple:
    print(i, end= ' ')"""