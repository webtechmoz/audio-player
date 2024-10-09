from controls.controls import (
    ft,
    IconButton,
    Text
)

class AudioControls(ft.Container):
    def __init__(
        self,
        page: ft.Page
    ):
        super().__init__()
        self.width = page.width
        self.height = page.height * 0.20
        self.bgcolor = ft.colors.with_opacity(0.4, 'white')
        self.top = page.height - (self.height + 70)
        self.border_radius = ft.border_radius.only(
            top_left=8,
            top_right=8
        )
        self.padding = ft.padding.all(8)
        self.content = ft.Column(
            controls=[
                ft.Column(
                    controls=[
                        Text(
                            value='Titulo da Música',
                            size=14
                        ),
                        Text(
                            value='Artista | Album',
                            size=12,
                            color=ft.colors.with_opacity(0.8, 'white')
                        )
                    ],
                    spacing=0
                ),
                ft.Column(
                    controls=[
                        ft.Stack(
                            controls=[
                                ProgressBar(
                                    width=page.width
                                ),
                                ProgressBar(
                                    width=page.width * 0.4,
                                    bgcolor=ft.colors.RED
                                )
                            ]
                        ),
                        ft.Row(
                            controls=[
                                Text(
                                    value='00:00',
                                    size=12
                                ),
                                Text(
                                    value='06:07',
                                    size=12
                                )
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        )
                    ]
                ),
                ft.Row(
                    controls=[
                        IconButton(
                            icon=ft.icons.MENU,
                            color=ft.colors.WHITE
                        ),
                        ft.Row(
                            controls=[
                                IconButton(
                                    icon=ft.icons.SKIP_PREVIOUS,
                                    color=ft.colors.WHITE
                                ),
                                IconButton(
                                    icon=ft.icons.PLAY_ARROW,
                                    color=ft.colors.WHITE
                                ),
                                IconButton(
                                    icon=ft.icons.SKIP_NEXT,
                                    color=ft.colors.WHITE
                                )
                            ]
                        ),
                        IconButton(
                            icon=ft.icons.FAVORITE_BORDER,
                            color=ft.colors.WHITE
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                )
            ],
            spacing=15
        )

class ProgressBar(ft.Container):
    def __init__(
        self,
        width: int,
        bgcolor: ft.colors = ft.colors.with_opacity(0.25, 'black'),
        height: int = 2
    ):
        super().__init__()
        self.width = width
        self.bgcolor = bgcolor
        self.height = height