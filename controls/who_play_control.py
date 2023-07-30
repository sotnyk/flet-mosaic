from typing import cast

import flet as ft
from aenum import StrEnum


class WhoPlay(StrEnum):
    HUMAN = "Human"
    LEVEL1 = "Level 1"
    LEVEL2 = "Level 2"


class WhoPlayControl(ft.UserControl):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.group = ft.Ref[ft.RadioGroup]()
        self.btns = [ft.Ref[ft.Radio]() for _ in range(3)]

    def build(self):
        human_btn = ft.Radio(ref=self.btns[0], label="Human", value=WhoPlay.HUMAN)
        level1_btn = ft.Radio(ref=self.btns[1], label="Level 1", value=WhoPlay.LEVEL1)
        level2_btn = ft.Radio(ref=self.btns[2], label="Level 2", value=WhoPlay.LEVEL2)
        group = ft.RadioGroup(ref=self.group,
                              content=ft.Row([human_btn, level1_btn, level2_btn]),
                              value=WhoPlay.HUMAN)
        return group

    def selected_value(self)->WhoPlay:
        return cast(WhoPlay, self.group.current.value)
