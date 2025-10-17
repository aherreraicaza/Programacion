texto = ("www. pythonparatodos. com")

texto_sin_espacios = texto.replace(" ","")

partes = texto_sin_espacios.split(".", 1)

parte1 = partes[0]
parte2 = partes[1]

print("Primera parte", parte1)
print("Segunda parte", parte2)

texto_concatenado = parte1 + "." + parte2

print("Texto concatenadado:", texto_concatenado)