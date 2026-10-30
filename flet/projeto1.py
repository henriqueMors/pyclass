import flet as ft
from icon_container import create_icon_container

LIMITE_RESULTADOS = 200          # evita travar a tela com milhares de ícones

is_dark_mode = False
icons_grid = None
favorites = []
favorites_grid = None


def main(page: ft.Page):

    def toggle_dark_mode(event):
        global is_dark_mode
        is_dark_mode = not is_dark_mode
        page.theme_mode = ft.ThemeMode.DARK if is_dark_mode else ft.ThemeMode.LIGHT
        page.update()

    def favorite_icon(icon_name: str):
        if icon_name in favorites:
            favorites.remove(icon_name)
        else:
            favorites.append(icon_name)

    def show_favorites(event=None):
        page.clean()
        favorites_grid.controls = []

        for icon_name in favorites:
            favorites_grid.controls.append(create_icon_container(
                icon_name=icon_name,
                on_favorite=favorite_icon,
                is_favorite=True,
            ))

        layout = ft.Column(
            expand=True,
            controls=[
                ft.Text("Ícones favoritos",
                        style=ft.TextStyle(size=24, weight=ft.FontWeight.BOLD)),
                ft.Text("Nenhum favorito ainda." if not favorites else f"{len(favorites)} favorito(s)"),
                favorites_grid,
                ft.Button("Voltar", on_click=show_search_page),
            ],
        )
        page.add(layout)

    def search_icons(event: ft.ControlEvent):
        search_value = event.control.value.strip().upper()
        icons_grid.controls = []

        encontrados = [icon.name for icon in ft.Icons if search_value in icon.name]

        for icon_name in encontrados[:LIMITE_RESULTADOS]:
            icons_grid.controls.append(create_icon_container(
                icon_name=icon_name,
                on_favorite=favorite_icon,
                is_favorite=icon_name in favorites,
            ))

        resultado.value = f"{len(encontrados)} ícone(s) encontrado(s)"
        if len(encontrados) > LIMITE_RESULTADOS:
            resultado.value += f" - mostrando os {LIMITE_RESULTADOS} primeiros"
        page.update()

    def show_search_page(event=None):
        global icons_grid
        global favorites_grid
        global resultado

        page.clean()
        search_bar = ft.TextField(
            prefix_icon=ft.Icons.SEARCH,
            hint_text="Digite algo para buscar (em inglês) e aperte Enter...",
            on_submit=search_icons,
        )

        resultado = ft.Text("")

        icons_grid = ft.GridView(
            expand=True,
            max_extent=200,
            controls=[],
            child_aspect_ratio=1.0,
            spacing=10,
            run_spacing=10,
        )

        favorites_grid = ft.GridView(
            expand=True,
            max_extent=200,
            controls=[],
            child_aspect_ratio=1.0,
            spacing=10,
            run_spacing=10,
        )

        layout = ft.Column(
            expand=True,
            controls=[
                search_bar,
                resultado,
                icons_grid,
                ft.Row([
                    ft.Button("Alternar Tema Visual", on_click=toggle_dark_mode),
                    ft.Button("Ver Favoritos", on_click=show_favorites),
                ]),
            ],
        )
        page.add(layout)

    page.title = "Buscador de Ícones"
    page.theme_mode = ft.ThemeMode.LIGHT
    show_search_page()


ft.run(main)