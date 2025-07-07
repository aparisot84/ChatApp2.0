import flet as ft

######### OPENGL ISSUES ON HP PAVILLION ########
import os
os.environ["LIBGL_ALWAYS_SOFTWARE"] = "1"
#############################################################
"""
                        LAYOUT
╔══════════════════════════════════════════════════════════╗
║               Sala de Chat (Título ou Cabeçalho)         ║
╠══════════════════════════════════════════════════════════╣
║ Mensagens da Sala (rolável)             | Participantes  ║
║ [mensagem 1...]                         | [Fulano]       ║
║ [mensagem 2...]                         | [Beltrano]     ║
║ [...]                                   | [Sicrano]      ║
║                                         |                ║
╠══════════════════════════════════════════════════════════╣
║ > [Digite sua mensagem aqui...]   [Enviar]    [voltar]   ║
╚══════════════════════════════════════════════════════════╝
"""

#################### CHAMADAS DA VIEW ###############
def show_chat_screen(page: ft.Page, show_main_screen_callback=None):
    page.clean()

    return

if __name__ == '__main__':
    def test_view(page: ft.Page):
        page.title = "Chat APP"
        show_chat_screen(page)
        page.window.width = 800
        page.window.height = 600
        page.window.resizable = False
        #page.window.maximizable = False
        page.theme_mode = ft.ThemeMode.LIGHT
        page.update()
    ft.app(target=test_view)