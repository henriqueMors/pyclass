import flet as ft


def create_icon_container(icon_name: str, on_favorite: callable, is_favorite: bool = False) -> ft.Container:
    def clicar_estrela(e):
        on_favorite(icon_name)
        # troca a estrela na hora: cheia = favorito, contorno = não favorito
        favorito_agora = favorite_button.icon == ft.Icons.STAR_OUTLINE
        favorite_button.icon = ft.Icons.STAR if favorito_agora else ft.Icons.STAR_OUTLINE
        favorite_button.update()

    favorite_button = ft.IconButton(
        icon=ft.Icons.STAR if is_favorite else ft.Icons.STAR_OUTLINE,
        icon_color=ft.Colors.AMBER,
        on_click=clicar_estrela,
    )

    return ft.Container(
        padding=ft.Padding.all(20),
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,   # muda sozinho no tema claro/escuro
        border_radius=ft.BorderRadius.all(10),
        alignment=ft.Alignment.CENTER,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Icon(getattr(ft.Icons, icon_name), size=50),   # texto -> ícone
                ft.Text(value=icon_name, size=11, text_align=ft.TextAlign.CENTER),
                favorite_button,
            ],
        ),
    )