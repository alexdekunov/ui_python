import flet as ft

def main(page: ft.Page):
    page.title = "Flet App"
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 350
    page.window_height = 400
    page.window_resizable = False

    user_login = ft.TextField(label='Логин', width=200)
    user_pass = ft.TextField(label='Пароль', width=200)
    btn_reg = ft.OutlinedButton(text='Добавить', width=200, on_click=register, disabled=True)


ft.app(target=main)