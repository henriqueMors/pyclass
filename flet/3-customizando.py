import flet as ft

VERDE = ft.Colors.GREEN
AMARELO = ft.Colors.AMBER_900
VERMELHO = ft.Colors.RED


def main(page: ft.Page):
    page.title = "Cores com o mouse"
    page.padding = 0

    caixa = ft.Container(
        bgcolor=VERDE,
        expand=True,                          # ocupa a tela toda, como um fundo
        alignment=ft.Alignment.CENTER,
        content=ft.Text("Passe o mouse e clique", size=24, color=ft.Colors.WHITE),
    )

    def mudar_cor(cor):
        caixa.bgcolor = cor
        page.update()                         # sem isso a cor não muda na tela

    area = ft.GestureDetector(
        content=caixa,
        expand=True,
        mouse_cursor=ft.MouseCursor.CLICK,
        on_enter=lambda e: mudar_cor(AMARELO),      # ponteiro entrou
        on_exit=lambda e: mudar_cor(VERDE),         # ponteiro saiu
        on_tap_down=lambda e: mudar_cor(VERMELHO),  # apertou o botão
        on_tap_up=lambda e: mudar_cor(AMARELO),     # soltou o botão
        on_tap_cancel=lambda e: mudar_cor(AMARELO), # apertou, arrastou e soltou
    )

    page.add(area)


ft.run(main)