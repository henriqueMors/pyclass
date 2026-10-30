import flet as ft

# Básico
# def main(page:ft.Page):
#     page.title = "Exemplo simples"
#     page.add(
#         ft.ElevatedButton(text="Botão Simples"),
#         ft.ElevatedButton("Botão Desabilitado", disabled=True)
#     )
#     page.update()

# Com ícones
# def main(page:ft.Page):
#     page.title = "Botão com Ícone"
#     page.add(
#         ft.ElevatedButton("Botão com Ícone", icon="access_time"),
#         ft.ElevatedButton("Botão com Ícone colorido", icon="park_rounded", icon_color="green400")
#     )
#     page.update()

# Com evento clique
# def main(page:ft.Page):
#     page.title = "Botão com clique"
    
#     def button_clicked(e):
#         b.data +=1
#         t.value = f"Botão clicado {b.data} vezes(s)"
#         page.update()
#     b = ft.ElevatedButton("Botão clicado", on_click=button_clicked, data=0)
#     t = ft.Text()
#     page.add(b, t)

# Conteúdo Customizado
def main(page:ft.Page):
    page.title = "Botão com conteúdo customizado"
    page.add(
        ft.Button(
            width=200,
            content=ft.Row(
                [
                    ft.Icon(ft.Icons.FAVORITE, color=ft.Colors.PINK, size=30),
                    ft.Icon(ft.Icons.AUDIOTRACK, color=ft.Colors.GREEN, size=30),
                    ft.Icon(ft.Icons.BEACH_ACCESS, color=ft.Colors.BLUE, size=30),
                    ft.Icon(ft.Icons.REFRESH, color=ft.Colors.BLUE_700, size=30),
                ],
            ),
        ),
        ft.Button(
            content = ft.Container(
                content = ft.Column(
                    [
                        ft.Text(value="Botão Composto", size=20),
                        ft.Text(value="Texto Secundário"),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=5
                ),
                padding=ft.Padding.all(10)
            )
        )
    )
ft.run(main)