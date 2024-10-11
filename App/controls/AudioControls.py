from controls.controls import (
    ft,
    IconButton,
    Text
)
import json

class AudioControls(ft.Container):
    def __init__(
        self,
        page: ft.Page
    ):
        
        super().__init__()
        self.width = page.width
        self.height = page.height * 0.20
        self.bgcolor = ft.colors.with_opacity(0.4, 'white')
        self.top = page.height - (self.height + 70 if page.platform.value == 'android' else self.height + 50)
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
                                pg_1 := ProgressBar(
                                    width=page.width
                                ),
                                pg_2 := ProgressBar(
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
                        btn_playlist := IconButton(
                            icon=ft.icons.MENU,
                            color=ft.colors.WHITE
                        ),
                        ft.Row(
                            controls=[
                                btn_previous := IconButton(
                                    icon=ft.icons.SKIP_PREVIOUS,
                                    color=ft.colors.WHITE,
                                    on_click=self.previous
                                ),
                                btn_play := IconButton(
                                    icon=ft.icons.PLAY_ARROW,
                                    color=ft.colors.WHITE,
                                    on_click=self.play
                                ),
                               btn_next :=  IconButton(
                                    icon=ft.icons.SKIP_NEXT,
                                    color=ft.colors.WHITE,
                                    on_click=self.next
                                )
                            ]
                        ),
                        btn_favorite := IconButton(
                            icon=ft.icons.FAVORITE_BORDER,
                            color=ft.colors.WHITE
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                )
            ],
            spacing=15
        )

        self.pg_1 = pg_1
        self.pg_2 = pg_2
        self.btn_playlist = btn_playlist
        self.btn_previous = btn_previous
        self.btn_play = btn_play
        self.btn_next = btn_next
        self.btn_favorite = btn_favorite
        self.audio_playlist: list[ft.Audio] = []
        self.current_audio: ft.Audio = None
    
    def play(self, e: ft.ControlEvent):

        if self.current_audio is None:
            self.add_playlist()

            if len(self.audio_playlist) > 0:
                self.current_audio = self.audio_playlist[-1]
            
            else:
                return

        if self.btn_play.icon == 'play_arrow':
            self.current_audio.resume()
            self.btn_play.icon = ft.icons.PAUSE
        
        elif self.btn_play.icon == 'pause':
            self.current_audio.pause()
            self.btn_play.icon = ft.icons.PLAY_ARROW
        
        self.page.update()
    
    def previous(self, e: ft.ControlEvent):
        if self.current_audio is not None:
            self.current_audio.pause()
            self.btn_play.icon = ft.icons.PLAY_ARROW

            i = self.audio_playlist.index(self.current_audio)

            if i > 0:
                self.current_audio = self.audio_playlist[i - 1]
            
            else:
                self.current_audio = self.audio_playlist[-1]
        
        else:
            self.add_playlist()
            self.current_audio = self.audio_playlist[0]
        
        self.current_audio.play()
        self.btn_play.icon = ft.icons.PAUSE
        self.page.update()

    def next(self, e: ft.ControlEvent):
        if self.current_audio is not None:
            self.current_audio.pause()
            self.btn_play.icon = ft.icons.PLAY_ARROW

            i = self.audio_playlist.index(self.current_audio)

            if i < len(self.audio_playlist) - 1:
                self.current_audio = self.audio_playlist[i + 1]
            
            else:
                self.current_audio = self.audio_playlist[0]
        
        else:
            self.add_playlist()
            self.current_audio = self.audio_playlist[0]
        
        self.current_audio.play()
        self.btn_play.icon = ft.icons.PAUSE
        self.page.update()
    
    def add_playlist(self):
        try:
            if self.page.platform.value == 'windows':
                with open('playlist/windows_playlist.json', 'r') as file:
                    audio_playlist: list[dict[str, str]] = json.load(file)['audios']
            
            elif self.page.platform.value == 'android':
                with open('playlist/android_playlist.json', 'r') as file:
                    audio_playlist: list[dict[str, str]] = json.load(file)['audios']
            
            for audio in audio_playlist:
                audio_control = ft.Audio(
                    src=audio['src'],
                    volume=1,
                    autoplay=False
                )

                self.audio_playlist.append(audio_control)
                self.page.overlay.append(audio_control)
                self.page.update()
        
        except Exception as e:
            print(f'Erro: {e}')


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