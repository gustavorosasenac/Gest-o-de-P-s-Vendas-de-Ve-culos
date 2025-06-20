import flet as ft
from DB.DB import session
from Models.veiculos import cadastros_de_veiculo, listar_veiculos, alterar_cadastro, excluir_veiculo
from Models.vendas import cadastrar_venda, listar_vendas, alterar_venda, excluir_venda



class Menu_principal:

    def __init__(self, page: ft.Page):
        page.title = "Menu Principal"
        page.theme_mode = ft.ThemeMode.DARK

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

        titulo = ft.Text("🚘 Sistema de Veículos", size=40, weight=ft.FontWeight.BOLD, color="white")

        botao_cadastros = ft.ElevatedButton(
            text="Cadastros",
            icon=ft.Icons.ASSIGNMENT,
            width=400,
            on_click=mostrar_cadastros)

        botao_vendas = ft.ElevatedButton(
            text="Vendas",
            icon=ft.Icons.SHOP,
            width=400,
            on_click=mostrar_vendas)

        botao_fechar_app = ft.ElevatedButton(
            text="Fechar Aplicação",
            icon=ft.Icons.CLOSE,
            width=400,
            on_click=fechar_app)
            
        conteudo = ft.Column(
            [titulo, botao_cadastros, botao_vendas, botao_fechar_app],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        
        page.add(
            ft.Stack(
                controls=[
                    ft.Image(
                        src="https://img.odcdn.com.br/wp-content/uploads/2024/03/shutterstock_1082263868-1.jpg",
                        fit=ft.ImageFit.COVER,
                        width=page.width,
                        height=page.height
                    ),
                    ft.Container(
                        content=conteudo,
                        alignment=ft.alignment.center,
                        padding=40,
                        bgcolor="#00000088",
                        border_radius=10
                    )
                ],
                expand=True
            )
        )
        
class MenuCarros:       
    def menu_cadastros(page: ft.Page):
        page.title = "Menu de Cadastros"
        page.theme_mode = ft.ThemeMode.DARK
        
        def voltar_menu(e):
            page.clean()
            Menu_principal(page)
            
        def cadastrar_veiculo(e):
            page.clean()
            cadastros_de_veiculo(page)
            
        def veiculos_cadastrados(e):
            page.clean()
            listar_veiculos(page)
            
        def alterar_cadastro_veiculo(e):
            page.clean()
            alterar_cadastro(page)
            
        def excluir_cadastro_veiculo(e):
            page.clean()
            excluir_veiculo(page)

        titulo = ft.Text("Cadastros", size=40, weight=ft.FontWeight.BOLD, color="white")

        botoes = [
            ft.ElevatedButton(
                text="Cadastrar Veículo",
                icon=ft.Icons.ADD,
                width=400,
                on_click=cadastrar_veiculo),
            ft.ElevatedButton(
                text="Mostrar Veículos Cadastrados",
                icon=ft.Icons.LIST,
                width=400,
                on_click=veiculos_cadastrados),
            ft.ElevatedButton(
                text="Alterar Cadastro de Veículo",
                icon=ft.Icons.EDIT,
                width=400,
                on_click=alterar_cadastro_veiculo),
            ft.ElevatedButton(
                text="Excluir Cadastro de Veículo",
                icon=ft.Icons.DELETE,
                width=400,
                on_click=excluir_cadastro_veiculo),
            ft.ElevatedButton(
                text="Voltar ao Menu Principal",
                icon=ft.Icons.ARROW_BACK,
                width=400,
                on_click=voltar_menu)
        ]
            
        conteudo = ft.Column(
            [titulo, *botoes],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        
        page.add(
            ft.Stack(
                controls=[
                    ft.Image(
                        src="https://img.odcdn.com.br/wp-content/uploads/2024/03/shutterstock_1082263868-1.jpg",
                        fit=ft.ImageFit.COVER,
                        width=page.width,
                        height=page.height
                    ),
                    ft.Container(
                        content=conteudo,
                        alignment=ft.alignment.center,
                        padding=40,
                        bgcolor="#00000088",
                        border_radius=10
                    )
                ],
                expand=True))
class MenuVendas:
    def menu_vendas(page: ft.Page):
        page.title = "Menu de Vendas"
        page.theme_mode = ft.ThemeMode.DARK
        
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



        titulo = ft.Text("Vendas", size=40, weight=ft.FontWeight.BOLD, color="white")

        botoes = [
            ft.ElevatedButton(
                text="Cadastrar Venda",
                icon=ft.Icons.ADD,
                width=400,
                on_click=cadastrar_venda),
            ft.ElevatedButton(
                text="Mostrar Vendas",
                icon=ft.Icons.LIST,
                width=400,
                on_click=listar_vendas),
            ft.ElevatedButton(
                text="Alterar Venda",
                icon=ft.Icons.EDIT,
                width=400,
                on_click=alterar_venda),
            ft.ElevatedButton(
                text="Excluir Venda",
                icon=ft.Icons.DELETE,
                width=400,
                on_click=excluir_venda),
            ft.ElevatedButton(
                text="Voltar ao Menu Principal",
                icon=ft.Icons.ARROW_BACK,
                width=400,
                on_click=voltar_menu)
        ]
            
        conteudo = ft.Column(
            [titulo, *botoes],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        
        page.add(
            ft.Stack(
                controls=[
                    ft.Image(
                        src="https://img.odcdn.com.br/wp-content/uploads/2024/03/shutterstock_1082263868-1.jpg",
                        fit=ft.ImageFit.COVER,
                        width=page.width,
                        height=page.height
                    ),
                    ft.Container(
                        content=conteudo,
                        alignment=ft.alignment.center,
                        padding=40,
                        bgcolor="#00000088",
                        border_radius=10
                    )
                ],
                expand=True
            )
        )

    