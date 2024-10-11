import flet as ft

class AudioCover(ft.Container):
    def __init__(
        self,
        page: ft.Page,
        image_src: str
    ):
        super().__init__()
        self.bgcolor = ft.colors.BLUE
        self.width = page.width
        self.height = page.height
        self.content = ft.Stack(
            controls=[
                cover_img := ft.Container(
                    image=ft.DecorationImage(
                        src=image_src,
                        fit=ft.ImageFit.COVER
                    ),
                    width=page.width * 0.50,
                    height=page.width * 0.50,
                    border_radius=page.width * 0.50,
                    bgcolor= ft.colors.BLACK,
                    left= (page.width * 0.5 / 2),
                    top= page.width * 1/3
                )
            ]
        )
    
        self.cover_img = cover_img