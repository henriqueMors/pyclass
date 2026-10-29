import flet as ft

def main(page:ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    
    # Adicionando a imagem
    img = ft.Image(
        src="https://www.w3schools.com/w3images/lights.jpg",
        border_radius=ft.BorderRadius.all(40),
        width=1000,
        height=1000,
        tooltip="Imagem Teste"
    )
    
    page.add(img)
    page.update()

ft.run(main)