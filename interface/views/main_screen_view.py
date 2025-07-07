import flet as ft

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
        if e.control.value == "Cliente":
            current_callback_key.current = "show_chat_screen"
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
        else:
            navigation_callbacks[current_callback_key.current]()
        page.update()

        # pra eu poder checar se os campos estão preenchidos ou nao, tenho que assocuá-los a variáveis, como abaixo

        #nome_field = ft.TextField(label="Nome")
        #email_field = ft.TextField(label="Email")

        return


    def exit_click(e):
        page.window.close()

    page.appbar = ft.AppBar(
        #leading=ft.Icon(ft.Icons.ANCHOR),
        title=ft.Text("CONFIGURAÇÕES INICIAIS", size=20, text_align=ft.TextAlign.CENTER),
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
    )

    # Componentes da tela
    text_nome = ft.Text("Nome: ", size=18)
    field_nome = ft.TextField(width=180)
    text_servidor = ft.Text("Servidor:", size=18)
    field_servidor = ft.TextField(width=180)
    text_porta = ft.Text("Porta:", size=18)
    field_porta = ft.TextField(width=180)
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
    button_iniciar = ft.ElevatedButton("Iniciar", icon="EXIT_TO_APP", on_click=check_fields)
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

