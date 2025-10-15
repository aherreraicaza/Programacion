palabra = str(input("Introduce una palabra"))

palindromo = palabra[::-1]

if palabra == palindromo:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
