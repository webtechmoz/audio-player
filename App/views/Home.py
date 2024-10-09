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
        super().__init__()
        self.route = '/'
        self.padding = ft.padding.all(0)
        self.appbar = Appbar(page=page)
        self.controls = [
            ft.Stack(
                controls=[
                    AudioCover(page=page, image_src=self.image_src),
                    AudioControls(page=page)
                ]
            )
        ]