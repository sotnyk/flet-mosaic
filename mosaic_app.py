import flet as ft
import flet.canvas as cv
from flet_core import Paint

from controls.palette import game_palette
from controls.field_size_control import FieldSizeControl, fieldsize_to_width_height
from controls.who_play_control import WhoPlayControl
from mosaic_core.field import Field


class MosaicControl(ft.UserControl):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.who_play_a = ft.Ref[WhoPlayControl]()
        self.who_play_b = ft.Ref[WhoPlayControl]()
        self.field_size = ft.Ref[FieldSizeControl]()
        self.canvas = ft.Ref[ft.canvas.Canvas]()
        self.field: Field | None = None
        self.player_to_move = 0

    def build(self):
        title_row = ft.Row([WhoPlayControl(ref=self.who_play_a),
                            ft.ElevatedButton("New game"),
                            ft.Text("   ")],
                           alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
        middle_row = ft.Row([ft.canvas.Canvas(ref=self.canvas, width=500, height=500)])
        bottom_row = ft.Row([ft.Text("   "),
                             FieldSizeControl(ref=self.field_size),
                             WhoPlayControl(ref=self.who_play_b)],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
        # self.init_game()
        return ft.Column([title_row,
                          middle_row,
                          bottom_row])

    def init_game(self):
        width, height = fieldsize_to_width_height[self.field_size.current.group.current.value]
        self.field = Field(width=width, height=height, color_num=len(game_palette))
        self.player_to_move = 0
        self.draw_field()
        self.update()

    def draw_field(self):
        if self.field is None:
            return
        canvas = self.canvas.current
        cw = canvas.width
        ch = canvas.height
        cells = self.field.cells
        canvas.shapes.clear()
        for x in range(self.field.width):
            for y in range(self.field.height):
                color = Paint(color=game_palette[cells[x, y]])
                canvas.shapes.append(cv.Rect(x * cw / self.field.width,
                                             y * ch / self.field.height,
                                             cw / self.field.width,
                                             ch / self.field.height,
                                             paint=color))


def main(page: ft.Page):
    page.title = "Mosaic game"
    page.description = "Mosaic game implemented on Python+flet"
    page.author = "S.Sotnyk"
    page.add(game:=MosaicControl())
    game.init_game()


ft.app(main, "Mosaic game")
