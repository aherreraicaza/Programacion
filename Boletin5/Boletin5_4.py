inicio = int(input("Introduce o número inicial: "))
fin = int(input("Introduce o número final: "))

for numero in range(inicio, fin + 1):
    if numero % 2 == 0:
        print(numero)
