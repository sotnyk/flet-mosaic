from functools import partial

import flet as ft

from controls.palette import game_palette


class MoveSelectorControl(ft.UserControl):
    def __init__(self, alignment: ft.MainAxisAlignment = ft.MainAxisAlignment.CENTER, *args,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self.alignment = alignment
        self.last_clicked: int | None = None

    def build(self):
        buttons = [ft.Container(ft.Text(f"{i + 1}"), bgcolor=game_palette[i],
                                alignment=ft.alignment.center,
                                height=40, width=40,
                                on_click=partial(self.on_click_n, n=i)
                                )
                   for i in range(len(game_palette))]
        return ft.Column(buttons, alignment=self.alignment)

    def on_click_n(self, e, n):
        # print(f"on_click_n: {n}")
        self.last_clicked = n
