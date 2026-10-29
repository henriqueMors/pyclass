import flet as ft

def main(page:ft.Page):
    page.title = "Images Example"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 50

    t1 = ft.Text(
        value = "Imagens Importante",
        theme_style=ft.TextThemeStyle.DISPLAY_LARGE,
        bgcolor= ft.Colors.WHITE,
        style= ft.TextStyle(
            color = ft.Colors.BLACK,
            font_family="Arial",
            italic=True,
            weight=ft.FontWeight.W_300
        ),
        max_lines=2,
        overflow=ft.TextOverflow.ELLIPSIS,
        text_align=ft.TextAlign.CENTER
    )
    page.update()
    
    images = ft.Row(expand=1, wrap=False, scroll="always")
    for i in range(0, 30):
        images.controls.append(
            ft.Image(
                src=f"https://picsum.photos/200/200?{i}",
                width=200,
                height=200,
                fit=ft.BoxFit.NONE,
                repeat=ft.ImageRepeat.REPEAT,
                border_radius=ft.BorderRadius.all(40)
            )
        )
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(t1, images)
    page.update()

ft.run(main)