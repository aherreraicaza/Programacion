decenas = {
    10: "dez", 20: "vinte", 30: "trinta", 40: "corenta",
    50: "cincuenta", 60: "sesenta", 70: "setenta", 80: "oitenta", 90: "noventa"
}

unidades = {
    1: "un", 2: "dous", 3: "tres", 4: "catro", 5: "cinco",
    6: "seis", 7: "sete", 8: "oito", 9: "nove"
}

especiales = {
    11: "once", 12: "doce", 13: "trece", 14: "catorce",
    15: "quince", 16: "dezaseis", 17: "dezasete",
    18: "dezaoito", 19: "dezanove"
}

numero = int(input("Introduce un número entre 1 e 99: "))

if numero == 10 or numero in decenas:
    print(decenas[numero])
elif 11 <= numero <= 19:
    print(especiales[numero])
else:
    d = (numero // 10) * 10
    u = numero % 10
    if u == 0:
        print(decenas[d])
    else:
        print(f"{decenas[d]} e {unidades[u]}")
