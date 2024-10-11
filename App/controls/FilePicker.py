import flet as ft
import json

class FilePicker(ft.FilePicker):
    def __init__(
        self
    ):
        super().__init__()
        self.on_result = self.file_picker_result
        self.audio_files: ft.FilePickerResultEvent = None
    

    def file_picker_result(self, e: ft.FilePickerResultEvent):
        if e.files:
            self.audio_files = e
        
        self.add_playlist()
    

    def add_playlist(self):
        try:
            if self.page.platform.value == 'windows':
                with open('playlist/windows_playlist.json', 'r') as file:
                    json.load(file)
            
            if self.page.platform.value == 'android':
                with open('playlist/android_playlist.json', 'r') as file:
                    json.load(file)
        
        except:
            if self.page.platform.value == 'windows':
                with open('playlist/windows_playlist.json', 'w') as file:
                    json.dump({"audios": []}, file, indent=4)
            
            if self.page.platform.value == 'android':
                with open('playlist/android_playlist.json', 'w') as file:
                    json.dump({"audios": []}, file, indent=4)
        
        if self.audio_files is not None:
            # Lê os ficheiros json
            if self.page.platform.value == 'windows':
                with open('playlist/windows_playlist.json', 'r') as file:
                    audio_files = json.load(file)
            
            if self.page.platform.value == 'android':
                with open('playlist/android_playlist.json', 'r') as file:
                    audio_files = json.load(file)
            
            # Adiciona os arquivos
            if self.page.platform.value == 'windows':
                with open('playlist/windows_playlist.json', 'w') as file:
                    for audio_file in self.audio_files.files:
                        audio_files['audios'].append(
                            {
                                'src': audio_file.path,
                                'name': audio_file.name,
                                'size': audio_file.size
                            }
                        )

                    json.dump(audio_files, file, indent=4)
            
            if self.page.platform.value == 'android':
                with open('playlist/android_playlist.json', 'w') as file:
                    for audio_file in self.audio_files.files:
                        audio_files['audios'].append(
                            {
                                'src': audio_file.path,
                                'name': audio_file.name,
                                'size': audio_file.size
                            }
                        )

                    json.dump(audio_files, file, indent=4)