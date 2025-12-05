def nombres(tupla):
    listaorden = []
    for persona in tupla:
        orden = ""
        orden += persona[1]
        orden += " "
        orden += persona[2]
        orden += ". "
        orden += persona[0]
        listaorden.append(orden)

    print(listaorden)


# Exemplo de uso
tuplas_nomes = [("González", "Ana", "M"), ("López", "Juan", "P"), ("Martínez", "Lucía", "R")]
nombres(tuplas_nomes)