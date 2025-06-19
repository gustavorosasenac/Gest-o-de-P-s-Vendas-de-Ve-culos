import flet as ft
from DB.DB import session
from Models.menu import menu_cadastros, menu_vendas


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
            menu_cadastros(page)

        def mostrar_vendas(e):
            page.clean()
            menu_vendas(page)

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

        