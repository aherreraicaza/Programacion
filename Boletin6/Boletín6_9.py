vector1 = [1, 2, 3]
vector2 = [-1, 0, 2]

num5 = 0
i = 0
for num in vector1:
    num2 = vector1[i]
    num3 = vector2[i]
    num4 = num2 * num3
    num5 = num5 + num4
    i = i + 1
print("producto_escalar: ", num5)

