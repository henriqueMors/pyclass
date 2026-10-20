"""" from collections import Counter

noticias = [
    {"veiculo": "Folha",   "titulo": "Claro anuncia nova rede 5G em São Paulo"},
    {"veiculo": "G1",      "titulo": "Operadoras ampliam cobertura no interior"},
    {"veiculo": "Estadão", "titulo": "Claro e Vivo disputam clientes de fibra"},
    {"veiculo": "G1",      "titulo": "Claro registra alta no lucro do trimestre"},
    {"veiculo": "Folha",   "titulo": "Anatel multa operadora por falhas"},
]

marca = str(input("Qual nome do cliente? \n"))

# 1. Filtra só as notícias que citam a marca
mencoes = [n for n in noticias if marca.lower() in n["titulo"].lower()]

print(f"'{marca}' foi citada {len(mencoes)} vezes hoje.\n")

# 2. Conta por veículo
print("Por veículo:")
for veiculo, total in Counter(n["veiculo"] for n in mencoes).most_common():
    print(f"  {veiculo}: {total}")

# 3. Lista numerada
print("\nLista de menções:")
for i, n in enumerate(mencoes, start=1):
    print(f"  {i}. [{n['veiculo']}] {n['titulo']}")




def regressivo(n):
    print("[regressor] começou")
    for i in range(n, 0, -1):
        print(f"[regressor] vou entregar o {i}")
        yield i
        print(f"[regressor] voltei depois do {i}")
    print("[regressor] acabou")


num = int(input("Digite o regressor: \n"))

for numero in regressivo(num):
    print(f"[for] recebi o {numero}") """


import re
 
def validar_senha(senha):
    return (
        len(senha) >= 8
        and re.search(r"[A-Z]", senha) is not None
        and re.search(r"[a-z]", senha) is not None
        and re.search(r"\d", senha) is not None
    )

senha = input("Digite uma senha: ")

if validar_senha(senha):
    print("Senha válida!")
else:
    print("Senha inválida. Use pelo menos 8 caracteres, com letra maiúscula, letra minúscula e número.")
