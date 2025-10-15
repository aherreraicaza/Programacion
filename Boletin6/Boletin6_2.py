numeros_ganadores = []
print("Introduce los 6 números ganadores de la Lotería Primitiva")
for i in range(1,7):
    numero = int(input("Introduce número ganador"))
    if numero >=1 and numero <=49:

        numeros_ganadores.append(numero)
    else:
        print("error")
print(numeros_ganadores)





