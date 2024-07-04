import flet as ft

def main(page: ft.Page):
    page.title = "Flet App"
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER


    user_label = ft.Text('Info')
    user_text = ft.TextField(value="введи текст", width=150, text_align=ft.TextAlign.CENTER)


    def get_info(e):
        user_label.value = user_text.value
        page.update()


    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.HOME, on_click=get_info),
                ft.Icon(ft.icons.BACK_HAND),
                ft.ElevatedButton(text='Click me', on_click=get_info),
                ft.OutlinedButton(text='hello', on_click=get_info),
                ft.Checkbox(label='Ты согласен?', value=True, on_change=get_info)
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                user_label,
                user_text
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )


ft.app(target=main)

