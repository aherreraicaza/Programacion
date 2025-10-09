numero = int(input("Introduce un número (0 para saír): "))

while numero != 0:
    for i in range(1, 11):
        print(numero, "x", i, "=", numero * i)
    numero = int(input("Introduce outro número (0 para saír): "))
