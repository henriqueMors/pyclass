# Sistema de login com interface gráfica (tkinter) + hash com salt
import hashlib
import secrets
import hmac
import tkinter as tk
from tkinter import messagebox  # janelinhas de aviso (erro, sucesso)

# "Banco de dados" de exemplo, na memória.
# Cada usuário guarda só o salt e o hash, nunca a senha.
banco = {}


# ---------------------------------------------------------------
# Parte 1 - Lógica de segurança (a mesma do login_hash.py)
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
# Parte 2 - Telas (tkinter)
# ---------------------------------------------------------------

def limpar_janela():
    """Apaga tudo que está na janela, para desenhar a próxima tela."""
    for elemento in window.winfo_children():
        elemento.destroy()


def tela_login():
    limpar_janela()
    window.title("Login")

    frame = tk.Frame(window)
    frame.pack(padx=20, pady=20, fill="x", expand=True)

    tk.Label(frame, text="Acesso ao sistema", font=("Arial", 14, "bold")).pack(pady=(0, 10))

    tk.Label(frame, text="Usuário").pack(anchor="w")
    usuario_inp = tk.Entry(frame)
    usuario_inp.pack(fill="x")

    tk.Label(frame, text="Senha").pack(anchor="w", pady=(8, 0))
    senha_inp = tk.Entry(frame, show="*")  # show="*" esconde a senha
    senha_inp.pack(fill="x")

    def entrar():
        usuario = usuario_inp.get().strip()
        senha = senha_inp.get()
        if verificar_login(usuario, senha):
            tela_principal(usuario)
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos.")
            senha_inp.delete(0, tk.END)  # limpa o campo de senha

    def cadastrar():
        usuario = usuario_inp.get().strip()
        senha = senha_inp.get()
        erro = cadastrar_usuario(usuario, senha)
        if erro:
            messagebox.showerror("Erro", erro)
        else:
            messagebox.showinfo("Sucesso", "Usuário cadastrado! Agora clique em Entrar.")

    botoes = tk.Frame(frame)
    botoes.pack(pady=15)
    tk.Button(botoes, text="Entrar", width=10, command=entrar).pack(side="left", padx=5)
    tk.Button(botoes, text="Cadastrar", width=10, command=cadastrar).pack(side="left", padx=5)

    # Apertar Enter no teclado também faz login
    window.bind("<Return>", lambda evento: entrar())
    usuario_inp.focus()


def tela_principal(usuario):
    limpar_janela()
    window.unbind("<Return>")  # Enter não faz mais login nesta tela
    window.title("Sistema")

    frame = tk.Frame(window)
    frame.pack(padx=20, pady=20, fill="both", expand=True)

    tk.Label(frame, text=f"Bem-vindo, {usuario}!", font=("Arial", 14, "bold")).pack(pady=(0, 10))
    tk.Label(frame, text=f"Usuários cadastrados: {len(banco)}").pack(anchor="w")

    # Mostra o que está salvo no banco para este usuário (só para estudo)
    dados = banco[usuario]
    tk.Label(frame, text="O que o sistema guardou sobre você:").pack(anchor="w", pady=(10, 0))
    tk.Label(frame, text=f"Salt: {dados['salt'].hex()}", fg="gray").pack(anchor="w")
    tk.Label(frame, text=f"Hash: {dados['hash'][:32]}...", fg="gray").pack(anchor="w")
    tk.Label(frame, text="Repare: a sua senha não está salva em lugar nenhum.").pack(anchor="w", pady=(5, 0))

    tk.Button(frame, text="Sair", width=10, command=tela_login).pack(pady=15)


# ---------------------------------------------------------------
# Programa principal
# ---------------------------------------------------------------
window = tk.Tk()
window.geometry("420x300")
tela_login()
window.mainloop()