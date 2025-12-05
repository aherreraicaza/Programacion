def maiores(nums, k):
    mas = []
    menos = []
    igual = []

    for n in nums:
        if n > k:
            mas.append(n)
        elif n < k:
            menos.append(n)
        elif n == k:
            igual.append(n)

    return mas, menos, igual


def multiplos(nums, k):
    multiples = []

    for n in nums:
        if n % k == 0:
            multiples.append(n)

    return multiples


# Ejemplo de uso
k = 4
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

mas, menos, igual = maiores(nums, k)
print(mas, "son mayores a", k)
print(menos, "son menores a", k)
print(igual, "son iguales a", k)

lista_multiplos = multiplos(nums, k)
print(lista_multiplos, "son múltiplos de", k)