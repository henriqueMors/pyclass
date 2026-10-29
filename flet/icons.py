import flet as ft

def main(page:ft.Page):
    icons_row = ft.Row(
        controls=[
            ft.Icon(ft.Icons.FAVORITE, color=ft.Colors.PINK, size=30),
            ft.Icon(ft.Icons.AUDIO_FILE, color=ft.Colors.GREEN_400, size=30),
            ft.Icon(ft.Icons.BEACH_ACCESS, color=ft.Colors.BLUE, size=30),
            ft.Icon(ft.Icons.SETTINGS, color="#c1c1c1", size=30),
                        # Notícias e fontes
            ft.Icon(ft.Icons.NEWSPAPER, color=ft.Colors.BLUE_GREY, size=30),
            ft.Icon(ft.Icons.ARTICLE, color=ft.Colors.BLUE_GREY, size=30),
            ft.Icon(ft.Icons.RSS_FEED, color=ft.Colors.ORANGE, size=30),
            ft.Icon(ft.Icons.PUBLIC, color=ft.Colors.BLUE, size=30),
            ft.Icon(ft.Icons.LINK, color=ft.Colors.BLUE, size=30),

            # Busca e filtros
            ft.Icon(ft.Icons.SEARCH, color=ft.Colors.INDIGO, size=30),
            ft.Icon(ft.Icons.FILTER_LIST, color=ft.Colors.INDIGO, size=30),

            # Alertas
            ft.Icon(ft.Icons.NOTIFICATIONS, color=ft.Colors.AMBER, size=30),
            ft.Icon(ft.Icons.WARNING, color=ft.Colors.ORANGE, size=30),

            # Sentimento
            ft.Icon(ft.Icons.SENTIMENT_SATISFIED, color=ft.Colors.GREEN, size=30),
            ft.Icon(ft.Icons.SENTIMENT_NEUTRAL, color=ft.Colors.GREY, size=30),
            ft.Icon(ft.Icons.SENTIMENT_DISSATISFIED, color=ft.Colors.RED, size=30),

            # Tendência
            ft.Icon(ft.Icons.TRENDING_UP, color=ft.Colors.GREEN, size=30),
            ft.Icon(ft.Icons.TRENDING_DOWN, color=ft.Colors.RED, size=30),

            # Relatórios
            ft.Icon(ft.Icons.DASHBOARD, color=ft.Colors.TEAL, size=30),
            ft.Icon(ft.Icons.BAR_CHART, color=ft.Colors.TEAL, size=30),
            ft.Icon(ft.Icons.PIE_CHART, color=ft.Colors.TEAL, size=30),
            ft.Icon(ft.Icons.PICTURE_AS_PDF, color=ft.Colors.RED_700, size=30),
            ft.Icon(ft.Icons.CALENDAR_MONTH, color=ft.Colors.DEEP_PURPLE, size=30),

            # Ações
            ft.Icon(ft.Icons.REFRESH, color=ft.Colors.BLUE_700, size=30),
            ft.Icon(ft.Icons.DOWNLOAD, color=ft.Colors.BLUE_700, size=30),
            ft.Icon(ft.Icons.SHARE, color=ft.Colors.BLUE_700, size=30),
            ft.Icon(ft.Icons.EDIT, color=ft.Colors.AMBER, size=30),
            ft.Icon(ft.Icons.DELETE, color=ft.Colors.RED, size=30),
            ft.Icon(ft.Icons.ADD, color=ft.Colors.GREEN, size=30),

            # Usuário
            ft.Icon(ft.Icons.PERSON, color=ft.Colors.BROWN, size=30),
            ft.Icon(ft.Icons.LOGIN, color=ft.Colors.GREEN, size=30),
            ft.Icon(ft.Icons.LOGOUT, color=ft.Colors.RED, size=30),
            ft.Icon(ft.Icons.LOCK, color=ft.Colors.GREY, size=30),

            # Navegação
            ft.Icon(ft.Icons.HOME, color=ft.Colors.BLUE, size=30),
            ft.Icon(ft.Icons.MENU, color=ft.Colors.GREY, size=30),
            ft.Icon(ft.Icons.ARROW_BACK, color=ft.Colors.GREY, size=30),
            ft.Icon(ft.Icons.CLOSE, color=ft.Colors.GREY, size=30),

            # Status
            ft.Icon(ft.Icons.CHECK_CIRCLE, color=ft.Colors.GREEN, size=30),
            ft.Icon(ft.Icons.ERROR, color=ft.Colors.RED, size=30),
            ft.Icon(ft.Icons.INFO, color=ft.Colors.CYAN, size=30),
        ],
        #alignment=ft.MainAxisAlignment.CENTER,
        #spacing=20
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20,
        wrap=True, 
    )
    page.add(
        ft.Column(
            controls=[
                icons_row
            ]
        )
    )

ft.run(main)