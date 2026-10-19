import pickle

class Cliente:
    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        
    def __str__(self):
        return f"{self.nome} {self.idade} anos - {self.cidade}"
    
clientes = [
    Cliente("Ana", 25, "São Paulo"),
    Cliente("Carlos", 30, "Rio de Janeiro"),
    Cliente("Fernanda", 22, "Curitiba")
]

# Salvar lista de clientes em arquivo pickle
with open("dados/clientes.pkl", "wb") as f:
    pickle.dump(clientes, f)
    
# Carregando os dados do arquivo pickle
with open("dados/clientes.pkl", "rb") as f:
    clientes_carregados = pickle.load(f)
    
for cliente in clientes_carregados:
    print(cliente)
    
# Adicionar cliente
novo_cliente = Cliente("Marcos", 28, "Porto Alegre")
clientes_carregados.append(novo_cliente)

with open("dados/clientes.pkl", "wb") as f:
    pickle.dump(clientes_carregados, f)