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
 
PADRAO_CPF = r"\d{3}\.\d{3}\.\d{3}-\d{2}"
 
 
def formato_valido(cpf):
    """True se o texto estiver exatamente no formato 000.000.000-00."""
    return re.fullmatch(PADRAO_CPF, cpf) is not None
 
 
def extrator_url(url)
    texto = url
        