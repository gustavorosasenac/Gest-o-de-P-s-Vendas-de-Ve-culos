import flet as ft
from DB.Database import session
from DB.Tables.table_vendas import Vendas, VendaVeiculo
from datetime import datetime
from Models.veiculos import Veiculos 

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
def maiusculo(e):
        # Converte o texto para maiúsculas e atualiza
        e.control.value = e.control.value.upper()
        e.control.update()

def cadastrar_venda(page: ft.Page):
    data_venda = ft.TextField(label="Data da Venda (DD-MM-YYYY)", width=400)
    comprador = ft.TextField(label="Comprador", width=400, on_change=maiusculo)
    valor = ft.TextField(label="Valor da Venda", width=400, on_change=maiusculo)
    dropdown_marca = ft.Dropdown(label="Selecione a marca", width=400)
    dropdown_modelo = ft.Dropdown(label="Selecione o modelo", width=400, disabled=True)
    dropdown_ano = ft.Dropdown(label="Selecione o ano", width=400, disabled=True)
    dropdown_motor = ft.Dropdown(label="Selecione o motor", width=400, disabled=True)
    
    def carregar_marcas():
        dropdown_marca.options = []
        marcas = session.query(Veiculos.fabricante).distinct().all()

        for marca in marcas:
            dropdown_marca.options.append(ft.dropdown.Option(marca[0]))
            page.update()
    
    def atualizar_modelos(e):
        dropdown_modelo.disabled = False
        dropdown_modelo.options = []
        dropdown_modelo.value = None
        dropdown_ano.disabled = True
        dropdown_ano.options = []
        dropdown_ano.value = None
        dropdown_motor.disabled = True
        dropdown_motor.options = []
        dropdown_motor.value = None
        
        if dropdown_marca.value:
            modelos = session.query(Veiculos.modelo).filter(
                Veiculos.fabricante == dropdown_marca.value
            ).distinct().all()
            
            for modelo in modelos:
                dropdown_modelo.options.append(ft.dropdown.Option(modelo[0]))
        
        page.update()
    
    def atualizar_anos(e):
        dropdown_ano.disabled = False
        dropdown_ano.options = []
        dropdown_ano.value = None
        dropdown_motor.disabled = True
        dropdown_motor.options = []
        dropdown_motor.value = None
        
        if dropdown_marca.value and dropdown_modelo.value:
            anos = session.query(Veiculos.ano).filter(
                Veiculos.fabricante == dropdown_marca.value,
                Veiculos.modelo == dropdown_modelo.value
            ).distinct().order_by(Veiculos.ano.desc()).all()
            
            for ano in anos:
                dropdown_ano.options.append(ft.dropdown.Option(int(ano[0])))
        
        page.update()
    
    def atualizar_motores(e):
        dropdown_motor.disabled = False
        dropdown_motor.options = []
        dropdown_motor.value = None
        
        if dropdown_marca.value and dropdown_modelo.value and dropdown_ano.value:
            motores = session.query(Veiculos.motorizacao).filter(
                Veiculos.fabricante == dropdown_marca.value,
                Veiculos.modelo == dropdown_modelo.value,
                Veiculos.ano == int(dropdown_ano.value)
            ).distinct().all()
            
            for motor in motores:
                dropdown_motor.options.append(ft.dropdown.Option(motor[0]))
        
        page.update()
    
    dropdown_marca.on_change = atualizar_modelos
    dropdown_modelo.on_change = atualizar_anos
    dropdown_ano.on_change = atualizar_motores
    
    carregar_marcas()
    
    def cadastrar_nova_venda(e):
        veiculo_id = session.query(Veiculos.id).filter(Veiculos.fabricante == dropdown_marca.value,
                                                        Veiculos.modelo == dropdown_modelo.value,
                                                        Veiculos.ano == int(dropdown_ano.value),
                                                        Veiculos.motorizacao == dropdown_motor.value).scalar()

        if not all([data_venda.value, comprador.value, valor.value]):
            dlg_erros.content = ft.Text("Preencha todos os campos!", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        try:
            data_str = data_venda.value
            data_formatada = datetime.strptime(data_str, "%d-%m-%Y").date()
        except:
            dlg_erros.content = ft.Text("Data inválida. Use o formato DD-MM-YYYY", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        
        nova_venda = Vendas(
            data_venda=data_formatada,
            comprador=comprador.value,
            valor=valor.value)
        
        session.add(nova_venda)
        session.flush()#Força a geração do ID antes do commit(solução)

        venda_veiculo = VendaVeiculo(
            id_vendas= nova_venda.id,
            id_veiculo= veiculo_id
            )
        
        session.add(venda_veiculo)
        session.commit()
        dlg_sucesso.content = ft.Text("Venda cadastrada com sucesso!", color="green", size=20)
        page.open(dlg_sucesso)
        dlg_sucesso.open = True
        
    botao_cadastrar = criar_botao("Cadastrar", ft.Icons.ADD, cadastrar_nova_venda, ft.Colors.TEAL_700)
    
    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Nova venda", size=30, weight=ft.FontWeight.BOLD, color="white"),
                ft.Row([dropdown_marca], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([dropdown_modelo], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([dropdown_ano], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([dropdown_motor], alignment=ft.MainAxisAlignment.CENTER),
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
        margin=ft.margin.symmetric(vertical=150),
        padding=20
    )

def listar_vendas(page: ft.Page):

    vendas = session.query(Vendas).all()

    if not vendas:
        dlg_erros.content = ft.Text("Nenhuma venda cadastrada", color="red", size=20)
        page.open(dlg_erros)
        dlg_erros.open = True
        page.update()
        return ft.Container()
    
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
            ft.Text("  Vendas Cadastradas", 
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
    comprador = ft.TextField(label="Comprador", width=400, on_change=maiusculo)
    valor = ft.TextField(label="Valor da Venda", width=400, on_change=maiusculo)

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
            ft.Text("Alterar venda", size=30, weight=ft.FontWeight.BOLD, color="white"),
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
        margin=ft.margin.symmetric(vertical=150),
        padding=20
        )
