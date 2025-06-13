import flet as ft
from datetime import datetime
from DB import session, Base, engine
from veiculos import Veiculos

Base.metadata.create_all(engine)

def menu_principal(page: ft.Page):
    page.title = "Menu Principal"
    page.theme_mode = ft.ThemeMode.DARK

    def fechar_app(e):
        page.window_destroy()
        
        

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
    botao_fechar_app = ft.ElevatedButton(
        text="Fechar Aplicação",
        icon=ft.Icon(name = "close"),
        width=400,
        on_click = fechar_app)
        
    conteudo = ft.Column(
        [titulo, botao_cadastros, botao_consultas, botao_fechar_app],
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
    page.tittle = "Menu de Cadastros"
    page.theme_mode = ft.ThemeMode.DARK
    def voltar_menu(e):
        page.clean()
        menu_principal(page)
    def cadastrar_veiculo(e):
        page.clean()
        cadastros_de_veiculo(page)
    def veiculos_cadastrados(e):
        page.clean()
        consultas(page)
    def alterar_cadastro_veiculo(e):
        page.clean()
        consultas(page)
    def excluir_cadastro_veiculo(e):
        page.clean()
        consultas(page)

    titulo = ft.Text("Cadastros", size = 40, weight=ft.FontWeight.BOLD, color = "black")

    botao_cadastrar_veiculo = ft.ElevatedButton(
        text="Cadastrar Veículo",
        icon=ft.Icon(name = "assigment"),
        width=400,
        on_click = cadastrar_veiculo)
    
    botao_veiculos_cadastrados = ft.ElevatedButton(
        text="Mostrar Veículos Cadastrados",
        icon=ft.Icon(name = "search"),
        width=400,
        on_click = veiculos_cadastrados)
    botao_alterar_cadastro_veiculo = ft.ElevatedButton(
        text="Alterar Cadastro de Veículo",
        icon=ft.Icon(name = "edit"),
        width=400,
        on_click = alterar_cadastro_veiculo)
    botao_excluir_cadastro_veiculo = ft.ElevatedButton(
        text="Excluir Cadastro de Veículo",
        icon=ft.Icon(name = "delete"),
        width=400,
        on_click = excluir_cadastro_veiculo)
    botao_voltar_menu = ft.ElevatedButton(
        text="Voltar ao Menu Principal",
        icon=ft.Icon(name = "arrow_back"),
        width=400,
        on_click = voltar_menu)
        
    conteudo = ft.Column(
        [titulo, botao_cadastrar_veiculo, botao_veiculos_cadastrados, botao_alterar_cadastro_veiculo, botao_excluir_cadastro_veiculo, botao_voltar_menu],
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






















def cadastros_de_veiculo(page: ft.Page):
    def voltar_menu(e):
        page.clean()
        menu_principal(page)
    
    fabricante = ft.TextField(label="Fabricante", width=400)
    modelo = ft.TextField(label="Modelo", width=400)    
    ano = ft.TextField(label="Ano", width=400)
    motorizacao = ft.TextField(label="Motorização", width=400)
    cambio = ft.TextField(label="Câmbio", width=400)
    km = ft.TextField(label="KM", width=400)
    dlg_erro = ft.AlertDialog(
        title=ft.Text("Erro!", color="red"),
        content=ft.Text("Preencha todos os campos!", color="red", size=20),
        alignment=ft.alignment.center,
        title_padding=ft.padding.all(25),)
    dlg_sucesso = ft.AlertDialog(
        title=ft.Text("Sucesso!", color="green"),
        content=ft.Text("Veículo cadastrado com sucesso!", color="green", size=20),
        alignment=ft.alignment.center,
        title_padding=ft.padding.all(25),)
    dlg_ja_cadastrado = ft.AlertDialog(
        title=ft.Text("Erro!", color="red"),
        content=ft.Text("Veiculo ja cadastrado", color="red", size=20),
        alignment=ft.alignment.center,
        title_padding=ft.padding.all(25),)
    

    def cadastrar_veiculo(e):
        
        if not (fabricante.value and modelo.value and ano.value and motorizacao.value and cambio.value and km.value):
            dlg_erro.open = True
            page.update()
        elif not ano.value.isdigit() or not km.value.replace('.', '', 1).isdigit():
            dlg_erro.content = ft.Text("Ano deve ser um número inteiro e KM deve ser um número válido!", color="red", size=20)
            dlg_erro.open = True
            page.update()
            
        else: 
            verificar_cadastro = session.query(Veiculos).filter(Veiculos.fabricante == fabricante.value).first()
            if verificar_cadastro:
                dlg_ja_cadastrado.open = True
                page.update()
            else:
                novo_veiculo  = Veiculos(
                    fabricante=fabricante.value,
                    modelo=modelo.value,
                    ano=int(ano.value),
                    motorizacao=motorizacao.value,
                    cambio=cambio.value,
                    km=float(km.value))
        
                session.add(novo_veiculo)
                session.commit()
                dlg_sucesso.open = True
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
        botao_cadastrar,
        dlg_erro,
        dlg_sucesso,

        ft.ElevatedButton(text = "Voltar ao Menu", icon=ft.Icons.ARROW_BACK, on_click=voltar_menu)],
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
    
ft.app(target=menu_principal, view=ft.AppView.FLET_APP)