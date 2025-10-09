m = int(input("Introduce a cantidade de números: "))

def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

for i in range(1, m + 1):
    numero = int(input(f"Introduce o número {i}: "))
    fact = factorial(numero)
    print(f"{i} - {numero}! = {fact}")
