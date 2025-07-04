import flet as ft
from DB.Database import session
from sqlalchemy import text
from DB.Tables.table_orcamento import Orcamento
from DB.Tables.table_vendas import VendaVeiculo
from DB.Tables.table_chamado import Chamado
from DB.Tables.table_item import Itens
from DB.Tables.table_diagnostico import Diagnostico



dlg_erros = ft.AlertDialog(
    title=ft.Text("Erro!", color="red", text_align=ft.TextAlign.CENTER),
    content=ft.Text("", color="red", size=20),
    alignment=ft.alignment.center,
    title_padding = ft.padding.all(25))

dlg_sucesso = ft.AlertDialog(
    title=ft.Text("Sucesso!", color="green", text_align=ft.TextAlign.CENTER),
    content=ft.Text("", color="green", size=20),
    alignment=ft.alignment.center,
    title_padding = ft.padding.all(25))

dlg_ja_cadastrado = ft.AlertDialog(
    title=ft.Text("Erro!", color="red"),
    content=ft.Text("", color="red", size=20),
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


def cadastro_de_orcamento(page: ft.Page):
    id_diagnostico = ft.TextField(label="ID do Diagnostico", width=400)
    id_item = ft.TextField(label="ID do Item", width=400)
    quantidade_item = ft.TextField(label="Quantidade do Item", width=400)
    custo_total = 0.0
    id_venda_veiculo = ft.TextField(label="ID da venda", width=400)

    def cadastrar_orcamento(e):
        if not all([id_diagnostico.value, id_item.value, quantidade_item.value, id_venda_veiculo.value]):
            dlg_erros.content = ft.Text("Preencha todos os campos!", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        if not id_venda_veiculo.value.isdigit():
            dlg_erros.content = ft.Text("ID deve ser um número inteiro", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        if not quantidade_item.value.isdigit():
            dlg_erros.content = ft.Text("A quantidade de itens deve ser um número inteiro", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        
        verificar_venda = session.query(VendaVeiculo).filter(VendaVeiculo.id == int(id_venda_veiculo.value)).first()
        
        if not verificar_venda:
            dlg_erros.content = ft.Text("Venda não encontrada", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        
        verificar_orcamento = session.query(Orcamento).filter(
            Orcamento.id_venda_veiculo == int(id_venda_veiculo.value),
            Orcamento.id_diagnostico == int(id_diagnostico.value),
            Orcamento.id_item == int(id_item.value),
            Orcamento.quantidade_item == int(quantidade_item.value)).first()
        
        item = session.query(Itens).filter(Itens.id == int(id_item.value)).first()
        custo_total = item.preco * int(quantidade_item.value)
        
        if verificar_orcamento:
                dlg_ja_cadastrado.content = ft.Text("Orçamento já cadastrado", color="red", size=20)
                page.open(dlg_ja_cadastrado)
                dlg_ja_cadastrado.open = True
                return
        else:
                novo_orcamento = Orcamento(
                id_diagnostico=id_diagnostico.value,
                id_item=id_item.value,
                quantidade_item=quantidade_item.value,
                custo_total=custo_total,
                id_venda_veiculo=id_venda_veiculo.value
                )
                
                session.add(novo_orcamento)
                session.commit()

                dlg_sucesso.content = ft.Text("Orçamento cadastrado com sucesso!", color="green", size=20)
                page.open(dlg_sucesso)
                dlg_sucesso.open = True

    botao_cadastrar = criar_botao("Cadastrar", ft.Icons.ADD, cadastrar_orcamento, ft.Colors.TEAL_700)

    return ft.Container(
    content=ft.Column(
        [
            ft.Text("Novo Orçamento", size=50, weight=ft.FontWeight.BOLD, color="white"),
            id_diagnostico,
            id_item,
            quantidade_item,
            id_venda_veiculo,
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

def listar_orcamento(page: ft.Page):
    orcamento = session.query(Orcamento).all()
    
    if not orcamento:
        dlg_erros.content = ft.Text("Nenhum Orçamento encontrado", color="red", size=20)
        page.open(dlg_erros)
        dlg_erros.open = True
        return
    
    lista_orcamento = ft.ListView(
    controls=[
        ft.Container(
            content=ft.Text(f"ID do Diagnostico: {o.id_diagnostico}\nID do Item: {o.id_item} \nQuantidade do Item: {o.quantidade_item}\nCusto Total: {o.custo_total}\nID da Venda: {o.id_venda_veiculo}\n",
                          size=16,
                          color=ft.Colors.WHITE),
            padding=10,
            border=ft.border.all(1, ft.Colors.GREY_800),
            margin=ft.margin.only(bottom=5))
        for o in orcamento
    ],
    width=900,
    spacing=5,
    padding=10
)
    
    return ft.Container(
        content=ft.Column([
            ft.Text("  Orçamentos Cadastrados", 
                   size=40, 
                   weight=ft.FontWeight.BOLD, 
                   color="white",
                   text_align=ft.TextAlign.LEFT),  # Alinhamento do título à esquerda
            ft.Divider(height=20),
            lista_orcamento
        ],
        alignment=ft.MainAxisAlignment.START,  # Alinha no topo
        horizontal_alignment=ft.CrossAxisAlignment.START  # Alinha tudo à esquerda
        ),
        bgcolor=ft.Colors.with_opacity(0.90, ft.Colors.BLACK),
        border_radius=20,
        width=1000,
        padding=ft.padding.only(left=20, top=20, right=20, bottom=20),  # Padding igual em todos os lados
        margin=ft.margin.only(left = 20),  # Margem reduzida à esquerda
        alignment=ft.alignment.top_left  # Alinha o container no topo esquerdo
    )

def alterar_orcamento(page: ft.Page):
    id_chamado = ft.TextField(label="ID do Chamado", width=400)
    descricao = ft.TextField(label="Descição", width=400)

    def buscar_chamado(e):
        if not all([id_chamado, descricao]):
            dlg_erros.content = ft.Text("Preencha todos os campos!", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        
        if not id_chamado.value.isdigit():
            dlg_erros.content = ft.Text("ID deve ser um número inteiro", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        
        chamado = session.query(Chamado).filter(Chamado.id == int(id_chamado.value)).first()
        
        if not chamado:
            dlg_erros.content = ft.Text("Chamado não encontrado.", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        else:
            chamado.id_venda_veiculo = id_chamado.value
            chamado.descricao = descricao.value
            session.commit()

            dlg_sucesso.content = ft.Text("Chamado alterado com sucesso!", color="green", size=20)
            page.open(dlg_sucesso)
            dlg_sucesso.open = True
        
    botao_alterar = criar_botao("Alterar", ft.Icons.ADD, buscar_chamado, ft.Colors.TEAL_700)

    return ft.Container(
        content =ft.Column(
            [
            ft.Text("Alterar Veículo", size=50, weight=ft.FontWeight.BOLD, color="white"),
            id_chamado,
            descricao,
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

def excluir_orcamento(page: ft.Page):
    id_chamado = ft.TextField(label="ID do Chamado", width=400)
    
    def excluir_chamado(e):
        if not id_chamado.value.isdigit():
            dlg_erros.content = ft.Text("ID deve ser um número inteiro", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        
        veiculo = session.query(Chamado).filter(Chamado.id == int(id_chamado.value)).first()
        
        if veiculo:
            session.delete(veiculo)
            session.commit()
            dlg_sucesso.content = ft.Text("Chamado excluído com sucesso!", color="green", size=20)
            page.open(dlg_sucesso)
            dlg_sucesso.open = True
        else:
            dlg_erros.content = ft.Text("Chamado não encontrado.", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
        
    botao_excluir= criar_botao("Excluir", ft.Icons.ADD, excluir_chamado, ft.Colors.RED_700)

    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Excluir Chamado", size=30, weight=ft.FontWeight.BOLD, color="white"),
                ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                id_chamado,
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