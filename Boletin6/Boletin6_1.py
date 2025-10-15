asignaturas = ["Matemáticas","Física", "Química", "Historia", "Língua"]

notas = []

for asignatura in asignaturas:
    nota =  float(input("Qué nota sacaste en " + asignatura))
    notas.append(nota)
i = 0
for m in asignaturas:
    print(asignaturas[i], notas[i])
    i= i + 1


