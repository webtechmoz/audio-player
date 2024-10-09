import flet as ft

class FilePicker(ft.FilePicker):
    def __init__(
        self,
    ):
        super().__init__()
        self.on_result = self.file_picker_result
    

    def file_picker_result(self, e: ft.FilePickerResultEvent):
        if e.files:
            for file in e.files:
                print(file.path)
        