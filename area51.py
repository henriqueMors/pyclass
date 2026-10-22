# 1. Lê as duas linhas
nomes = [n.strip() for n in input().split(",")]

# 2. map com float: converte cada preço de texto para número
precos = list(map(float, input().split()))

# 3. map com lambda: 10% de desconto, arredondado para 2 casas
com_desconto = list(map(lambda p: round(p * 0.9, 2), precos))


# 4. Função que monta a etiqueta
def criar_etiqueta(nome, preco):
    return f"{nome}: R$ {preco:.2f}"


# 5. map com duas listas: pega um nome e um preço de cada vez
etiquetas = list(map(criar_etiqueta, nomes, precos))

# 6. Mostra tudo
print(f"Preços: {precos}")
print(f"Com desconto: {com_desconto}")
for etiqueta in etiquetas:
    print(etiqueta)

