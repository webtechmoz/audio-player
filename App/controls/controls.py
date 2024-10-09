import flet as ft

class Text(ft.Text):
    def __init__(
        self,
        value: str,
        size: int = 14,
        color: ft.colors = ft.colors.WHITE,
        weight: ft.FontWeight = 'bold',
        nowrap: bool = True
    ):
        super().__init__()
        self.value = value
        self.size = size
        self.color = color
        self.weight = weight
        self.no_wrap = nowrap

class Icon(ft.Icon):
    def __init__(
        self,
        icon: ft.icons,
        color: ft.colors = ft.colors.with_opacity(0.5, 'green'),
        size: int = 25
    ):
        super().__init__()
        self.name = icon
        self.size = size
        self.color = color

class IconButton(ft.IconButton):
    def __init__(
        self,
        icon: ft.icons,
        size: int = 25,
        color: ft.colors = ft.colors.with_opacity(0.5, 'blue'),
        on_click: ft.ControlEvent = None
    ):
        super().__init__()
        self.icon = icon
        self.icon_color = color
        self.icon_size = size
        self.on_click = on_click