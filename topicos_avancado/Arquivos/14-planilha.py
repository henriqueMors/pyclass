import pandas as pd

#1-Importando os Dados
tb_clientes = pd.read_excel("dados/clientes.xlsx", sheet_name="Aba3")
print(tb_clientes)
print(type(tb_clientes))

#2-Adicionar coluna de index
tb_clientes = pd.read_excel("dados/clientes.xlsx", index_col=0)
print(tb_clientes)

#3-Importar Colunas Específicas
tb_clientes = pd.read_excel("dados/clientes.xlsx", usecols=[1,2])
print(tb_clientes)

#4-Exportando dados na planilha
tb_clientes_aba1 = pd.read_excel("dados/clientes.xlsx", sheet_name="Aba1")
tb_clientes_aba2 = pd.read_excel("dados/clientes.xlsx", sheet_name="Aba2")

with pd.ExcelWriter("dados/novos_clientes.xlsx") as nova_planilha:
    tb_clientes_aba1.to_excel(nova_planilha, sheet_name="Aba1", index=False)
    tb_clientes_aba2.to_excel(nova_planilha, sheet_name="Aba2", index=False)