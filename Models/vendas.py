import flet as ft
from DB.Database import session
from DB.Tables.table_vendas import Vendas, VendaVeiculo
from datetime import datetime

dlg_erros = ft.AlertDialog(
    title=ft.Text("Erro!", color="red", text_align=ft.TextAlign.CENTER),
    content=ft.Text("", color="red", size=20),
    alignment=ft.alignment.center,
    title_padding = ft.padding.all(25))

dlg_sucesso = ft.AlertDialog(
    title=ft.Text("Sucesso!", color="green", text_align=ft.TextAlign.CENTER),
    content=ft.Text("Veículo cadastrado com sucesso!", color="green", size=20),
    alignment=ft.alignment.center,
    title_padding = ft.padding.all(25))

dlg_ja_cadastrado = ft.AlertDialog(
    title=ft.Text("Erro!", color="red"),
    content=ft.Text("Veículo já cadastrado", color="red", size=20),
    alignment=ft.alignment.center,
    title_padding = ft.padding.all(25))

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

def cadastrar_venda(page: ft.Page):
    id_veiculo = ft.TextField(label="ID do Veículo Vendido", width=400)
    data_venda = ft.TextField(label="Data da Venda (DD-MM-YYYY)", width=400)
    comprador = ft.TextField(label="Comprador", width=400)
    valor = ft.TextField(label="Valor da Venda", width=400)
    
    def cadastrar_nova_venda(e):
        if not all([id_veiculo.value, data_venda.value, comprador.value, valor.value]):
            dlg_erros.content = ft.Text("Preencha todos os campos!", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        
        data_str = data_venda.value
        data_formatada = datetime.strptime(data_str, "%d-%m-%Y").date()

        verificar_cadastro = session.query(Vendas).filter(
            Vendas.data_venda == data_formatada,
            Vendas.comprador == comprador.value,
            Vendas.valor == valor.value).first()
        
        if verificar_cadastro:
            dlg_ja_cadastrado.content = ft.Text("Venda já cadastrada", color="red", size=20)
            page.open(dlg_ja_cadastrado)
            dlg_ja_cadastrado.open = True
            return
        else:
            nova_venda = Vendas(
                data_venda=data_formatada,
                comprador=comprador.value,
                valor=valor.value)
            
            session.add(nova_venda)
            venda_veiculo = VendaVeiculo(
                id_veiculo=int(id_veiculo.value),
                id_vendas=nova_venda.id)
            session.add(venda_veiculo)
            session.commit()

            dlg_sucesso.content = ft.Text("Venda cadastrada com sucesso!", color="green", size=20)
            page.open(dlg_sucesso)
            dlg_sucesso.open = True
        
    botao_cadastrar = criar_botao("Cadastrar", ft.Icons.ADD, cadastrar_nova_venda, ft.Colors.TEAL_700)
    
    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Nova venda", size=50, weight=ft.FontWeight.BOLD, color="white"),
                id_veiculo,
                data_venda,
                comprador,
                valor,
                ft.Divider(height=40, color=ft.Colors.TRANSPARENT),
                botao_cadastrar,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        bgcolor=ft.Colors.with_opacity(0.90, ft.Colors.BLACK),
        border_radius=20,
        width=500,
        alignment=ft.alignment.center,
        margin=ft.margin.symmetric(vertical=130),
        padding=20
    )

def listar_vendas(page: ft.Page):

    vendas = session.query(Vendas).all()

    if not vendas:
        dlg_erros.content = ft.Text("Nenhuma venda cadastrada", color="red", size=20)
        page.open(dlg_erros)
        dlg_erros.open = True
        page.update()
        return
    
    lista_vendas = ft.ListView(
    controls=[
        ft.Container(
            content=ft.Text(f"ID: {v.id} Data: {v.data_venda} Comprador: {v.comprador} Valor: R$ {v.valor}", size=16,color=ft.Colors.WHITE),
            padding=10,
            border=ft.border.all(1, ft.Colors.GREY_800),
            margin=ft.margin.only(bottom=5))
            for v in vendas
    ],
        width=900,
        padding=10,
        spacing=5)
    
    return ft.Container(
        content=ft.Column([
            ft.Text("  Veículos Cadastrados", 
                   size=40, 
                   weight=ft.FontWeight.BOLD, 
                   color="white",
                   text_align=ft.TextAlign.LEFT),  # Alinhamento do título à esquerda
            ft.Divider(height=20),
            lista_vendas
        ],
        alignment=ft.MainAxisAlignment.START,  # Alinha no topo
        horizontal_alignment=ft.CrossAxisAlignment.START  # Alinha tudo à esquerda
        ),
        bgcolor=ft.Colors.with_opacity(0.90, ft.Colors.BLACK),
        border_radius=20,
        width=1000,
        padding=ft.padding.only(left=20, top=20, right=20, bottom=20),  # Padding igual em todos os lados
        margin=ft.margin.only(left = 20),  # Margem reduzida à esquerda
        alignment=ft.alignment.top_left)  # Alinha o container no topo esquerdo

def alterar_venda(page: ft.Page):

    id_venda = ft.TextField(label="ID da Venda", width=400)
    data_venda = ft.TextField(label="Data da Venda (DD-MM-YYYY)", width=400)
    comprador = ft.TextField(label="Comprador", width=400)
    valor = ft.TextField(label="Valor da Venda", width=400)

    def buscar_venda(e):
        if not all([id_venda.value, data_venda.value, comprador.value, valor.value]):
            dlg_erros.content = ft.Text("Preencha todos os campos!", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        
        if not id_venda.value.isdigit():
            dlg_erros.content = ft.Text("ID deve ser um número inteiro", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        
        venda = session.query(Vendas).filter(Vendas.id == int(id_venda.value)).first()
        data_str = data_venda.value
        data_formatada = datetime.strptime(data_str, "%d-%m-%Y").date()

        if not venda:
            dlg_erros.content = ft.Text("Venda não encontrada.", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
        else:
            venda.data_venda = data_formatada
            venda.comprador = comprador.value
            venda.valor = valor.value
            session.commit()

            dlg_sucesso.content = ft.Text("Venda alterada com sucesso!", color="green", size=20)
            page.open(dlg_sucesso)
            dlg_sucesso.open = True
        
    botao_alterar = criar_botao("Alterar", ft.Icons.ADD, buscar_venda, ft.Colors.TEAL_700)

    return ft.Container(
        content =ft.Column(
            [
            ft.Text("Alterar venda", size=50, weight=ft.FontWeight.BOLD, color="white"),
            id_venda,
            data_venda,
            comprador,
            valor,
            ft.Divider(height=40, color=ft.Colors.TRANSPARENT),
            botao_alterar,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,  
        ),
        bgcolor=ft.Colors.with_opacity(0.90, ft.Colors.BLACK),
        border_radius=20,
        width=500,
        alignment=ft.alignment.center,
        margin=ft.margin.symmetric(vertical=100),
        padding=20
        )

def excluir_venda(page: ft.Page):

    id_venda = ft.TextField(label="ID da Venda", width=400)

    def excluir_venda(e):
        if not id_venda.value.isdigit():
            dlg_erros.content = ft.Text("ID deve ser um número inteiro", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        
        venda = session.query(Vendas).filter(Vendas.id == int(id_venda.value)).first()
        
        if venda:
            session.delete(venda)
            session.commit()
            dlg_sucesso.content = ft.Text("Venda excluída com sucesso!", color="green", size=20)
            page.open(dlg_sucesso)
            dlg_sucesso.open = True
        else:
            dlg_erros.content = ft.Text("Venda não encontrada.", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True

    botao_excluir= criar_botao("Excluir", ft.Icons.ADD, excluir_venda, ft.Colors.RED_700)

    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Excluir Veiculo", size=30, weight=ft.FontWeight.BOLD, color="white"),
                ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                id_venda,
                ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
                botao_excluir,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        bgcolor=ft.Colors.with_opacity(0.90, ft.Colors.BLACK),
        border_radius=20,
        width=400,
        alignment=ft.alignment.center,
        margin=ft.margin.symmetric(vertical=220),
        padding=20)