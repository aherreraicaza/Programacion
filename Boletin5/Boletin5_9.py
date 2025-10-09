positivos = 0
negativos = 0
ceros = 0

for i in range(10):
    numero = int(input(f"Introduce o número {i+1}: "))
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        ceros += 1

print("Números positivos:", positivos)
print("Números negativos:", negativos)
print("Ceros:", ceros)
