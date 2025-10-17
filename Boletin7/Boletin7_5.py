texto = "Python Python Python"
vocales = "aeiou"
consonantes = "bcdfghjklmnpqrstvwxyz"
contador_vocales = 0
contador_consonantes = 0

for letra in texto.lower():
    if letra in vocales:
        contador_vocales = contador_vocales + 1
    elif letra in consonantes:
        contador_consonantes = contador_consonantes + 1

print("Número de vocales:", contador_vocales)
print("Número de consonantes:", contador_consonantes)
