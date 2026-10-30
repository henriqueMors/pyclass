import flet as ft

def main(page:ft.Page):
    page.title = "Cartão de Aniversário"
    
    card_content = ft.Column(
        [
            ft.ListTile(
                leading=ft.Icons.CAKE,
                title=ft.Text("Feliz aniversário!", size=25, weight="bold"),
                subtitle=ft.Text("Que seu dia seja repleto de alegrias, risadas e muito amor.")
            ),
            ft.Row(
                [
                    ft.TextButton("Compartilhar", 
                            on_click=lambda _: page.add(ft.Text("Mensagem compartilhada com sucesso",
                                                                color=ft.Colors.GREEN_600))),
                    ft.TextButton("Enviar votos"),
                    ft.TextButton("Loucura premiada")
                ],
                alignment=ft.MainAxisAlignment.END
            )
        ]
    )
    
    page.add(
        ft.Card(
            content=ft.Container(
                content=card_content,
                width=400,
                padding=20
            )
        )
    )

ft.run(main)