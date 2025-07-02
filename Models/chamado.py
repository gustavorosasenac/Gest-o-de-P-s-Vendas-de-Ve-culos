import flet as ft
from DB.Database import session
from DB.Tables.table_chamado import Chamado
from DB.Tables.table_vendas import VendaVeiculo

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

def cadastro_de_chamado(page: ft.Page):
        id_venda_veiculo = ft.TextField(label="ID da Venda", width=400)
        descricao = ft.TextField(label="Descrição do Chamado", width=400)

        def cadastrar_chamado(e):
            if not all([id_venda_veiculo.value, descricao.value]):
                dlg_erros.content = ft.Text("Preencha todos os campos!", color="red", size=20)
                page.open(dlg_erros)
                dlg_erros.open = True
                return
            if not id_venda_veiculo.value.isdigit():
                dlg_erros.content = ft.Text("ID deve ser um número inteiro", color="red", size=20)
                page.open(dlg_erros)
                dlg_erros.open = True
                return
            
            verificar_venda = session.query(VendaVeiculo).filter(VendaVeiculo.id == int(id_venda_veiculo.value)).first()
            
            if not verificar_venda:
                dlg_erros.content = ft.Text("Venda não encontrada", color="red", size=20)
                page.open(dlg_erros)
                dlg_erros.open = True
                return
            
            else:
                  novo_chamado = Chamado(
                    id_venda_veiculo=id_venda_veiculo.value,
                    descricao=descricao.value)
                  
                  session.add(novo_chamado)
                  session.commit()

                  dlg_sucesso.content = ft.Text("Chamado cadastrado com sucesso!", color="green", size=20)
                  page.open(dlg_sucesso)
                  dlg_sucesso.open = True

        botao_cadastrar = criar_botao("Cadastrar", ft.Icons.ADD, cadastrar_chamado, ft.Colors.TEAL_700)


        return ft.Container(
        content=ft.Column(
            [
                ft.Text("Novo Chamado", size=50, weight=ft.FontWeight.BOLD, color="white"),
                id_venda_veiculo,
                descricao,
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




