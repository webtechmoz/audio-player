from controls.controls import (
    ft,
    Icon,
    IconButton,
    Text
)
from controls.FilePicker import FilePicker

class Appbar(ft.AppBar):
    def __init__(
        self,
        page: ft.Page
    ):
        fp = FilePicker()
        page.overlay.append(fp)
        super().__init__()
        self.bgcolor = ft.colors.with_opacity(0.40, 'black')
        self.leading = ft.Row(
            controls=[
                Icon(
                    icon=ft.icons.MUSIC_NOTE,
                ),
                Text(
                    value=page.title,
                    size=18,
                    color=ft.colors.with_opacity(0.8, 'green')
                )
            ]
        )
        self.actions = [
            IconButton(
                icon=ft.icons.FOLDER,
                on_click=lambda e: fp.pick_files(
                    dialog_title=page.title,
                    file_type=ft.FilePickerFileType.AUDIO,
                    allow_multiple=True
                )
            )
        ]
        self.toolbar_height = 40