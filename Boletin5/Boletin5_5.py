n = int(input("Introduce o valor de n: "))

for i in range(1, n + 1):
    triangular = 0
    for j in range(1, i + 1):
        triangular += j
    print(f"{i} - {triangular}")
