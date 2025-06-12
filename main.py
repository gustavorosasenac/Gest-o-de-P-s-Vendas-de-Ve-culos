import flet as ft

def menu_principal(page: ft.Page):
    page.tittle = "Menu Principal"
    page.theme_mode = ft.ThemeMode.DARK


    def mostrar_cadastros(e):
        page.clean()
        cadastros(page)

    def mostrar_consultas(e):
        page.clean()
        consultas(page)


    titulo = ft.Text("🚘 Sistema de Veículos", size = 40, weight=ft.FontWeight.BOLD, color = "black")

    botao_cadastros = ft.ElevatedButton(
        text="Cadastros",
        icon=ft.Icon(name = "assigment"),
        width=400,
        on_click = mostrar_cadastros)
    
    botao_consultas = ft.ElevatedButton(
        text="Consultas",
        icon=ft.Icon(name = "search"),
        width=400,
        on_click = mostrar_consultas)
        
    conteudo = ft.Column(
        [titulo, ft.Divider(), botao_cadastros, botao_consultas],
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

def cadastros(page: ft.Page):
    def voltar_menu(e):
        page.clean()
        menu_principal(page)
    page.tittle = "Tela de Cadastros"
    page.add(
        ft.Column([
            ft.Text("Cadastros", size = 50, weight=ft.FontWeight.BOLD, color = "white"),
            ft.ElevatedButton(text = "Voltarao Menu", icon=ft.Icons.ARROW_BACK, on_click=voltar_menu),
            ft.ElevatedButton(text="Cadastros", icon=ft.Icon(name = "assigment"), width=400)],

            alignment = ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,))
    
def consultas(page: ft.Page):
    def voltar_menu(e):
        page.clean()
        menu_principal(page)
    page.tittle = "Tela de Consultas"
    page.add(
        ft.Column([
            ft.Text("Tela de Consultas", size=30, color = "white"),
            ft.ElevatedButton(text = "Voltarao Menu", icon=ft.Icons.ARROW_BACK, on_click=voltar_menu)],

            alignment = ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,))
    
ft.app(target = menu_principal)