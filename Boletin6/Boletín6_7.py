palabra = str(input("Introduce una palabra"))
a = 0
e = 0
i = 0
o = 0
u = 0
palabra_minuscula = palabra.lower()

for letra in palabra_minuscula:
    if letra == 'a':
        a = a+1
    elif letra =='e':
        e = e+1
    elif letra == 'i':
        i = i+1
    elif letra == 'o':
        o = o+1
    elif letra == 'u':
        u = u+1
print("Número de veces que contiene cada vocal")
print("a:", a)
print("e:", e)
print("i:", i)
print("o:", o)
print("u:", u)


#hola que tal