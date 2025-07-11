import flet as ft
import socket

######### OPENGL ISSUES ON HP PAVILLION ########
import os

from jupyter_client.localinterfaces import local_ips

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
    page.title = "Chat APP"
    page.window.width = 800
    page.window.height = 600
    page.window.resizable = False
    page.window.maximizable = False

    page.update()

    def get_local_ip():
        local_ip = socket.gethostbyname(socket.gethostname())
        return local_ip

    def start_server_click(e):
        Listview_chat_messages.controls.append(ft.Text(get_local_ip()))
        update_server_ip()
        page.update()

    def stop_server_click(e):
        list_view_connected_users.controls.append(ft.Text("Fulano de Tal: 192.168.1.1"))
        page.update()

    def exit_click(e):
        page.window.close()

    page.appbar = ft.AppBar(
        #leading=ft.Icon(ft.Icons.ANCHOR),
        title=ft.Text("GERENCIADOR DO SERVIDOR DE CHAT", size=20, text_align=ft.TextAlign.CENTER),
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
        center_title =True
    )

    text_endereco = ft.Text("Servidor ativo em XXX.XXX.XXX.XXX:XXXX", size=18, text_align=ft.TextAlign.CENTER)
    text_tempo_atividade = ft.Text("Tempo de atividade: DDD:HH:MM:SS", size=18, text_align=ft.TextAlign.CENTER)
    text_logs = ft.Text("Logs do Servidor", size=18, text_align=ft.TextAlign.CENTER)
    text_conexoes_ativas = ft.Text("Conexões Ativas", size=18, text_align=ft.TextAlign.CENTER)

    Listview_chat_messages = ft.ListView(expand=True, spacing=10, auto_scroll=True)
    list_view_connected_users = ft.ListView(expand=True, spacing=10, auto_scroll=True)

    button_start_server = ft.ElevatedButton("Iniciar Servidor", icon="PLAY", on_click=start_server_click)
    button_stop_server = ft.ElevatedButton("Parar Servidor", icon="STOP", on_click=stop_server_click)
    button_back = ft.ElevatedButton("Voltar", icon="ARROW_BACK")
    button_sair = ft.ElevatedButton("Exit", icon="EXIT_TO_APP", on_click=exit_click)

    page.add(
        ft.Row([
            text_endereco,
        ], alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row([
            text_tempo_atividade,
        ], alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Divider(),
        ft.Row([

            #####################
            ft.Container(
                content = ft.Column([
                    text_logs,
                    ft.Divider(),
                    Listview_chat_messages
                ],
                  width=330
                ),
            ),
            ft.VerticalDivider(width=3),
            ft.Container(
                content=ft.Column([
                    text_conexoes_ativas,
                    ft.Divider(),
                    list_view_connected_users,
                ],
                    width=200,
                ),
            ),
        ], expand=True
        ),
        ft.Divider(),
        ft.Row([
            button_start_server,
            button_stop_server,
            button_back,
            button_sair
        ], alignment=ft.MainAxisAlignment.SPACE_EVENLY, spacing=40
        )
    )
    def update_server_ip():
        ip = get_local_ip()
        text_endereco.value = f"Servidor Ativo em {ip}: 5000"
        text_endereco.update()
        page.update()

    update_server_ip()

if __name__ == '__main__':
    def test_view(page: ft.Page):
        page.title = "Chat APP"
        show_server_screen(page)
        page.window.width = 600
        page.window.height = 500
        page.window.resizable = False
        page.window.maximizable = False
        page.theme_mode = ft.ThemeMode.LIGHT
        page.update()
    ft.app(target=test_view)





