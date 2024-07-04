import flet as ft

def main(page: ft.Page):
    page.title = "Flet App"
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 350
    page.window_height = 400
    page.window_resizable = False
    



ft.app(target=main)

