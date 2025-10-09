import math

print("Calculadora de superficies")
print("1…. Cadrado")
print("2…. Triángulo")
print("3…. Círculo")

opcion = input("Escolle unha opción (1-3): ")

if opcion == "1":
    lado = float(input("Introduce o lado do cadrado: "))
    area = lado ** 2
    print("A superficie do cadrado é:", area)
elif opcion == "2":
    base = float(input("Introduce a base do triángulo: "))
    altura = float(input("Introduce a altura do triángulo: "))
    area = (base * altura) / 2
    print("A superficie do triángulo é:", area)
elif opcion == "3":
    raio = float(input("Introduce o raio do círculo: "))
    area = math.pi * raio ** 2
    print("A superficie do círculo é:", area)
else:
    print("Opción incorrecta")
