def es_primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def factorial(num):
    if num == 0 or num == 1:
        return 1
    resultado = 1
    for i in range(2, num + 1):
        resultado *= i
    return resultado

def procesar_numeros(lista_numeros):

    primos = []
    for num in lista_numeros:
        if es_primo(num):
            primos.append(num)

    sumatorio = sum(lista_numeros)

    if lista_numeros:
        promedio = sumatorio / len(lista_numeros)
    else:
        promedio = 0

    factoriales = []
    for num in lista_numeros:
        factoriales.append(factorial(num))

    return primos, sumatorio, promedio, factoriales

numeros = [3, 4, 5, 6, 7, 8, 9, 10]
primos, sumatorio, promedio, factoriales = procesar_numeros(numeros)
print(f'Números primos: {primos}')
print(f'Sumatorio: {sumatorio}')
print(f'Promedio: {promedio}')
print(f'Factoriales: {factoriales}')