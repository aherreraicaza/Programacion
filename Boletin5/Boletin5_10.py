while True:
    base = float(input("Introduce a base do rectángulo (positiva): "))
    if base > 0:
        break
    print("Erro: a base debe ser un número positivo.")

while True:
    altura = float(input("Introduce a altura do rectángulo (positiva): "))
    if altura > 0:
        break
    print("Erro: a altura debe ser un número positivo.")

area = base * altura

print(f"O área do rectángulo é: {area}")
