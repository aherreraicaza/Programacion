letras = "TRWAGMYFPDXBNJZSQVHLCKE"

dni = int(input("Introduce o número do DNI: "))

print(dni, letras[dni % 23])
