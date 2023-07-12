import flet as ft


def main(page: ft.Page):
    page.add(
        ft.Row([
            ft.Column([ft.Container(ft.Text(f"{i}")) for i in range(3)],
                      alignment=ft.MainAxisAlignment.START, height=300),
            ft.Container(ft.Text("Game field"), width=300, height=300, bgcolor=ft.colors.TEAL,
                         alignment=ft.alignment.center),
            ft.Column([ft.Container(ft.Text(f"{i}")) for i in range(3)],
                      alignment=ft.MainAxisAlignment.END, height=300),
            ],
        )
    )
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER


ft.app(main, "Layout example")
