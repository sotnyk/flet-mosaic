import flet as ft


def main(page: ft.Page):
    page.add(
        ft.Row([
            ft.Column(
                [ft.Container(ft.Text(f"{i}"), alignment=ft.alignment.center) for i in range(3)],
                alignment=ft.alignment.top_right),
            ft.Container(ft.Text("Game field"), width=300, height=300, bgcolor=ft.colors.TEAL,
                         alignment=ft.alignment.center),
            ft.Column([ft.Container(ft.Text(f"{i}")) for i in range(3)],
                      alignment=ft.alignment.bottom_left),
        ])
    )


ft.app(main, "Layout example")
