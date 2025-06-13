import flet as ft
from datetime import datetime
from DB import session, Base, engine
from veiculos import Veiculos

Base.metadata.create_all(engine)

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
        [titulo, botao_cadastros, botao_consultas],
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
    
    fabricante = ft.TextField(label="Fabricante", width=400)
    modelo = ft.TextField(label="Modelo", width=400)    
    ano = ft.TextField(label="Ano", width=400)
    motorizacao = ft.TextField(label="Motorização", width=400)
    cambio = ft.TextField(label="Câmbio", width=400)
    km = ft.TextField(label="KM", width=400)
    data_venda = ft.TextField(label="Data de Venda", width=400)
    sucesso_red = ft.Text("", size=20, color="red")
    sucesso_green = ft.Text("", size=20, color="green")

    def cadastrar_veiculo(e):
        if not (fabricante.value and modelo.value and ano.value and motorizacao.value and cambio.value and km.value and data_venda.value):
            sucesso_red.value = "Todos os campos são obrigatórios!"
            page.update()
            return

        novo_veiculo  = Veiculos(
            fabricante=fabricante.value,
            modelo=modelo.value,
            ano=ano.value,
            motorizacao=motorizacao.value,
            cambio=cambio.value,
            km=float(km.value),
            data_venda=datetime.strptime(data_venda.value, "%Y-%m-%d").date())
        
        session.add(novo_veiculo)
        session.commit()
        sucesso_green.value = "Veículo cadastrado com sucesso!"
        page.update()

    botao_cadastrar = ft.ElevatedButton(
            text="Cadastrar Veículo",
            icon=ft.Icon(name="add"),
            width=400,
            on_click=cadastrar_veiculo)

    page.title = "Tela de Cadastros"
    page.clean()
    page.add(
    ft.Column([
        ft.Text("Cadastros", size = 50, weight=ft.FontWeight.BOLD, color = "white"),
        fabricante,
        modelo,
        ano,
        motorizacao,
        cambio,
        km,
        data_venda,
        botao_cadastrar,
        sucesso_red,
        sucesso_green,
            
        ft.ElevatedButton(text = "Voltarao Menu", icon=ft.Icons.ARROW_BACK, on_click=voltar_menu)],
        alignment = ft.MainAxisAlignment.CENTER,
        horizontal_alignment= ft.CrossAxisAlignment.CENTER,))
    
def consultas(page: ft.Page):
    def voltar_menu(e):
        page.clean()
        menu_principal(page)
    page.title = "Tela de Consultas"
    page.add(
        ft.Column([
            ft.Text("Tela de Consultas", size=30, color = "white"),
            ft.ElevatedButton(text = "Voltar ao Menu", icon=ft.Icons.ARROW_BACK, on_click=voltar_menu)],

            alignment = ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,))
    
ft.app(target = menu_principal)