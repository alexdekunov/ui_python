import flet as ft
import sqlite3



def main(page: ft.Page):
    page.title = "Flet App"
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 350
    page.window_height = 400
    page.window_resizable = False


    def register(e):
        db = sqlite3.connect('base_users')

        cur = db.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    login TEXT,
                    pass TEXT
        )""")
        cur.execute(f"INSERT INTO users VALUES(NULL, '{user_login.value}', '{user_pass.value}')")

        db.close()

        user_login.value = ''
        user_pass.value = ''
        btn_reg.text = 'Добавлено'
        page.update()



    def validate(e):
        if all([user_login.value, user_pass.value]):
            btn_reg.disabled = False
        else:
            btn_reg.disabled = True

        page.update()


    user_login = ft.TextField(label='Логин', width=200, on_change=validate)
    user_pass = ft.TextField(label='Пароль', password=True, width=200, on_change=validate)
    btn_reg = ft.OutlinedButton(text='Добавить', width=200, on_click=register, disabled=True)

       

    page.add(
        ft.Row(
            [
                ft.Column(
                    [
                        ft.Text('Регистрация'),
                        user_login,
                        user_pass,
                        btn_reg
                    ]
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )


ft.app(target=main)
