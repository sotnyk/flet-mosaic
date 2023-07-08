import flet as ft

from controls.mosaic_control import MosaicControl


def main(page: ft.Page):
    page.title = "Mosaic game"
    page.description = "Mosaic game implemented on Python+flet"
    page.author = "S.Sotnyk"
    page.add(game := MosaicControl())
    page.window_height = 1200
    page.window_width = 800
    game.init_game()


ft.app(main, "Mosaic game")
