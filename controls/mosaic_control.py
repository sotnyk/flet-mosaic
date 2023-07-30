import threading
import time

import flet as ft
from flet import canvas as cv
from flet_core import Paint

from controls.field_size_control import FieldSizeControl, fieldsize_to_width_height
from controls.move_selector_control import MoveSelectorControl
from controls.palette import game_palette
from controls.who_play_control import WhoPlayControl, WhoPlay
from mosaic_core.field import Field
from mosaic_core.thinkers import RandomThinker, GreedyThinker, ThinkerBase


class MosaicControl(ft.UserControl):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.running = False
        self.cur_player_index = 0
        self.th: threading.Thread|None = None
        self.who_play_a = ft.Ref[WhoPlayControl]()
        self.who_play_b = ft.Ref[WhoPlayControl]()
        self.field_size = ft.Ref[FieldSizeControl]()
        self.canvas = ft.Ref[ft.canvas.Canvas]()
        self.field: Field | None = None
        self.player_to_move = 0
        self.players_num = 2
        self.homes: list[tuple[int, int]] = []
        self.thinkers: list[ThinkerBase] = []

    def did_mount(self):
        self.running = True
        self.th = threading.Thread(target=self.update_timer, args=(), daemon=True)
        self.th.start()

    def will_unmount(self):
        self.running = False

    def update_timer(self):
        while self.running:
            if not self.thinkers:
                # Not initialized yet
                time.sleep(1)
                continue
            who_play = self.who_play_a.current.selected_value() if self.player_to_move == 0 \
                else self.who_play_b.current.selected_value()
            home = self.homes[self.player_to_move]
            if who_play == WhoPlay.HUMAN:
                self.update()
                time.sleep(1)
                continue
            elif who_play == WhoPlay.LEVEL1:
                thinker = self.thinkers[1]
            elif who_play == WhoPlay.LEVEL2:
                thinker = self.thinkers[2]
            else:
                raise ValueError(f"Not implemented who_play={who_play}")
            move = thinker.think(self.field, player_home=home)
            self.field.make_move(home, self.homes, move)
            self.player_to_move = (self.player_to_move + 1) % self.players_num
            self.draw_field()
            self.update()
            time.sleep(1)

    def build(self):
        field_size = 640
        title_row = ft.Row([WhoPlayControl(ref=self.who_play_a, expand=True),
                            ft.ElevatedButton("New game", expand=True),
                            ft.Text("   ", expand=True)],
                           alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
        middle_row = ft.Row([
            ft.Container(MoveSelectorControl(height=field_size, alignment=ft.MainAxisAlignment.START)),
            ft.canvas.Canvas(ref=self.canvas, width=field_size, height=field_size),
            ft.Container(MoveSelectorControl(height=field_size, alignment=ft.MainAxisAlignment.END))
                             ])
        bottom_row = ft.Row([ft.Text("   ", expand=True),
                             FieldSizeControl(ref=self.field_size, expand=True),
                             WhoPlayControl(ref=self.who_play_b, expand=True)],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
        return ft.Column([title_row,
                          middle_row,
                          bottom_row])

    def init_game(self):
        width, height = fieldsize_to_width_height[self.field_size.current.group.current.value]
        self.field = Field(width=width, height=height, color_num=len(game_palette))
        self.player_to_move = 0
        homes = self.field.homes_two_players()
        self.homes = homes
        self.thinkers = [RandomThinker(homes), RandomThinker(homes), GreedyThinker(homes)]
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
