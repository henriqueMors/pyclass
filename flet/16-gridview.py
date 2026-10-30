import flet as ft

def main(page:ft.Page):
    page.title = "GridVIew Example"
    page.padding = 50
    page.update()
    
    images = ft.GridView(
        expand = 1,
        runs_count=5,
        max_extent=150,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5
    )
    
    page.add(images)
    
    for i in range(0, 60):
        images.controls.append(
            ft.Image(
                src=f"https://picsum.photos/150/150?{i}",
                fit=ft.BoxFit.COVER,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.BorderRadius.all(20)
            )
        )
    page.update()

ft.run(main, view=ft.AppView.WEB_BROWSER)