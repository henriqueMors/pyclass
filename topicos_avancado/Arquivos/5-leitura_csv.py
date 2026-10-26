with open("topicos_avancado/Arquivos/dados/cursos.csv", "r", encoding="utf-8") as file:
    for line in file:
        # linha = line.rstrip().split(",")
        # print(linha[0], linha[1])
        linguagem, categoria = line.rstrip().split(",")
        print(f"{linguagem}->{categoria}")