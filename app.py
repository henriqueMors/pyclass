import flet as ft


def main(page: ft.Page):
    page.title = "Meu primeiro app"

    nome = ft.TextField(label="Seu nome")
    saudacao = ft.Text("Olá!")

    def clicar(e):
        saudacao.value = f"Olá, {nome.value}!"
        page.update()

    page.add(nome, ft.Button("Enviar", on_click=clicar), saudacao)

ft.run(main)