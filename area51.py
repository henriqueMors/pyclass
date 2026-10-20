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
 
def regexDivisor(texto):
    textoDividido = re.split(r'\s+', texto)
    quantidade = len(textoDividido)
    print(quantidade)



textoCompleto = """
Relatório de links da semana

Na segunda-feira, a equipe publicou o novo portal em https://www.portal-noticias.example.com
e o blog técnico em http://blog.devteam.example.org/artigos/python-regex.
O formulário de inscrição está em https://inscricoes.cursoonline.example/turma-2026?origem=email
e a documentação da API foi movida para https://api.servicos.example.net/v2/docs.

Para suporte, acesse http://suporte.minhaempresa.example.com.br/chamados/novo
ou envie um e-mail para atendimento@minhaempresa.example.com.br (isto não é uma URL).
O painel de vendas fica em https://dashboard.vendas.example.com/relatorios/mensal#outubro,
e o espelho antigo ainda responde em http://legado.sistema.example:8080/login.

Links de parceiros:
- https://loja.parceiro-um.example.com/produtos/fone-bluetooth
- http://www.parceiro-dois.example.org
- https://imprensa.agencia.example.com.br/releases/2026/10/lancamento.html

Atenção: www.semprotocolo.example.com e ftp://arquivos.example.com não começam com http.
"""

regexDivisor(textoCompleto)