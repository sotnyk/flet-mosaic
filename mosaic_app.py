import flet as ft

from controls.mosaic_control import MosaicControl


def main(page: ft.Page):
    page.title = "Mosaic game"
    page.description = "Mosaic game implemented on Python+flet"
    page.author = "S.Sotnyk"
    page.add(
        ft.Container(
            game := MosaicControl(),
            width=790,
            height=810,
        )
    )
    page.window_height = 810
    page.window_width = 800
    game.init_game()
    page.update()


ft.app(main, "Mosaic game", view=ft.WEB_BROWSER)
