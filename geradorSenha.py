import secrets
import string


def perguntar_tamanho():
    """Pergunta quantos caracteres a senha deve ter."""
    while True:
        try:
            tamanho = int(input("Quantos caracteres deseja? "))
            if tamanho < 4:
                print("Use pelo menos 4 caracteres.")
            else:
                return tamanho
        except ValueError:
            print("Digite um número inteiro.")


def perguntar_sim_nao(pergunta):
    """Faz uma pergunta de sim ou não e devolve True ou False."""
    while True:
        resposta = input(pergunta + " (s/n): ").strip().lower()
        if resposta in ("s", "sim"):
            return True
        if resposta in ("n", "nao", "não"):
            return False
        print("Responda com s ou n.")


def gerar_senha(tamanho, usar_especiais, usar_numeros):
    """Monta a senha conforme as opções escolhidas."""
    # Letras minúsculas e maiúsculas sempre entram
    grupos = [string.ascii_lowercase, string.ascii_uppercase]

    if usar_numeros:
        grupos.append(string.digits)        # 0123456789
    if usar_especiais:
        grupos.append(string.punctuation)   # !@#$%&*...

    # Garante pelo menos 1 caractere de cada grupo escolhido
    senha = [secrets.choice(grupo) for grupo in grupos]

    # Completa o resto com caracteres de qualquer grupo
    todos = "".join(grupos)
    while len(senha) < tamanho:
        senha.append(secrets.choice(todos))

    # Embaralha para os caracteres garantidos não ficarem sempre no início
    secrets.SystemRandom().shuffle(senha)

    return "".join(senha)


# Programa principal
tamanho = perguntar_tamanho()
especiais = perguntar_sim_nao("Deve conter caracteres especiais?")
numeros = perguntar_sim_nao("Deve conter números?")

senha = gerar_senha(tamanho, especiais, numeros)
print("Sua senha:", senha)