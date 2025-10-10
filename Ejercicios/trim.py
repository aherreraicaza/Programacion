cadea = "                     unha cadea calquera "

print(cadea)
while cadea[0].isspace():
    cadea = cadea.removeprefix(' ')

while cadea[-1].isspace():
    cadea = cadea.removesuffix(' ')

print(cadea)