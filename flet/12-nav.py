import flet as ft

def main(page:ft.Page):
    page.title = "NavigationBar"
    page.navigation_bar = ft.NavigationBar(
        destinations= [
            ft.NavigationBarDestination(ft.Icons.EXPLORE, label="Explore"),
            ft.NavigationBarDestination(ft.Icons.COMMUTE, label="Commute"),
            ft.NavigationBarDestination(ft.Icons.BOOKMARK_BORDER,
                                        label="Explore",
                                        selected_icon=ft.Icons.BOOKMARK
                                        ),
        ]
    )
    page.add(ft.Text("Bodybulder"))

ft.run(main)