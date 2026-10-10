# Sistema de login com Flet + hash com salt
import hashlib
import secrets
import hmac
import flet as ft

# "Banco de dados" de exemplo, na memória.
# Cada usuário guarda só o salt e o hash, nunca a senha.
banco = {}


# ---------------------------------------------------------------
# Parte 1 - Lógica de segurança (igual ao login_tkinter.py)
# ---------------------------------------------------------------

def gerar_hash(senha, salt):
    """Gera o hash da senha misturada com o salt."""
    hash_bytes = hashlib.pbkdf2_hmac("sha256", senha.encode(), salt, 100_000)
    return hash_bytes.hex()


def cadastrar_usuario(usuario, senha):
    """Cadastra o usuário. Devolve uma mensagem de erro, ou None se deu certo."""
    if not usuario or not senha:
        return "Preencha usuário e senha."
    if usuario in banco:
        return "Esse usuário já existe."
    salt = secrets.token_bytes(16)
    banco[usuario] = {"salt": salt, "hash": gerar_hash(senha, salt)}
    return None


def verificar_login(usuario, senha):
    """Devolve True se usuário e senha estiverem corretos."""
    dados = banco.get(usuario)
    if dados is None:
        return False
    hash_digitado = gerar_hash(senha, dados["salt"])
    return hmac.compare_digest(hash_digitado, dados["hash"])


# ---------------------------------------------------------------
# Parte 2 - Telas (Flet)
# ---------------------------------------------------------------

def main(page: ft.Page):
    page.title = "Sistema de Login"
    page.window.width = 420
    page.window.height = 480
    page.padding = 30

    def tela_login():
        page.controls.clear()  # apaga a tela anterior

        usuario_inp = ft.TextField(label="Usuário", autofocus=True)
        senha_inp = ft.TextField(label="Senha", password=True, can_reveal_password=True)
        mensagem = ft.Text("")  # área para avisos de erro ou sucesso

        def entrar(e):
            usuario = usuario_inp.value.strip()
            if verificar_login(usuario, senha_inp.value):
                tela_principal(usuario)
            else:
                mensagem.value = "Usuário ou senha incorretos."
                mensagem.color = ft.Colors.RED
                senha_inp.value = ""
                page.update()

        def cadastrar(e):
            erro = cadastrar_usuario(usuario_inp.value.strip(), senha_inp.value)
            if erro:
                mensagem.value = erro
                mensagem.color = ft.Colors.RED
            else:
                mensagem.value = "Usuário cadastrado! Agora clique em Entrar."
                mensagem.color = ft.Colors.GREEN
            page.update()

        # Apertar Enter no campo de senha também faz login
        senha_inp.on_submit = entrar

        page.add(
            ft.Text("Acesso ao sistema", size=22, weight=ft.FontWeight.BOLD),
            usuario_inp,
            senha_inp,
            ft.Row([
                ft.Button("Entrar", on_click=entrar),
                ft.Button("Cadastrar", on_click=cadastrar),
            ]),
            mensagem,
        )
        page.update()

    def tela_principal(usuario):
        page.controls.clear()
        dados = banco[usuario]

        page.add(
            ft.Text(f"Bem-vindo, {usuario}!", size=22, weight=ft.FontWeight.BOLD),
            ft.Text(f"Usuários cadastrados: {len(banco)}"),
            ft.Text("O que o sistema guardou sobre você:"),
            ft.Text(f"Salt: {dados['salt'].hex()}", color=ft.Colors.GREY, size=12),
            ft.Text(f"Hash: {dados['hash'][:32]}...", color=ft.Colors.GREY, size=12),
            ft.Text("Repare: a sua senha não está salva em lugar nenhum."),
            ft.Button("Sair", on_click=lambda e: tela_login()),
        )
        page.update()

    tela_login()


ft.run(main)