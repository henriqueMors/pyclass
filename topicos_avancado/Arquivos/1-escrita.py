name = input("Digite o nome do aluno:\n")

"""
Arquivos - Modos de Operação:

1-> Modo W - write
2-> Modo A - append
3-> Modo R - read
"""

# Implementação 1
# file = open("dados/names.txt", "a", encoding="utf-8")
# file.write(f"{name}\n")
# file.close()

# Implementação 2
with open("dados/names.txt", "a", encoding="utf-8") as file:
    file.write(f"{name}\n")