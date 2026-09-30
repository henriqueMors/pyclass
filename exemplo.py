entregas = [
    {"nome": "Login",         "status": "concluída"},
    {"nome": "API Pagamento", "status": "atrasada"},
    {"nome": "Relatório",     "status": "concluída"},
    {"nome": "Dashboard",     "status": "em andamento"},
    {"nome": "Integração",    "status": "atrasada"},
]

for e in entregas:
    print(f"{e['nome']:<15} -> {e['status']}")