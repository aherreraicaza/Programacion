n = int(input("Introduce o número máximo das fichas: "))

for i in range(n + 1):
    for j in range(i, n + 1):
        print(f"{i}-{j}")
