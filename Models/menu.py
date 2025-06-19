import flet as ft
from Models.veiculos import cadastros_de_veiculo, listar_veiculos, alterar_cadastro, excluir_veiculo
from Models.vendas import cadastrar, listar_vendas, alterar_venda, excluir_venda

def menu_cadastros(page: ft.Page):
    page.title = "Menu de Cadastros"
    page.theme_mode = ft.ThemeMode.DARK
    
    def voltar_menu(e):
        page.clean()
        menu_cadastros(page)
        
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

def menu_vendas(page: ft.Page):
    page.title = "Menu de Vendas"
    page.theme_mode = ft.ThemeMode.DARK
    
    def voltar_menu(e):
        page.clean()
        menu_principal(page)

    def listar(e):
        page.clean()
        listar_vendas(page)

    def alterar(e):
        page.clean()
        alterar_venda(page)

    def excluir(e):
        page.clean()
        excluir_venda(page)

    titulo = ft.Text("Vendas", size=40, weight=ft.FontWeight.BOLD, color="white")

    botoes = [
        ft.ElevatedButton(
            text="Cadastrar Venda",
            icon=ft.Icons.ADD,
            width=400,
            on_click=cadastrar),
        ft.ElevatedButton(
            text="Mostrar Vendas",
            icon=ft.Icons.LIST,
            width=400,
            on_click=listar),
        ft.ElevatedButton(
            text="Alterar Venda",
            icon=ft.Icons.EDIT,
            width=400,
            on_click=alterar),
        ft.ElevatedButton(
            text="Excluir Venda",
            icon=ft.Icons.DELETE,
            width=400,
            on_click=excluir),
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