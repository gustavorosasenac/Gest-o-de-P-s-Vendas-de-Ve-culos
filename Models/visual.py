import flet as ft
from DB.Database import session
imagem_fundo = src="imagens/foto.jpg"

class Menu_principal:
    def __init__(self, page: ft.Page):
        page.assets_dir = "assets"
        page.window.maximized = True
        # Configuração da página
        page.title = "🚘 Sistema de Veículos Premium"
        page.theme_mode = ft.ThemeMode.DARK
        page.padding = 0
        page.fonts = {"Poppins": "https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap"}
        page.theme = ft.Theme(font_family="Poppins")

        # Elementos da UI
        titulo = ft.Text("Sistema de Veículos",size=36,weight=ft.FontWeight.BOLD,color=ft.Colors.WHITE,text_align=ft.TextAlign.CENTER) 
        subtitulo = ft.Text("Gerenciamento completo de frota e vendas",size=16,color=ft.Colors.WHITE70,text_align=ft.TextAlign.CENTER)
        
        # Funções dos botões
        def fechar_app(e):
            page.clean()
            page.update()
            page.vertical_alignment = ft.MainAxisAlignment.CENTER
            page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
            page.add(ft.Text("Aplicação fechada."))
            session.close()
            
        def mostrar_veiculos(e):
            page.clean()
            MenuCarros.menu_carros(page)

        def mostrar_vendas(e):
            page.clean()
            MenuVendas.menu_vendas(page)
        
        def mostrar_feedback(e):
            page.clean()
            MenuFeedback.menu_feedback(page)

        def mostrar_chamado(e):
            page.clean()
            MenuChamado.menu_chamado(page)
        
        def mostrar_orcamento(e):
            page.clean()
            MenuOrcamento.menu_orcamento(page)
        
        def mostrar_diagnostico(e):
            page.clean()
            MenuDiagnostico.menu_diagnostico(page)
        
        def mostrar_itens(e):
            page.clean()
            MenuItens.menu_itens(page)

        def mostrar_adm(e):
            page.clean()
            MenuAdm.menu_adm(page)


        # Estilo do botão, só precisando alterar os textos e ícones
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
                width=280,
                height=45
                ),
                margin=ft.margin.only(bottom=15),
                animate=ft.Animation(300, "easeInOut")
            )
        
        botao_cadastros = criar_botao("Veículos", ft.Icons.CAR_RENTAL, mostrar_veiculos, ft.Colors.TEAL_700)
        botao_vendas = criar_botao("Vendas", ft.Icons.SHOPPING_CART, mostrar_vendas, ft.Colors.INDIGO_700)
        botao_feedback = criar_botao("Feedback", ft.Icons.FEEDBACK, mostrar_feedback, ft.Colors.ORANGE_700)
        botao_chamado = criar_botao("Chamados", ft.Icons.ASSIGNMENT, mostrar_chamado, ft.Colors.YELLOW_700)
        botao_orcamento = criar_botao("Orçamento", ft.Icons.MONEY, mostrar_orcamento, ft.Colors.PURPLE_700)
        botao_diagnostico = criar_botao("Diagnóstico", ft.Icons.TROUBLESHOOT, mostrar_diagnostico, ft.Colors.GREEN_700)
        botao_item = criar_botao("Itens", ft.Icons.ADD_BOX, mostrar_itens, ft.Colors.TEAL_700)
        botao_fechar_app = criar_botao("Fechar Aplicação", ft.Icons.EXIT_TO_APP, fechar_app, ft.Colors.RED_700)
        botao_adm = criar_botao("Painel ADM", ft.Icons.SECURITY, mostrar_adm, ft.Colors.BROWN)
        
        
        # Layout principal
        conteudo = ft.Column(
            [
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Icon(name=ft.Icons.DIRECTIONS_CAR, size=50, color=ft.Colors.WHITE),
                            titulo,
                            subtitulo,
                            ft.Divider(height=40, color=ft.Colors.TRANSPARENT),
                            botao_cadastros,
                            botao_vendas,
                            botao_feedback,
                            botao_chamado,
                            botao_diagnostico,
                            botao_orcamento,
                            botao_item,
                            ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                            botao_fechar_app,
                            botao_adm,
                            ft.Divider(height=20, color=ft.Colors.TRANSPARENT)
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=2
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
                    ft.Image(
                        imagem_fundo,
                        width=page.width,
                        height=page.height,
                        fit=ft.ImageFit.COVER,
                        opacity=0.7
                    ),
                    ft.Container(
                        content=ft.Column(
                            [conteudo],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER
                        ),
                        expand=True
                    )
                ],
                expand=True))
        
class MenuCarros:       
    def menu_carros(page: ft.Page):
        page.title = "Menu Carros"
        page.theme_mode = ft.ThemeMode.DARK
        page.padding = 0
        page.fonts = {"Poppins": "https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap"}
        page.theme = ft.Theme(font_family="Poppins")

        titulo = ft.Text("Veículos", size=36, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE, text_align=ft.TextAlign.CENTER)
        subtitulo = ft.Text("Gerenciamento de veículos", size=16, color=ft.Colors.WHITE70, text_align=ft.TextAlign.CENTER)
        
        # Espaço para o conteúdo dinâmico
        content_column = ft.Column([], expand=True)

        def voltar_menu(e):
            page.clean()
            Menu_principal(page)
            
        def cadastrar_veiculo(e):
            from Models.veiculos import cadastros_de_veiculo
            content_column.controls = [cadastros_de_veiculo(page)]
            page.update()
            
        def veiculos_cadastrados(e):
            from Models.veiculos import listar_veiculos
            content_column.controls = [listar_veiculos(page)]
            page.update()
            
        def alterar_cadastro_veiculo(e):
            from Models.veiculos import alterar_cadastro
            content_column.controls = [alterar_cadastro(page)]
            page.update()

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
        
        botao_cadastrar = criar_botao("Cadastrar Veículo", ft.Icons.ADD, cadastrar_veiculo, ft.Colors.TEAL_700)
        botao_listar = criar_botao("Listar Veículos", ft.Icons.LIST, veiculos_cadastrados, ft.Colors.INDIGO_700)
        botao_alterar = criar_botao("Alterar Veículo", ft.Icons.EDIT, alterar_cadastro_veiculo, ft.Colors.PURPLE_700)
        botao_voltar = criar_botao("Voltar ao Menu Principal", ft.Icons.ARROW_BACK, voltar_menu, ft.Colors.ORANGE_700)
            
        # Layout do menu (coluna à esquerda)
        menu_column = ft.Column(
            [
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Icon(name=ft.Icons.DIRECTIONS_CAR, size=50, color=ft.Colors.WHITE),
                            titulo,
                            subtitulo,
                            ft.Divider(height=40, color=ft.Colors.TRANSPARENT),
                            botao_cadastrar,
                            botao_listar,
                            botao_alterar,
                            ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                            botao_voltar
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
        
        # Layout principal (menu à esquerda e conteúdo à direita)
        main_row = ft.Row(
    [
        menu_column,  # Menu à esquerda (fixo)
        ft.Container(  # Área central expandível
            content=ft.Row(
                [
                    content_column  # Conteúdo será centralizado dentro desta linha
                ],
                alignment=ft.MainAxisAlignment.CENTER,  # Centraliza horizontalmente
                vertical_alignment=ft.CrossAxisAlignment.CENTER  # Centraliza verticalmente
            ),
            expand=True
        )
    ],
    expand=True,
    spacing=300  # Espaçamento entre o menu e o conteúdo
)
        
        page.add(
            ft.Stack(
                [
                    ft.Image(
                        imagem_fundo,
                        width=page.width,
                        height=page.height,
                        fit=ft.ImageFit.COVER,
                        opacity=0.7
                    ),
                    ft.Container(
                        content=main_row,
                        expand=True
                    )
                ],
                expand=True
            )
        )

class MenuVendas:
    def menu_vendas(page: ft.Page):
        page.title = "Menu de Vendas"
        page.theme_mode = ft.ThemeMode.DARK
        page.padding = 0
        page.fonts = {"Poppins": "https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap"}
        page.theme = ft.Theme(font_family="Poppins")

        titulo = ft.Text("Vendas",size=36,weight=ft.FontWeight.BOLD,color=ft.Colors.WHITE,text_align=ft.TextAlign.CENTER) 
        subtitulo = ft.Text("Gerenciamento de vendas",size=16,color=ft.Colors.WHITE70,text_align=ft.TextAlign.CENTER)
        
        # Espaço para o conteúdo dinâmico
        content_column = ft.Column([], expand=True)

        def voltar_menu(e):
            page.clean()
            Menu_principal(page)

        def cadastrar_venda(e):
            from Models.vendas import cadastrar_venda
            content_column.controls = [cadastrar_venda(page)]
            page.update()

        def listar_vendas(e):
            from Models.vendas import listar_vendas
            content_column.controls = [listar_vendas(page)]
            page.update()

        def alterar_venda(e):
            from Models.vendas import alterar_venda
            content_column.controls = [alterar_venda(page)]
            page.update()

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
                animate=ft.Animation(300, "easeInOut"))
        
        botao_cadastrar = criar_botao("Cadastrar Venda", ft.Icons.ADD, cadastrar_venda, ft.Colors.TEAL_700)
        botao_listar = criar_botao("Listar Vendas", ft.Icons.LIST, listar_vendas, ft.Colors.INDIGO_700)
        botao_alterar = criar_botao("Alterar Venda", ft.Icons.EDIT, alterar_venda, ft.Colors.PURPLE_700)
        botao_voltar = criar_botao("Voltar ao Menu Principal", ft.Icons.ARROW_BACK, voltar_menu, ft.Colors.ORANGE_700)

        menu_column = ft.Column(
            [
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Icon(name=ft.Icons.SHOPPING_CART, size=50, color=ft.Colors.WHITE),
                            titulo,
                            subtitulo,
                            ft.Divider(height=40, color=ft.Colors.TRANSPARENT),
                            botao_cadastrar,
                            botao_listar,
                            botao_alterar,
                            ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                            botao_voltar
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
        
        # Layout principal (menu à esquerda e conteúdo à direita)
        main_row = ft.Row(
    [
        menu_column,  # Menu à esquerda (fixo)
        ft.Container(  # Área central expandível
            content=ft.Row(
                [
                    content_column  # Conteúdo será centralizado dentro desta linha
                ],
                alignment=ft.MainAxisAlignment.CENTER,  # Centraliza horizontalmente
                vertical_alignment=ft.CrossAxisAlignment.CENTER  # Centraliza verticalmente
            ),
            expand=True
        )
    ],
    expand=True,
    spacing=300  # Espaçamento entre o menu e o conteúdo
)
        
        page.add(
            ft.Stack(
                [
                    ft.Image(
                        imagem_fundo,
                        width=page.width,
                        height=page.height,
                        fit=ft.ImageFit.COVER,
                        opacity=0.7
                    ),
                    ft.Container(
                        content=main_row,
                        expand=True
                    )
                ],
                expand=True
            )
        )

class MenuFeedback():
    def menu_feedback(page: ft.Page):
        page.title = "Menu Feedback"
        page.theme_mode = ft.ThemeMode.DARK
        page.padding = 0
        page.fonts = {"Poppins": "https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap"}
        page.theme = ft.Theme(font_family="Poppins")

        titulo = ft.Text("Feedback",size=36,weight=ft.FontWeight.BOLD,color=ft.Colors.WHITE,text_align=ft.TextAlign.CENTER)
        subtitulo = ft.Text("Gerenciamento de Feedback",size=16,color=ft.Colors.WHITE70,text_align=ft.TextAlign.CENTER)
        
        # Espaço para o conteúdo dinâmico
        content_column = ft.Column([], expand=True)

        def voltar_menu(e):
            page.clean()
            Menu_principal(page)
            page.update()

        def cadastro_feedback(e):
            from Models.feedback import cadastro_de_feedback
            content_column.controls = [cadastro_de_feedback(page)]
            page.update()

        def listar_feedback(e):
            from Models.feedback import listar_feedback
            content_column.controls = [listar_feedback(page)]
            page.update()

        def alterar_feedback(e):
            from Models.feedback import alterar_feedback
            content_column.controls = [alterar_feedback(page)]
            page.update()

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
                animate=ft.Animation(300, "easeInOut"))
        
        botao_cadastrar = criar_botao("Cadastrar feedback", ft.Icons.ADD, cadastro_feedback, ft.Colors.TEAL_700)
        botao_listar = criar_botao("Listar feedback", ft.Icons.LIST, listar_feedback, ft.Colors.INDIGO_700)
        botao_alterar = criar_botao("Alterar feedback", ft.Icons.EDIT, alterar_feedback, ft.Colors.PURPLE_700)
        botao_voltar = criar_botao("Voltar ao Menu Principal", ft.Icons.ARROW_BACK, voltar_menu, ft.Colors.ORANGE_700)

        menu_column = ft.Column(
            [
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Icon(name=ft.Icons.REPORT, size=50, color=ft.Colors.WHITE),
                            titulo,
                            subtitulo,
                            ft.Divider(height=40, color=ft.Colors.TRANSPARENT),
                            botao_cadastrar,
                            botao_listar,
                            botao_alterar,
                            ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                            botao_voltar
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
        
        # Layout principal (menu à esquerda e conteúdo à direita)
        main_row = ft.Row(
    [
        menu_column,  # Menu à esquerda (fixo)
        ft.Container(  # Área central expandível
            content=ft.Row(
                [
                    content_column  # Conteúdo será centralizado dentro desta linha
                ],
                alignment=ft.MainAxisAlignment.CENTER,  # Centraliza horizontalmente
                vertical_alignment=ft.CrossAxisAlignment.CENTER  # Centraliza verticalmente
            ),
            expand=True
        )
    ],
    expand=True,
    spacing=300  # Espaçamento entre o menu e o conteúdo
)
        
        page.add(
            ft.Stack(
                [
                    ft.Image(
                        imagem_fundo,
                        width=page.width,
                        height=page.height,
                        fit=ft.ImageFit.COVER,
                        opacity=0.7
                    ),
                    ft.Container(
                        content=main_row,
                        expand=True
                    )
                ],
                expand=True
            )
        )

class MenuChamado():
    def menu_chamado(page: ft.Page):
        page.title = "Menu de Chamados"
        page.theme_mode = ft.ThemeMode.DARK
        page.padding = 0
        page.fonts = {"Poppins": "https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap"}
        page.theme = ft.Theme(font_family="Poppins")

        titulo = ft.Text("Chamados",size=36,weight=ft.FontWeight.BOLD,color=ft.Colors.WHITE,text_align=ft.TextAlign.CENTER)
        subtitulo = ft.Text("Gerenciamento de Chamados",size=16,color=ft.Colors.WHITE70,text_align=ft.TextAlign.CENTER)
        
        # Espaço para o conteúdo dinâmico
        content_column = ft.Column([], expand=True)

        def voltar_menu(e):
            page.clean()
            Menu_principal(page)

        def cadastrar_chamado(e):
            from Models.chamado import cadastro_de_chamado
            content_column.controls = [cadastro_de_chamado(page)]
            page.update()
            
        def listar_chamado(e):
            from Models.chamado import listar_chamados
            content_column.controls = [listar_chamados(page)]
            page.update()
            
        def alterar_chamado(e):
            from Models.chamado import alterar_cadastro
            content_column.controls = [alterar_cadastro(page)]
            page.update()

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
        
        botao_cadastrar = criar_botao("Cadastrar Chamado", ft.Icons.ADD, cadastrar_chamado, ft.Colors.TEAL_700)
        botao_listar = criar_botao("Listar Chamado", ft.Icons.LIST, listar_chamado, ft.Colors.INDIGO_700)
        botao_alterar = criar_botao("Alterar Chamado", ft.Icons.EDIT, alterar_chamado, ft.Colors.PURPLE_700)
        botao_voltar = criar_botao("Voltar ao Menu Principal", ft.Icons.ARROW_BACK, voltar_menu, ft.Colors.ORANGE_700)

        menu_column = ft.Column(
            [
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Icon(name=ft.Icons.ASSIGNMENT, size=50, color=ft.Colors.WHITE),
                            titulo,
                            subtitulo,
                            ft.Divider(height=40, color=ft.Colors.TRANSPARENT),
                            botao_cadastrar,
                            botao_listar,
                            botao_alterar,
                            ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                            botao_voltar
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
        
        # Layout principal (menu à esquerda e conteúdo à direita)
        main_row = ft.Row(
    [
        menu_column,  # Menu à esquerda (fixo)
        ft.Container(  # Área central expandível
            content=ft.Row(
                [
                    content_column  # Conteúdo será centralizado dentro desta linha
                ],
                alignment=ft.MainAxisAlignment.CENTER,  # Centraliza horizontalmente
                vertical_alignment=ft.CrossAxisAlignment.CENTER  # Centraliza verticalmente
            ),
            expand=True
        )
    ],
    expand=True,
    spacing=300  # Espaçamento entre o menu e o conteúdo
)
        
        page.add(
            ft.Stack(
                [
                    ft.Image(
                        imagem_fundo,
                        width=page.width,
                        height=page.height,
                        fit=ft.ImageFit.COVER,
                        opacity=0.7
                    ),
                    ft.Container(
                        content=main_row,
                        expand=True
                    )
                ],
                expand=True
            )
        )

class MenuDiagnostico():
    def menu_diagnostico(page: ft.Page):
        page.title = "Menu Diagnostico"
        page.theme_mode = ft.ThemeMode.DARK
        page.padding = 0
        page.fonts = {"Poppins": "https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap"}
        page.theme = ft.Theme(font_family="Poppins")

        titulo = ft.Text("Diagnostico",size=36,weight=ft.FontWeight.BOLD,color=ft.Colors.WHITE,text_align=ft.TextAlign.CENTER)
        subtitulo = ft.Text("Gerenciamento de Diagnostico",size=16,color=ft.Colors.WHITE70,text_align=ft.TextAlign.CENTER)
        
        # Espaço para o conteúdo dinâmico
        content_column = ft.Column([], expand=True)

        def voltar_menu(e):
            page.clean()
            Menu_principal(page)
            page.update()

        def cadastro_diagnostico(e):
            from Models.diagnostico import cadastro_de_diagnostico
            content_column.controls = [cadastro_de_diagnostico(page)]
            page.update()

        def listar_diagnostico(e):
            from Models.diagnostico import listar_diagnostico
            content_column.controls = [listar_diagnostico(page)]
            page.update()

        def alterar_diagnostico(e):
            from Models.diagnostico import alterar_diagnostico
            content_column.controls = [alterar_diagnostico(page)]
            page.update()

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
                animate=ft.Animation(300, "easeInOut"))
        
        botao_cadastrar = criar_botao("Cadastrar diagnostico", ft.Icons.ADD, cadastro_diagnostico, ft.Colors.TEAL_700)
        botao_listar = criar_botao("Listar diagnostico", ft.Icons.LIST, listar_diagnostico, ft.Colors.INDIGO_700)
        botao_alterar = criar_botao("Alterar diagnostico", ft.Icons.EDIT, alterar_diagnostico, ft.Colors.PURPLE_700)
        botao_voltar = criar_botao("Voltar ao Menu Principal", ft.Icons.ARROW_BACK, voltar_menu, ft.Colors.ORANGE_700)

        menu_column = ft.Column(
            [
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Icon(name=ft.Icons.TROUBLESHOOT, size=50, color=ft.Colors.WHITE),
                            titulo,
                            subtitulo,
                            ft.Divider(height=40, color=ft.Colors.TRANSPARENT),
                            botao_cadastrar,
                            botao_listar,
                            botao_alterar,
                            ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                            botao_voltar
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
        
        # Layout principal (menu à esquerda e conteúdo à direita)
        main_row = ft.Row(
    [
        menu_column,  # Menu à esquerda (fixo)
        ft.Container(  # Área central expandível
            content=ft.Row(
                [
                    content_column  # Conteúdo será centralizado dentro desta linha
                ],
                alignment=ft.MainAxisAlignment.CENTER,  # Centraliza horizontalmente
                vertical_alignment=ft.CrossAxisAlignment.CENTER  # Centraliza verticalmente
            ),
            expand=True
        )
    ],
    expand=True,
    spacing=300  # Espaçamento entre o menu e o conteúdo
)
        
        page.add(
            ft.Stack(
                [
                    ft.Image(
                        imagem_fundo,
                        width=page.width,
                        height=page.height,
                        fit=ft.ImageFit.COVER,
                        opacity=0.7
                    ),
                    ft.Container(
                        content=main_row,
                        expand=True
                    )
                ],
                expand=True
            )
        )

class MenuOrcamento():
    def menu_orcamento(page: ft.Page):
        page.title = "Menu de Orçamentos"
        page.theme_mode = ft.ThemeMode.DARK
        page.padding = 0
        page.fonts = {"Poppins": "https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap"}
        page.theme = ft.Theme(font_family="Poppins")

        titulo = ft.Text("Orçamentos",size=36,weight=ft.FontWeight.BOLD,color=ft.Colors.WHITE,text_align=ft.TextAlign.CENTER)
        subtitulo = ft.Text("Gerenciamento de Orçamentos",size=16,color=ft.Colors.WHITE70,text_align=ft.TextAlign.CENTER)
        
        # Espaço para o conteúdo dinâmico
        content_column = ft.Column([], expand=True)

        def voltar_menu(e):
            page.clean()
            Menu_principal(page)

        def cadastrar_orcamento(e):
            from Models.orcamento import cadastro_de_orcamento
            content_column.controls = [cadastro_de_orcamento(page)]
            page.update()
            
        def listar_orcamento(e):
            from Models.orcamento import listar_orcamento
            content_column.controls = [listar_orcamento(page)]
            page.update()

        def listar_orcamento_venda(e):
            from Models.orcamento import listar_orcamento_por_venda
            content_column.controls = [listar_orcamento_por_venda(page, session)]
            page.update()
            
        def alterar_orcamento(e):
            from Models.orcamento import alterar_orcamento
            content_column.controls = [alterar_orcamento(page)]
            page.update()

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
        
        botao_cadastrar = criar_botao("Cadastrar Orçamento", ft.Icons.ADD, cadastrar_orcamento, ft.Colors.TEAL_700)
        botao_listar = criar_botao("Listar Orçamento", ft.Icons.LIST, listar_orcamento, ft.Colors.INDIGO_700)
        botao_lista_venda = criar_botao("Listar Orçamento por Venda", ft.Icons.LIST, listar_orcamento_venda, ft.Colors.INDIGO_700)
        botao_alterar = criar_botao("Alterar Orçamento", ft.Icons.EDIT, alterar_orcamento, ft.Colors.PURPLE_700)
        botao_voltar = criar_botao("Voltar ao Menu Principal", ft.Icons.ARROW_BACK, voltar_menu, ft.Colors.ORANGE_700)

        menu_column = ft.Column(
            [
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Icon(name=ft.Icons.ASSIGNMENT, size=50, color=ft.Colors.WHITE),
                            titulo,
                            subtitulo,
                            ft.Divider(height=40, color=ft.Colors.TRANSPARENT),
                            botao_cadastrar,
                            botao_listar,
                            botao_lista_venda,
                            botao_alterar,
                            ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                            botao_voltar
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
        
        # Layout principal (menu à esquerda e conteúdo à direita)
        main_row = ft.Row(
    [
        menu_column,  # Menu à esquerda (fixo)
        ft.Container(  # Área central expandível
            content=ft.Row(
                [
                    content_column  # Conteúdo será centralizado dentro desta linha
                ],
                alignment=ft.MainAxisAlignment.CENTER,  # Centraliza horizontalmente
                vertical_alignment=ft.CrossAxisAlignment.CENTER  # Centraliza verticalmente
            ),
            expand=True
        )
    ],
    expand=True,
    spacing=300  # Espaçamento entre o menu e o conteúdo
)
        
        page.add(
            ft.Stack(
                [
                    ft.Image(
                        imagem_fundo,
                        width=page.width,
                        height=page.height,
                        fit=ft.ImageFit.COVER,
                        opacity=0.7
                    ),
                    ft.Container(
                        content=main_row,
                        expand=True
                    )
                ],
                expand=True
            )
        )

class MenuItens():
    def menu_itens(page: ft.Page):
        page.title = "Menu Itens"
        page.theme_mode = ft.ThemeMode.DARK
        page.padding = 0
        page.fonts = {"Poppins": "https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap"}
        page.theme = ft.Theme(font_family="Poppins")

        titulo = ft.Text("Itens", size=36, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE,
                         text_align=ft.TextAlign.CENTER)
        subtitulo = ft.Text("Gerenciamento de Itens", size=16, color=ft.Colors.WHITE70,
                            text_align=ft.TextAlign.CENTER)

        # Espaço para o conteúdo dinâmico
        content_column = ft.Column([], expand=True)

        def voltar_menu(e):
            page.clean()
            Menu_principal(page)
            page.update()

        def cadastro_de_itens(e):
            from Models.item import cadastro_de_itens
            content_column.controls = [cadastro_de_itens(page)]
            page.update()

        def listar_itens(e):
            from Models.item import listar_itens
            content_column.controls = [listar_itens(page)]
            page.update()

        def alterar_itens(e):
            from Models.item import alterar_itens
            content_column.controls = [alterar_itens(page)]
            page.update()

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
                animate=ft.Animation(300, "easeInOut"))

        botao_cadastrar = criar_botao("Cadastrar item", ft.Icons.ADD, cadastro_de_itens, ft.Colors.TEAL_700)
        botao_listar = criar_botao("Listar itens", ft.Icons.LIST, listar_itens, ft.Colors.INDIGO_700)
        botao_alterar = criar_botao("Alterar item", ft.Icons.EDIT, alterar_itens, ft.Colors.PURPLE_700)
        botao_voltar = criar_botao("Voltar ao Menu Principal", ft.Icons.ARROW_BACK, voltar_menu, ft.Colors.ORANGE_700)

        menu_column = ft.Column(
            [
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Icon(name=ft.Icons.TROUBLESHOOT, size=50, color=ft.Colors.WHITE),
                            titulo,
                            subtitulo,
                            ft.Divider(height=40, color=ft.Colors.TRANSPARENT),
                            botao_cadastrar,
                            botao_listar,
                            botao_alterar,
                            ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                            botao_voltar
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

        # Layout principal (menu à esquerda e conteúdo à direita)
        main_row = ft.Row(
            [
                menu_column,  # Menu à esquerda (fixo)
                ft.Container(  # Área central expandível
                    content=ft.Row(
                        [
                            content_column  # Conteúdo será centralizado dentro desta linha
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,  # Centraliza horizontalmente
                        vertical_alignment=ft.CrossAxisAlignment.CENTER  # Centraliza verticalmente
                    ),
                    expand=True
                )
            ],
            expand=True,
            spacing=300  # Espaçamento entre o menu e o conteúdo
        )

        page.add(
            ft.Stack(
                [
                    ft.Image(
                        imagem_fundo,
                        width=page.width,
                        height=page.height,
                        fit=ft.ImageFit.COVER,
                        opacity=0.7
                    ),
                    ft.Container(
                        content=main_row,
                        expand=True
                    )
                ],
                expand=True
            )
        )

class MenuAdm():
    def menu_adm(page: ft.Page):
        page.title = "Menu de Administração"
        page.theme_mode = ft.ThemeMode.DARK
        page.padding = 0
        page.fonts = {"Poppins": "https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap"}
        page.theme = ft.Theme(font_family="Poppins")

        titulo = ft.Text("Administração", size=36, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE, text_align=ft.TextAlign.CENTER)
        subtitulo = ft.Text("Gerenciamento do Sistema", size=16, color=ft.Colors.WHITE70, text_align=ft.TextAlign.CENTER)

        content_column = ft.Column([], expand=True)

        def voltar_menu(e):
            page.clean()
            Menu_principal(page)

        def excluir_chamados(e):
            from Models.adm import excluir_chamado
            content_column.controls = [excluir_chamado(page)]
            page.update()

        def excluir_diagnosticos(e):
            from Models.adm import excluir_diagnostico
            content_column.controls = [excluir_diagnostico(page)]
            page.update()

        def excluir_orcamentos(e):
            from Models.adm import excluir_orcamento
            content_column.controls = [excluir_orcamento(page)]
            page.update()

        def excluir_itens(e):
            from Models.adm import excluir_item
            content_column.controls = [excluir_item(page)]
            page.update()

        def excluir_feedbacks(e):
            from Models.adm import excluir_feedback
            content_column.controls = [excluir_feedback(page)]
            page.update()

        def excluir_vendas(e):
            from Models.adm import excluir_venda
            content_column.controls = [excluir_venda(page)]
            page.update()
        
        def excluir_veiculos(e):
            from Models.adm import excluir_veiculo
            content_column.controls = [excluir_veiculo(page)]
            page.update()

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
                    width=280,
                    height=45
                ),
                margin=ft.margin.only(bottom=15),
                animate=ft.Animation(300, "easeInOut")
            )

        botao_excluir_chamado = criar_botao("Excluir Chamado", ft.Icons.DELETE, excluir_chamados, ft.Colors.RED_700)
        botao_excluir_diagnostico = criar_botao("Excluir Diagnostico", ft.Icons.DELETE, excluir_diagnosticos, ft.Colors.RED_700)
        botao_excluir_orcamento = criar_botao("Excluir Orçamento", ft.Icons.DELETE, excluir_orcamentos, ft.Colors.RED_700)
        botao_excluir_item = criar_botao("Excluir Item", ft.Icons.DELETE, excluir_itens, ft.Colors.RED_700)
        botao_excluir_feedback = criar_botao("Excluir Feedback", ft.Icons.DELETE, excluir_feedbacks, ft.Colors.RED_700)
        botao_excluir_venda = criar_botao("Excluir Venda", ft.Icons.DELETE, excluir_vendas, ft.Colors.RED_700)
        botao_excluir_veiculo = criar_botao("Excluir Veículo", ft.Icons.DELETE, excluir_veiculos, ft.Colors.RED_700)
        botao_voltar = criar_botao("Voltar ao Menu Principal", ft.Icons.ARROW_BACK, voltar_menu, ft.Colors.ORANGE_700)

        menu_column = ft.Column(
            [
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Icon(name=ft.Icons.DELETE, size=50, color=ft.Colors.WHITE),
                            titulo,
                            subtitulo,
                            botao_excluir_chamado,
                            botao_excluir_diagnostico,
                            botao_excluir_orcamento,
                            botao_excluir_item,
                            botao_excluir_feedback,
                            botao_excluir_venda,
                            botao_excluir_veiculo,
                            ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                            botao_voltar
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
        
        # Layout principal (menu à esquerda e conteúdo à direita)
        main_row = ft.Row(
    [
        menu_column,  # Menu à esquerda (fixo)
        ft.Container(  # Área central expandível
            content=ft.Row(
                [
                    content_column  # Conteúdo será centralizado dentro desta linha
                ],
                alignment=ft.MainAxisAlignment.CENTER,  # Centraliza horizontalmente
                vertical_alignment=ft.CrossAxisAlignment.CENTER  # Centraliza verticalmente
            ),
            expand=True
        )
    ],
    expand=True,
    spacing=300  # Espaçamento entre o menu e o conteúdo
)
        
        page.add(
            ft.Stack(
                [
                    ft.Image(
                        imagem_fundo,
                        width=page.width,
                        height=page.height,
                        fit=ft.ImageFit.COVER,
                        opacity=0.7
                    ),
                    ft.Container(
                        content=main_row,
                        expand=True
                    )
                ],
                expand=True
            )
        )




        