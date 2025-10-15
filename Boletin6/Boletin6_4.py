asignaturas = ["Matemáticas","Física", "Química", "Historia", "Língua"]
asignaturas_suspensas = []
notas = []

for asignatura in asignaturas:
    nota =  int(input("Qué nota sacaste en " + asignatura))
    if nota <5:
        notas.append(nota)
        asignaturas_suspensas.append(asignatura)
i = 0
for m in asignaturas_suspensas:
    print(asignaturas_suspensas[i], notas[i])
    i= i + 1