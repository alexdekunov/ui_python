import flet as ft

def main(page: ft.Page):
    page.title = "Погода"
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    user_data = ft.TextField(label="Введите город", width=400)

    def get_info(e):
        pass


    def change_theme(e):
        page.theme_mode = 'light' if page.theme_mode == 'dark' else 'dark' # тернарное условие
        page.update()


    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.SUNNY, on_click=change_theme),
                ft.Text('Погодная программа')
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

  


ft.app(target=main)

