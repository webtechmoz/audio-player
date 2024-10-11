from views.Home import (
    ft,
    Home
)

def main(page: ft.Page):
    page.title = 'Audio Player'
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = ft.padding.all(0)
    page.window.width = 350
    page.window.height = 720
    page.window.maximizable = False
    page.window.resizable = False

    home = Home(page=page)

    def router(route):
        page.views.clear()

        if page.route == '/':
            page.views.append(home)
        
        page.update()
    
    page.on_route_change = router
    page.go(page.route)

if __name__ == '__main__':
    ft.app(target=main)