import flet as ft

######### OPENGL ISSUES ON HP PAVILLION ########
import os
os.environ["LIBGL_ALWAYS_SOFTWARE"] = "1"
#############################################################
"""
                        LAYOUT
╔══════════════════════════════════════════════════════════╗
║            Gerenciador do Servidor de Chat               ║
╠══════════════════════════════════════════════════════════╣
║           🟢 Servidor ativo em 127.0.0.1:5000            ║     
║            Tempo de atividade: DDD:HH:MM:SS              ║
╠══════════════════════════════════════════════════════════╣
║ Logs do Servidor: (rolável)         | Conexões Ativas:   ║
║----------------------------------------------------------║
║ [Servidor iniciado na porta 5000]   | [Fulano] - IP      ║
║ [Aguardando conexões...]            | [Beltrano] - IP    ║
║ [Cliente conectado: 192.168.0.12]   | [Sicrano] - IP     ║
║ [Mensagem recebida de Fulano]       |                    ║
║ [Cliente desconectado]              |                    ║
╠══════════════════════════════════════════════════════════╣
║ [Limpar Log] [Iniciar Servidor] [Parar Servidor] [Voltar]║
╚══════════════════════════════════════════════════════════╝
"""


#################### CHAMADAS DA VIEW ###############
def show_server_screen(page: ft.Page, show_main_screen_callback=None):
    page.clean()

    return

if __name__ == '__main__':
    def test_view(page: ft.Page):
        page.title = "Chat APP"
        show_server_screen(page)
        page.window.width = 800
        page.window.height = 600
        page.window.resizable = False
        #page.window.maximizable = False
        page.theme_mode = ft.ThemeMode.LIGHT
        page.update()
    ft.app(target=test_view)





