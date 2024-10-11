from controls.Appbar import (
    ft,
    Appbar
)
from controls.AudioCover import AudioCover
from controls.AudioControls import AudioControls

class Home(ft.View):
    def __init__(
        self,
        page: ft.Page
    ):
        self.image_src = 'https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/cc/00/56/cc0056e3-3781-791a-1c34-fb4c76bdeac8/AppIcon-0-0-1x_U007ephone-0-0-0-0-0-0-sRGB-85-220.png/1024x1024.jpg'
        self.audio_cover = AudioCover(page=page, image_src=self.image_src)
        self.audio_controls = AudioControls(page=page)
        super().__init__()
        self.route = '/'
        self.padding = ft.padding.all(0)
        self.appbar = Appbar(page=page)
        self.controls = [
            ft.Stack(
                controls=[
                    self.audio_cover,
                    self.audio_controls
                ]
            )
        ]

        page.on_resized = self.on_resize
    

    def on_resize(self, e: ft.WindowResizeEvent):
        width = e.width
        height = e.height

        self.audio_cover.width = width
        self.audio_cover.height = height

        #AudioCover
        self.audio_cover.cover_img.width=width * 0.50
        self.audio_cover.cover_img.height=width * 0.50
        self.audio_cover.cover_img.border_radius=width * 0.50
        self.audio_cover.cover_img.bgcolor= ft.colors.BLACK
        self.audio_cover.cover_img.left= (width * 0.5 / 2)
        self.audio_cover.cover_img.top= width * 1/3

        #Audio Controls
        self.audio_controls.width = e.width
        self.audio_controls.height = e.height * 0.22

        # ProgressBar
        self.audio_controls.pg_1.width = e.width
        self.audio_controls.pg_2.width = e.width * 0.5

        e.page.update()