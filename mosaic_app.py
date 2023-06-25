import flet as ft


def main(page: ft.Page):
    page.title = "Mosaic game"
    page.description = "Mosaic game implemented on Python+flet"
    page.author = "S.Sotnyk"
    page.add(ft.Text(value="Hello, world!"))


ft.app(main, "Mosaic game")
