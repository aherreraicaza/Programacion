abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
          "n","o","p","q","r","s","t","u","v","w","x","y","z"]
multiplos = []

for letra in abecedario:
    if abecedario.index(letra) % 3 != 2:
        multiplos.append(letra)
print(multiplos)