import flet as ft

######### OPENGL ISSUES ON HP PAVILLION ########
import os
os.environ["LIBGL_ALWAYS_SOFTWARE"] = "1"


############# IMPORTAÇÃO DA VIEWS #############

from interface.views.main_screen_view import show_main_screen
from interface.views.chat_screen_view import show_chat_screen
from interface.views.server_screen_view import show_server_screen

#################### CHAMADAS DAS VIEWS ###############
def main(page: ft.Page):

    # Configurações gerais da página
    page.title = "Chat APP - Um Aplicativo para Conversas Online"
    page.window.width = 300
    page.window.height = 450
    page.window.resizable = False
    page.theme_mode = ft.ThemeMode.LIGHT

    def navigate_to_main_screen():
        show_main_screen(page, navigation_callbacks)

    def navigate_to_chat_screen():
        show_chat_screen(page, navigate_to_chat_screen)

    def navigate_to_server_screen():
        show_server_screen(page, navigate_to_server_screen)

    navigation_callbacks = {
        "show_main_screen": navigate_to_main_screen,
        "show_chat_screen": navigate_to_chat_screen,
        "show_server_screen": navigate_to_server_screen,
    }

    navigate_to_main_screen()
    page.update()

if __name__ == '__main__':
    ft.app(target=main, view=ft.AppView.FLET_APP)



