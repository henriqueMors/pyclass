import flet as ft
from time import sleep

def main(page:ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    
    pb = ft.ProgressBar(width=400)
    status = ft.Text("Aguarde...")
    
    page.add(
        ft.Text("Progresso Linear", theme_style=ft.TextThemeStyle.HEADLINE_SMALL),
        ft.Column([status, pb]),
        ft.Text("Progresso Indeterminado", theme_style=ft.TextThemeStyle.HEADLINE_SMALL),
        ft.ProgressBar(width=400, color=ft.Colors.AMBER, bgcolor="#eeeeee"),
    )
    
    for i in range(0, 101):
        pb.value = i*0.01
        status.value = f"Carregando... {i}%"
        sleep(0.1)
        page.update()

    status.value = "Concluído!"
    page.update()

ft.run(main)