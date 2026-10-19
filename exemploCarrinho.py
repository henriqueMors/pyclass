carrinho = [item.strip() for item in input().split(",")]

caixa = iter(carrinho)

print(f"Primeiro item: {next(caixa)}")
print(f"Segundo item: {next(caixa)}")

for item in caixa:
    print(f"Restante: {item}")

print(next(caixa, "Carrinho vazio"))