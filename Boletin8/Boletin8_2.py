def encajan(ficha1, ficha2):
    return ficha1[0] == ficha2[0] or ficha1[0] == ficha2[1] or ficha1[1] == ficha2[0] or ficha1[1] == ficha2[1]


f1 = (3, 4)
f2 = (5, 4)

f3 = (6, 4)
f4 = (5, 1)

print(encajan(f1, f2))
print(encajan(f3, f4))