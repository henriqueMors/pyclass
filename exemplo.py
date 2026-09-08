nomes = []

while True:
    novo_nome = input("Digite o nome a ser adicionado (ou pressione Enter para sair): ")
    if novo_nome == "":
        break
    nomes.append(novo_nome)

print(nomes)