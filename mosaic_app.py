import flet as ft

from controls.mosaic_control import MosaicControl


def main(page: ft.Page):
    page.title = "Mosaic game"
    page.description = "Mosaic game implemented on Python+flet"
    page.author = "S.Sotnyk"
    page.add(game := MosaicControl())
    page.window_height = 800
    page.window_width = 900
    game.init_game()
    page.update()


ft.app(main, "Mosaic game")
