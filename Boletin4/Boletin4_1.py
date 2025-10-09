artigo = input("Introduce o nome do artigo: ")
vendas = int(input("Introduce o número de vendas anuais: "))

if vendas <= 100:
    tipo = "baixo"
elif vendas <= 500:
    tipo = "medio"
elif vendas <= 1000:
    tipo = "alto"
else:
    tipo = "primeira necesidade"

print(f"O artigo '{artigo}' é de tipo: {tipo}")
