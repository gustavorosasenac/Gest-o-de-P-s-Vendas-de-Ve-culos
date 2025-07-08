import flet as ft
from DB.Database import session
from DB.Tables.table_item import Itens

#dlg é só o nome da variavel, ft.AlertDialog cria a caixa de aviso de erro ou sucesso.
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
def maiusculo(e):
        # Converte o texto para maiúsculas e atualiza
        e.control.value = e.control.value.upper()
        e.control.update()

#Inicia o cadastro de item
def cadastro_de_itens(page: ft.Page):
    # Campos do formulário
    nome = ft.TextField(label="Nome", width=400, on_change=maiusculo)
    preco  = ft.TextField(label="Preço", width=400, on_change=maiusculo)

    # Função para cadastrar ‘item’
    def cadastro_de_itens(e):
        if not all([nome.value, preco.value]):
            dlg_erros.content = ft.Text("Preencha todos os campos!", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        
        verificar_cadastro = session.query(Itens).filter(
            Itens.nome == nome.value,
            Itens.preco == preco.value,
        ).first()

        if verificar_cadastro:
            dlg_ja_cadastrado.content = ft.Text("Item já cadastrado", color="red", size=20)
            page.open(dlg_ja_cadastrado)
            dlg_ja_cadastrado.open = True
            return
        else:
            novo_item = Itens(
                nome = nome.value,
                preco = preco.value,
                )

            session.add(novo_item)
            session.commit()

            dlg_sucesso.content = ft.Text("Item cadastrado com sucesso!", color="green", size=20)
            page.open(dlg_sucesso)
            dlg_sucesso.open = True

    botao_cadastrar = criar_botao("Cadastrar", ft.Icons.ADD, cadastro_de_itens, ft.Colors.TEAL_700)

    # Retorna os controles do formulário
    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Novo item", size=30, weight=ft.FontWeight.BOLD, color="white"),
                nome,
                preco,
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


def listar_itens(page: ft.Page):
    itens = session.query(Itens).all()

    if not Itens:
        dlg_erros.content = ft.Text("Nenhum item cadastrado", color="red", size=20)
        page.open(dlg_erros)
        dlg_erros.open = True
        page.update()
        return
    # ft.ListView vai exibir em formato de lista

    lista_itens = ft.ListView(
        controls=[
            ft.Container(
                content=ft.Text(f"ID: {v.id} | Nome: {v.nome} | Preço: {v.preco} | ",
                                size=16,
                                color=ft.Colors.WHITE),
                padding=10,
                border=ft.border.all(1, ft.Colors.GREY_800),
                margin=ft.margin.only(bottom=5))
            for v in itens
        ],
        width=900,
        spacing=5,
        padding=10
    )

    return ft.Container(
        content=ft.Column([
            ft.Text("Itens Cadastrados",
                    size=40,
                    weight=ft.FontWeight.BOLD,
                    color="white",
                    text_align=ft.TextAlign.LEFT),  # Alinhamento do título à esquerda
            ft.Divider(height=20),
            lista_itens
        ],
            alignment=ft.MainAxisAlignment.START,  # Alinha no topo
            horizontal_alignment=ft.CrossAxisAlignment.START  # Alinha tudo à esquerda
        ),
        bgcolor=ft.Colors.with_opacity(0.90, ft.Colors.BLACK),
        border_radius=20,
        width=1000,
        padding=ft.padding.only(left=20, top=20, right=20, bottom=20),  # Padding igual em todos os lados
        margin=ft.margin.only(left=20),  # Margem reduzida à esquerda
        alignment=ft.alignment.top_left  # Alinha o container no topo esquerdo
    )


def alterar_itens(page: ft.Page):
    id_Itens = ft.TextField(label="ID do item", width=400)
    nome = ft.TextField(label="Nome do item", width=400, on_change=maiusculo)
    preco = ft.TextField(label="Preço", width=400, on_change=maiusculo)

    def buscar_itens(e):
        if not all([id_Itens, nome.value, preco.value]):
            dlg_erros.content = ft.Text("Preencha todos os campos!", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return

        if not id_Itens.value.isdigit():
            dlg_erros.content = ft.Text("ID deve ser um número inteiro", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return

        itens = session.query(Itens).filter(Itens.id == int(id_Itens.value)).first()

        if not itens:
            dlg_erros.content = ft.Text("Item não encontrado.", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        else:
            itens.nome = nome.value
            itens.preco = preco.value
            session.commit()

            dlg_sucesso.content = ft.Text("Item alterado com sucesso!", color="green", size=20)
            page.open(dlg_sucesso)
            dlg_sucesso.open = True

    botao_alterar = criar_botao("Alterar", ft.Icons.ADD, buscar_itens, ft.Colors.TEAL_700)

    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Alterar Item", size=30, weight=ft.FontWeight.BOLD, color="white"),
                id_Itens,
                nome,
                preco,
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
