import flet as ft
from DB.Database import session

class Menu_principal:

    def __init__(self, page: ft.Page):
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
            
        def mostrar_cadastros(e):
            page.clean()
            MenuCarros.menu_cadastros(page)

        def mostrar_vendas(e):
            page.clean()
            MenuVendas.menu_vendas(page)

        def mostrar_pos_venda(e):
            page.clean()
            MenuPosvenda.menu_pos(page)

        
        
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
                width=300,
                height=60
                ),
                margin=ft.margin.only(bottom=15),
                animate=ft.Animation(300, "easeInOut")
            )
        
        botao_cadastros = criar_botao("Cadastros", ft.Icons.CAR_RENTAL, mostrar_cadastros, ft.Colors.TEAL_700)
        botao_vendas = criar_botao("Vendas", ft.Icons.SHOPPING_CART, mostrar_vendas, ft.Colors.INDIGO_700)
        botao_pos_venda = criar_botao("Pós-Vendas", ft.Icons.ASSIGNMENT_RETURN, mostrar_pos_venda, ft.Colors.PURPLE_700)
        botao_fechar_app = criar_botao("Fechar Aplicação", ft.Icons.EXIT_TO_APP, fechar_app, ft.Colors.RED_700)
        
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
                            botao_pos_venda,
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
                    ft.Image(
                        src="https://images.unsplash.com/photo-1494976388531-d1058494cdd8",
                        width=page.width,
                        height=page.height,
                        fit=ft.ImageFit.COVER,
                        opacity=0.7
                    ),
                    ft.Container(
                        gradient=ft.LinearGradient(
                            begin=ft.alignment.top_center,
                            end=ft.alignment.bottom_center,
                            colors=[ft.Colors.with_opacity(0.5, ft.Colors.BLACK), ft.Colors.BLACK]
                        ),
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
    def menu_cadastros(page: ft.Page):
        page.title = "Menu de Cadastros"
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
            
        def excluir_cadastro_veiculo(e):
            from Models.veiculos import excluir_veiculo
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
                    width=300,
                    height=60
                ),
                margin=ft.margin.only(bottom=15),
                animate=ft.Animation(300, "easeInOut")
            )
        
        botao_cadastrar = criar_botao("Cadastrar Veículo", ft.Icons.ADD, cadastrar_veiculo, ft.Colors.TEAL_700)
        botao_listar = criar_botao("Listar Veículos", ft.Icons.LIST, veiculos_cadastrados, ft.Colors.INDIGO_700)
        botao_alterar = criar_botao("Alterar Veículo", ft.Icons.EDIT, alterar_cadastro_veiculo, ft.Colors.PURPLE_700)
        botao_excluir = criar_botao("Excluir Veículo", ft.Icons.DELETE, excluir_cadastro_veiculo, ft.Colors.RED_700)
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
                            botao_excluir,
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
        ft.Container(  # Espaço flexível para o conteúdo
            content=content_column,
            expand=True,
            padding=ft.padding.only(left=50)  # Ajuste opcional para afastar mais
        )
    ],
    expand=True,
    spacing=0  # Remove espaçamento entre colunas
)
        
        page.add(
            ft.Stack(
                [
                    ft.Image(
                        src="https://images.unsplash.com/photo-1494976388531-d1058494cdd8",
                        width=page.width,
                        height=page.height,
                        fit=ft.ImageFit.COVER,
                        opacity=0.7
                    ),
                    ft.Container(
                        gradient=ft.LinearGradient(
                            begin=ft.alignment.top_center,
                            end=ft.alignment.bottom_center,
                            colors=[ft.Colors.with_opacity(0.5, ft.Colors.BLACK), ft.Colors.BLACK]
                        ),
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
        
        def voltar_menu(e):
            page.clean()
            Menu_principal(page)

        def cadastrar_venda(e):
            page.clean()
            from Models.vendas import cadastrar_venda
            cadastrar_venda(page)

        def listar_vendas(e):
            page.clean()
            from Models.vendas import listar_vendas
            listar_vendas(page)

        def alterar_venda(e):
            page.clean()
            from Models.vendas import alterar_venda
            alterar_venda(page)

        def excluir_venda(e):
            page.clean()
            from Models.vendas import excluir_venda
            excluir_venda(page)

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
        botao_excluir = criar_botao("Excluir Venda", ft.Icons.DELETE, excluir_venda, ft.Colors.RED_700)
        botao_voltar = criar_botao("Voltar ao Menu Principal", ft.Icons.ARROW_BACK, voltar_menu, ft.Colors.ORANGE_700)

        conteudo = ft.Column(
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
                            botao_excluir,
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
            horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        
        page.add(
            ft.Stack(
                [
                    ft.Image(
                        src="https://images.unsplash.com/photo-1494976388531-d1058494cdd8",
                        width=page.width,
                        height=page.height,
                        fit=ft.ImageFit.COVER,
                        opacity=0.7
                    ),
                    ft.Container(
                        gradient=ft.LinearGradient(
                            begin=ft.alignment.top_center,
                            end=ft.alignment.bottom_center,
                            colors=[ft.Colors.with_opacity(0.5, ft.Colors.BLACK), ft.Colors.BLACK]
                        ),
                        content=ft.Column(
                            [conteudo],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER
                        ),
                        expand=True
                    )
                ],
                expand=True))


class MenuPosvenda:       
    def menu_pos(page: ft.Page):
        page.title = "Menu Pós Venda"
        page.theme_mode = ft.ThemeMode.DARK
        page.padding = 0
        page.fonts = {"Poppins": "https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap"}
        page.theme = ft.Theme(font_family="Poppins")

        titulo = ft.Text("Pós Vendas",size=36,weight=ft.FontWeight.BOLD,color=ft.Colors.WHITE,text_align=ft.TextAlign.CENTER)
        subtitulo = ft.Text("Gerenciamento de Pós Vendas",size=16,color=ft.Colors.WHITE70,text_align=ft.TextAlign.CENTER)
        
        def voltar_menu(e):
            page.clean()
            Menu_principal(page)
            
        def cadastrar_ocorrencia(e):
            from Models.pos_venda import registrar_ocorrencia
            page.clean()
            registrar_ocorrencia(page)

        def historico_problema_veiculo(e):
            from Models.pos_venda import procurar_veiculo
            page.clean()
            procurar_veiculo(page)
            
        def alterar_ocorrencia(e):
            pass

        def excluir_ocorrencia(e):
            pass

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
        botao_cadastrar = criar_botao("Cadastrar Veículo", ft.Icons.ADD, cadastrar_ocorrencia, ft.Colors.TEAL_700)
        botao_historico = criar_botao("Listar Veículos", ft.Icons.LIST, historico_problema_veiculo, ft.Colors.INDIGO_700)
        botao_alterar = criar_botao("Alterar Veículo", ft.Icons.EDIT, alterar_ocorrencia, ft.Colors.PURPLE_700)
        botao_excluir = criar_botao("Excluir Veículo", ft.Icons.DELETE, excluir_ocorrencia, ft.Colors.RED_700)
        botao_voltar = criar_botao("Voltar ao Menu Principal", ft.Icons.ARROW_BACK, voltar_menu, ft.Colors.ORANGE_700)

        conteudo = ft.Column(
            [
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Icon(name=ft.Icons.DIRECTIONS_CAR, size=50, color=ft.Colors.WHITE),
                            titulo,
                            subtitulo,
                            ft.Divider(height=40, color=ft.Colors.TRANSPARENT),
                            botao_cadastrar,
                            botao_historico,
                            botao_alterar,
                            botao_excluir,
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
        
        page.add(
            ft.Stack(
                [
                    ft.Image(
                        src="https://images.unsplash.com/photo-1494976388531-d1058494cdd8",
                        width=page.width,
                        height=page.height,
                        fit=ft.ImageFit.COVER,
                        opacity=0.7
                    ),
                    ft.Container(
                        gradient=ft.LinearGradient(
                            begin=ft.alignment.top_center,
                            end=ft.alignment.bottom_center,
                            colors=[ft.Colors.with_opacity(0.5, ft.Colors.BLACK), ft.Colors.BLACK]
                        ),
                        content=ft.Column(
                            [conteudo],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER
                        ),
                        expand=True
                    )
                ],
                expand=True))