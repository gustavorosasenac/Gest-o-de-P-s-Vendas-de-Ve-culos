import flet as ft
from DB.Database import session

class Login:
    def __init__(self, page: ft.Page):
        page.window.maximized = True
        # Configuração da página
        page.title = "Login"
        page.theme_mode = ft.ThemeMode.DARK
        page.padding = 0
        page.fonts = {"Poppins": "https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap"}
        page.theme = ft.Theme(font_family="Poppins")

        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        # Elementos da UI
        titulo = ft.Text("Login",size=36,weight=ft.FontWeight.BOLD,color=ft.Colors.WHITE,text_align=ft.TextAlign.CENTER) 
        
        # Funções dos botões
        def fechar_app(e):
            page.clean()
            page.update()
            page.vertical_alignment = ft.MainAxisAlignment.CENTER
            page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
            page.add(ft.Text("Aplicação fechada."))
            session.close()
            
        def logar(e):
            from Models.visual import Menu_principal
            page.clean()
            Menu_principal(page)

        def criar_botao(texto, icone, funcao, cor=ft.Colors.BLUE_700):
            return ft.Container(
                content=ft.ElevatedButton(
                    text=texto,
                    icon=icone,
                    on_click=funcao,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=10),
                        padding=20,
                        bgcolor=cor,
                        color=ft.Colors.WHITE
                    ),
                width=300,
                height=60
                ),
                margin=ft.margin.only(bottom=15),
                animate=ft.Animation(300, "easeInOut")
            )
        
        botao_logar = criar_botao("Entrar", ft.Icons.LOGIN, logar, ft.Colors.TEAL_700)
        botao_fechar_app = criar_botao("Fechar Aplicação", ft.Icons.EXIT_TO_APP, fechar_app, ft.Colors.RED_700)

        conteudo = ft.Column(
            [
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Icon(name=ft.Icons.LOGIN, size=50, color=ft.Colors.WHITE),
                            titulo,
                            ft.Divider(height=40, color=ft.Colors.TRANSPARENT),
                            botao_logar,
                            ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                            botao_fechar_app
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=5
                    ),
                    padding=ft.padding.all(30),
                    bgcolor=ft.Colors.with_opacity(0.85, ft.Colors.BLACK),
                    border_radius=20,
                    width=400
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
        
        # Fundo com gradiente e imagem
        page.add(
            ft.Stack(
                [
                    ft.Container(
                        gradient=ft.LinearGradient(
                            begin=ft.alignment.top_center,
                            end=ft.alignment.bottom_center,
                            colors=[ft.Colors.with_opacity(0.5, ft.Colors.BLACK), ft.Colors.BLACK]
                        ),
                        content=ft.Row(
                            [conteudo],
                            alignment=ft.MainAxisAlignment.CENTER,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER
                        ),
                        expand=True
                    )
                ],
                expand=True))