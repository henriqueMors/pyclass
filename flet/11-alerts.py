import flet as ft

def main(page:ft.Page):
    page.title = "Usando AlertDialogs e Banner"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    action_button_style = ft.ButtonStyle(color=ft.Colors.BLUE)
    
    def close_banner(e):
        page.pop_dialog()
        page.add(ft.Text("Clicado: "+e.control.content))
    
    def show_banner(e):
        banner = ft.Banner(                     # ← cria um banner NOVO a cada clique
            bgcolor=ft.Colors.AMBER_100,
            leading=ft.Icon(ft.Icons.WARNING_AMBER_ROUNDED, color=ft.Colors.AMBER, size=40),
            content=ft.Text(
                value="Oops, there were some errors while trying to delete the file.",
                color=ft.Colors.BLACK,
            ),
            actions=[
                ft.TextButton("Retry", style=action_button_style, on_click=close_banner),
                ft.TextButton("Ignore", style=action_button_style, on_click=close_banner),
                ft.TextButton("Cancel", style=action_button_style, on_click=close_banner),
            ],
        )
        page.show_dialog(banner)
    
    def show_non_modal_dialog(e):
        dlg = ft.AlertDialog(
            title=ft.Text("Hi, this is a non-modal dialog!"),
            on_dismiss=lambda e: page.add(ft.Text("Non-modal dialog dismissed"))
        )
        page.show_dialog(dlg)
        
    def show_modal_dialog(e):
        def handle_close(e):
            page.pop_dialog()
            page.add(ft.Text(f"Modal dialog closed with action: {e.control.content}"))
    
        dlg_modal = ft.AlertDialog(
            modal = True,
            title=ft.Text("Please Confirm?"),
            content=ft.Text("DO yo really want to delete all those files?"),
            actions=[
                ft.TextButton("Yes", on_click=handle_close),
                ft.TextButton("No", on_click=handle_close)
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=lambda e: page.add(ft.Text("Modal dialog dismissed"))
        )
    
        page.show_dialog(dlg_modal)
        
    page.add(
        ft.Column(
            controls = [
                ft.Button("Open non-modal dialog", on_click=show_non_modal_dialog),
                ft.Button("Open modal dialog", on_click=show_modal_dialog),
                ft.Button("Show banner", on_click=show_banner),
            ]
        )
    )

ft.run(main)