class Aluno:
    def __init__(self, numero, nome, nota):
        self.numero = numero
        self.nome = nome
        self.nota = nota

    def classificar(self):
        if self.nota >= 7:
            return "Aprovado"
        elif self.nota >= 5:
            return "Recuperação"
        else:
            return "Reprovado"

    def __str__(self):
        return f"{self.numero} - {self.nome}: {self.nota} ({self.classificar()})"

def media_turma(alunos):
    total = 0
    for aluno in alunos:
        total += aluno.nota
    return total / len(alunos)

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
