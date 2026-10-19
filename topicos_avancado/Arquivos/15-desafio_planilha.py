import pandas as pd
import os
from pathlib import Path

# 1-Importando os dados de todas as sheets
tb_clientes_dict = pd.read_excel("dados/clientes.xlsx", sheet_name=None)
print(tb_clientes_dict)
print(type(tb_clientes_dict))

#2-Criando a pasta 'planilhas_separadas' se não existir
pasta_saida = "dados/planilhas_separadas"
if not os.path.exists(pasta_saida):
    os.makedirs(pasta_saida)
    
#3-Separando as planilhas
for nome_aba, tabela in tb_clientes_dict.items():
    caminho_arquivo = os.path.join(pasta_saida, f"{nome_aba}.xlsx")
    tabela.to_excel(caminho_arquivo, index=False)
    
#4-Criando a pasta 'planilhas_consolidadas' se não existir
pasta_consolidada = "dados/planilhas_consolidadas"
if not os.path.exists(pasta_consolidada):
    os.makedirs(pasta_consolidada)
    
#5-Caminho para o arquivo
caminho_arquivo_consolidado = os.path.join(pasta_consolidada, "clientes.xlsx")

#6-Consolidar planilhas
with pd.ExcelWriter(caminho_arquivo_consolidado) as consolidada:
    for arquivo in Path(pasta_saida).glob("*.xlsx"):
        tabela = pd.read_excel(arquivo)
        tabela.to_excel(consolidada, sheet_name=arquivo.stem, index=False)