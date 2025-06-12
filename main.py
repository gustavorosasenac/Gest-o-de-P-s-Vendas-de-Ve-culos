import flet as ft

def menu(page: ft.Page):
    page.title = "Menu Principal"
    page.theme_mode = ft.ThemeMode.DARK

    def clique(e):
        page.dialog = ft.AlertDialog(
            title=ft.Text(f"Você clicou em: {e.control.text}"),
            open=True
        )
        page.update()

    titulo = ft.Text("🚘 Sistema de Veículos", size=40, weight=ft.FontWeight.BOLD, color="white")

    botao_cadastrar = ft.ElevatedButton(
        text="Cadastrar Veículo",
        icon=ft.Icon(name="add_circle"),
        width=400,
        on_click=clique
    )

    botao_consultar = ft.ElevatedButton(
        text="Consultar Veículos",
        icon=ft.Icon(name="search"),
        width=400,
        on_click=clique
    )

    conteudo = ft.Column(
        [
            titulo,
            ft.Divider(),
            botao_cadastrar,
            botao_consultar
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    layout = ft.Stack(
        controls=[
            ft.Image(
                src="https://previews.123rf.com/images/misign/misign2204/misign220400001/184469781-a-old-yellow-tricycle-car-is-a-three-wheeled-light-commercial-vehicle-produced-since-1948-in-italy.jpg",
                fit=ft.ImageFit.COVER,
                width=page.width,
                height=page.height
            ),
            ft.Container(
                content=conteudo,
                alignment=ft.alignment.center,
                padding=40,
                bgcolor="#00000088",  # Preto com 53% de opacidade
                border_radius=10
            )
        ],
        expand=True
    )

    page.add(layout)

ft.app(target=menu)
