import flet as ft
from aenum import IntEnum


class FieldSize(IntEnum):
    Size8x8 = 8
    Size16x16 = 16
    Size32x32 = 32


fieldsize_to_width_height = {
    FieldSize.Size8x8: (8, 8),
    FieldSize.Size16x16: (16, 16),
    FieldSize.Size32x32: (32, 32)
}


class FieldSizeControl(ft.UserControl):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.group = ft.Ref[ft.RadioGroup]()
        self.btns = [ft.Ref[ft.Radio]() for _ in range(len(FieldSize))]

    def build(self):
        for n, s in enumerate(FieldSize):
            btn = ft.Radio(ref=self.btns[n], label=f"{s.value}x{s.value}", value=str(s))
        group = ft.RadioGroup(ref=self.group,
                              content=ft.Row([b.current for b in self.btns]),
                              value=self.btns[0].current.value)
        return group
