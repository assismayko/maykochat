import flet as ft

def main(page: ft.Page):
    page.title = "Maykochat"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    def iniciar_chat(e):
        dlg = ft.AlertDialog(
            title=ft.Text("Bem vindo ao Mayko Chat"),
            content=ft.Column(
                [
                    ft.TextField(label="Escreva seu nome", value=""),
                    ft.ElevatedButton(
                        "Entrar no Chat",
                        on_click=lambda e: exibir_chat(e),
                    ),
                ]
            ),
        )
        page.dialog = dlg
        dlg.open = True
        page.update()

    def exibir_chat(e):
        # Feche o popup (AlertDialog)
        page.dialog.open = False
        page.update()

        # Implemente a UI do chat aqui

    titulo = ft.Text("Maykochat", size=30)
    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=iniciar_chat)
    page.add(titulo, botao_iniciar)


ft.app(target=main)