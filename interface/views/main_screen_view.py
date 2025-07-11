import flet as ft
from utils.formatters import format_ip
from utils.formatters import format_port
######### OPENGL ISSUES ON HP PAVILLION ########
import os
os.environ["LIBGL_ALWAYS_SOFTWARE"] = "1"

######################################################################
"""
        LAYOUT
╔══════════════════════════════╗
║     Configurações Iniciais   ║    Row com o título
╠══════════════════════════════╣
║ Nome:        [___________]   ║    row com um texto e um text field
║ Servidor:    [127.0.0.1  ]   ║    row com um texto e um text field
║ Porta:       [5000       ]   ║    row com um texto e um text field
║ Modo:        ( ) Cliente     ║    row com um text e um dropdown
║              ( ) Servidor    ║
║                              ║    espaço entre os rows
║ Tema:        [Claro  v]      ║    row com um texto e um dropdown
║ Notificações: [x] Ativar     ║    row com um texto e um checkbox
║                              ║    espaço entre os rows
║ [ Iniciar Chat ]  [ Sair ]   ║    row com dois botões
╚══════════════════════════════╝
# criar os formatadores para os campos:
IP: XXX.XXX.XXX.XXX de 0 a 255
porta: de 1 a 65.535
-> Em caso de erro, abrir janela de alerta
"""
#################### CHAMADAS DA VIEW ###############

def show_main_screen(page: ft.Page, navigation_callbacks):
    page.clean()

    # Usar um ft.Ref para armazenar o valor selecionado do dropdown
    selected_mode_ref = ft.Ref[ft.Dropdown]()
    dropdown_ref = ft.Ref[ft.Dropdown]()
    current_callback_key = ft.Ref[str]()
    current_callback_key.current = "show_chat_screen"

    def select_mode(e):
        if e.control.value == "Servidor":
           current_callback_key.current = "show_server_screen"
           text_servidor.disabled=True
        if e.control.value == "Cliente":
            current_callback_key.current = "show_chat_screen"
            text_servidor.disabled = False
        page.update()

    def change_theme_mode(e):
        if e.control.value == "Claro":
            page.theme_mode = ft.ThemeMode.LIGHT
        elif e.control.value == "Escuro":
            page.theme_mode = ft.ThemeMode.DARK
        page.update()

    def notification_option(e):
        # tocar um som quando o checkbox estiver selecionado
        # Função que trata a opção de notificação pelo sistema
        #t.value = f"Checkbox value changed to {c.value}"
        #t.update() #faz o update
        """
        if notification == True:
            notification = False
        elif notification == False:
            notification = True
        """
        return #notification

    def check_fields(e):
        if not field_nome.value or not field_porta.value or not field_servidor.value:
            alert_dialog = ft.AlertDialog(title=ft.Text("Preencha todos os campos antes de continuar"))
            alert_dialog.open = True
            page.update()
            return False
        else:
            navigation_callbacks[current_callback_key.current]()
            page.update()
            return True


    def iniciar_click(e):
        #essa funçao vai ser respons'avel por chamar a funçao de checar se os campos est~ao preenchidos e chamar a proxima janela, seja ela a de servidor ou a de cliente

        return

    def exit_click(e):
        page.window.close()

    def ip_mask():
        # Atualiza o valor do campo sem interferir na digitação
        field_servidor.value = format_ip(field_servidor.value)
        field_servidor.update()

    def port_mask():
        nip.value = format_nip(nip.value)
        nip.update()

    page.appbar = ft.AppBar(
        #leading=ft.Icon(ft.Icons.ANCHOR),
        title=ft.Text("CONFIGURAÇÕES INICIAIS", size=20, text_align=ft.TextAlign.CENTER),
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
    )

    # Componentes da tela
    text_nome = ft.Text("Nome: ", size=18)
    field_nome = ft.TextField(width=180)
    text_servidor = ft.Text("Servidor:", size=18)
    field_servidor = ft.TextField(width=180, on_change=lambda e: ip_mask())
    text_porta = ft.Text("Porta:", size=18)
    field_porta = ft.TextField(width=180, on_change=lambda e: port_mask())
    text_modo = ft.Text("Modo:", size=18)
    dropdown_modo = ft.Dropdown(width=150, value="Cliente", options=[
        ft.dropdown.Option("Servidor"),
        ft.dropdown.Option("Cliente")
        ], on_change=select_mode, ref=dropdown_ref)
    text_tema = ft.Text("Tema:", size=18)
    dropdown_tema = ft.Dropdown(width=150, value="Claro",  options=[
        ft.dropdown.Option("Claro"),
        ft.dropdown.Option("Escuro")
        ], on_change=change_theme_mode)
    text_notificacoes = ft.Text("Notificações:", size=18)
    checkbox_notificacoes = ft.Checkbox(value = True, on_change=notification_option)
    button_iniciar = ft.ElevatedButton("Iniciar", icon="EXIT_TO_APP", on_click=iniciar_click)
    button_sair = ft.ElevatedButton("Exit", icon="EXIT_TO_APP", on_click=exit_click)

    # Montagem dos componentes na tela
    page.add(
        #ft.Divider(),
        ft.Row([
           text_nome,
           field_nome
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=27
        ),
        ft.Row([
            text_servidor,
            field_servidor
            ], alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row([
            text_porta,
            field_porta
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=38
        ),
        ft.Row([
            text_modo,
            dropdown_modo
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=35
        ),
        ft.Row([
            text_tema,
            dropdown_tema
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=35
        ),
        ft.Row([
            text_notificacoes,
            checkbox_notificacoes
        ], alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row([
            button_iniciar,
            button_sair
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=40
        ),
    )

