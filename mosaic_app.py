import flet as ft

from controls.mosaic_control import MosaicControl
from mosaic_core import get_version


class MosaicApp(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.game = MosaicControl()
        page.on_route_change = self.on_route_change
        self.about_view = ft.View(
            "/about",
            [
                ft.Text("About page"),
                ft.ElevatedButton(
                    "Go to main page",
                    on_click=lambda _: page.go("/"),
                ),
            ]
        )
        self.appbar_items = [
            ft.PopupMenuItem(text="About Mosaic", on_click=lambda _: page.go("/about")),
        ]
        self.appbar = ft.AppBar(
            leading=ft.Icon(ft.icons.APPS_SHARP),
            leading_width=50,
            title=ft.Text(f"Mosaic game v."+get_version(), font_family="Pacifico", size=18,
                          text_align=ft.TextAlign.START),
            center_title=False,
            toolbar_height=40,
            bgcolor=ft.colors.LIGHT_BLUE_ACCENT_700,
            actions=[
                ft.Container(
                    content=ft.PopupMenuButton(items=self.appbar_items),
                    margin=ft.margin.only(left=50, right=25),
                )
            ],
        )
        self.page.appbar = self.appbar
        self.page.update()


    def view_pop(self, view):
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)

    def on_route_change(self, route):
        if self.page.route == "/about":
            self.page.views.append(self.about_view)
        else:
            while len(self.page.views) > 1:
                self.page.views.pop()
        self.page.update()

    def build(self):
        return ft.Container(
            self.game,
            width=790,
            height=810,
        )

    def initialize(self):
        self.game.init_game()
        self.page.update()


def main(page: ft.Page):
    page.title = "Mosaic game"
    page.description = "Mosaic game implemented on Python+flet"
    page.author = "S.Sotnyk"
    page.add(
        ft.Container(
            # game := MosaicControl(),
            app := MosaicApp(page),
            width=790,
            height=810,
        )
    )
    # page.add(ft.Text(f"Initial route: {page.route}"))
    page.window_height = 810
    page.window_width = 800
    # game.init_game()
    app.initialize()
    page.update()


ft.app(main, view=ft.WEB_BROWSER, port=8080, assets_dir="assets")
