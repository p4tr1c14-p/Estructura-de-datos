
profesor = input("Es profesor de la UNSIJ (si/no): ")
alumno = input("Es alumno de la UNSIJ (si/no): ")

profesor = profesor.lower() == "si"
alumno = alumno.lower() == "si"

print(f"Forma parte de la UNSIJ?: {profesor or alumno}")