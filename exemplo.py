# Programa principal
alunos = []   # começa vazia

print("Cadastro de alunos (deixe o nome em branco para encerrar)\n")

while True:
    nome = input("Nome completo: ").strip()
    if nome == "":           # nome vazio = terminou o cadastro
        break

    numero = len(alunos) + 1   # número automático: 1, 2, 3...

    try:
        nota = float(input("Nota: ").replace(",", "."))
    except ValueError:
        print("Nota inválida. Aluno não cadastrado.\n")
        continue             # volta para o início do laço

    alunos.append(Aluno(numero, nome, nota))
    print(f"Aluno {numero} cadastrado!\n")

# Depois do cadastro, mostra o resultado
if alunos:
    print("\n--- Resultado ---")
    for aluno in alunos:
        print(aluno)
    print(f"Média da turma: {media_turma(alunos):.1f}")
else:
    print("Nenhum aluno cadastrado.")