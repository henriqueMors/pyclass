# Sistema de login simples usando hash + salt
import hashlib  # gera o hash
import secrets  # gera o salt aleatório
import hmac     # compara hashes de forma segura

# "Banco de dados" de exemplo: um dicionário que fica na memória.
# Cada usuário guarda só o salt e o hash, nunca a senha.
banco = {}


def gerar_hash(senha, salt):
    """Gera o hash da senha misturada com o salt."""
    # pbkdf2_hmac repete o SHA-256 muitas vezes (100 mil),
    # o que deixa ataques de força bruta bem mais lentos.
    hash_bytes = hashlib.pbkdf2_hmac(
        "sha256",
        senha.encode(),   # texto -> bytes
        salt,
        100_000,
    )
    return hash_bytes.hex()  # bytes -> texto legível


def cadastrar():
    usuario = input("Novo usuário: ").strip()
    if usuario in banco:
        print("Esse usuário já existe.\n")
        return

    senha = input("Nova senha: ")

    salt = secrets.token_bytes(16)       # valor aleatório, diferente para cada usuário
    hash_senha = gerar_hash(senha, salt)

    banco[usuario] = {"salt": salt, "hash": hash_senha}
    print("Usuário cadastrado com sucesso!\n")


def login():
    usuario = input("Usuário: ").strip()
    senha = input("Senha: ")

    dados = banco.get(usuario)
    if dados is None:
        print("Usuário ou senha incorretos.\n")
        return

    # Refaz o hash com o MESMO salt que foi salvo no cadastro
    hash_digitado = gerar_hash(senha, dados["salt"])

    # Compara o hash digitado com o hash salvo
    if hmac.compare_digest(hash_digitado, dados["hash"]):
        print(f"Login liberado. Bem-vindo, {usuario}!\n")
    else:
        print("Usuário ou senha incorretos.\n")


def mostrar_banco():
    """Mostra o que está salvo, para você ver que não existe senha guardada."""
    if not banco:
        print("Nenhum usuário cadastrado.\n")
        return
    for usuario, dados in banco.items():
        print(f"Usuário: {usuario}")
        print(f"  Salt: {dados['salt'].hex()}")
        print(f"  Hash: {dados['hash']}")
    print()


# Programa principal: menu
while True:
    print("1 - Cadastrar")
    print("2 - Login")
    print("3 - Ver o que está salvo no banco")
    print("4 - Sair")
    opcao = input("Escolha: ").strip()
    print()

    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        login()
    elif opcao == "3":
        mostrar_banco()
    elif opcao == "4":
        print("Até mais!")
        break
    else:
        print("Opção inválida.\n")
