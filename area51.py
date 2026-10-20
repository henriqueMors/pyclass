from collections import Counter

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