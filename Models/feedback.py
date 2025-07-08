import flet as ft
from DB.Database import session
from DB.Tables.table_feeback import Feedback
from DB.Tables.table_vendas import Vendas

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

def maiusculo(e):
        # Converte o texto para maiúsculas e atualiza
        e.control.value = e.control.value.upper()
        e.control.update()

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

def cadastro_de_feedback(page: ft.Page):
    id_venda = ft.TextField(label="ID da Venda", width=400)
    comentario = ft.TextField(label="Comentário", width=400, on_change=maiusculo)

    def cadastrar_feedback(e):
        if not all([id_venda.value, comentario.value]):
            dlg_erros.content = ft.Text("Preencha todos os campos!", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        if not id_venda.value.isdigit():
            dlg_erros.content = ft.Text("ID da venda deve ser um número inteiro", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        
        verificar_venda = session.query(Vendas).filter(Vendas.id == id_venda.value).first()

        if not verificar_venda:
            dlg_erros.content = ft.Text("Venda não encontrada", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        else:
             novo_feedback = Feedback(
                 id_venda_veiculos=id_venda.value,
                 comentario=comentario.value)
             session.add(novo_feedback)
             session.commit()
             dlg_sucesso.content = ft.Text("Feedback cadastrado com sucesso!", color="green", size=20)
             page.open(dlg_sucesso)
             dlg_sucesso.open = True
    
    botao_cadastrar = criar_botao("Cadastrar", ft.Icons.ADD, cadastrar_feedback, ft.Colors.TEAL_700)

    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Novo Feedback", size=30, weight=ft.FontWeight.BOLD, color="white"),
                id_venda,
                comentario,
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
        margin=ft.margin.symmetric(vertical=200),
        padding=20
    )

def listar_feedback(page: ft.Page):

    feedbacks = session.query(Feedback).all()

    if not feedbacks:
        dlg_erros.content = ft.Text("Nenhum feedback cadastrado", color="red", size=20)
        page.open(dlg_erros)
        dlg_erros.open = True
        return

    lista_feedback = ft.ListView(
    controls=[
        ft.Container(
            content=ft.Text(f"ID: {v.id} | Venda ID: {v.id_venda_veiculos} | Comentário: {v.comentario}",
                          size=16,
                          color=ft.Colors.WHITE),
            padding=10,
            border=ft.border.all(1, ft.Colors.GREY_800),
            margin=ft.margin.only(bottom=5))
        for v in feedbacks
    ],
    width=900,
    spacing=5,
    padding=10
)
    
    return ft.Container(
        content=ft.Column([
            ft.Text("  Feedbacks Cadastrados", 
                   size=40, 
                   weight=ft.FontWeight.BOLD, 
                   color="white",
                   text_align=ft.TextAlign.LEFT),  # Alinhamento do título à esquerda
            ft.Divider(height=20),
            lista_feedback
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

def alterar_feedback(page: ft.Page):
    id_feedback = ft.TextField(label="ID do Feedback", width=400)
    id_venda = ft.TextField(label="ID da Venda", width=400)
    comentario = ft.TextField(label="Comentário", width=400, on_change=maiusculo)

    def alterar_feedback(e):
        if not all([id_feedback.value, id_venda.value, comentario.value]):
            dlg_erros.content = ft.Text("Preencha todos os campos!", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        
        if not id_feedback.value.isdigit() or not id_venda.value.isdigit():
            dlg_erros.content = ft.Text("IDs devem ser números inteiros", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        
        feedback = session.query(Feedback).filter(Feedback.id == id_feedback.value).first()
        
        if not feedback:
            dlg_erros.content = ft.Text("Feedback não encontrado", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        
        venda = session.query(Vendas).filter(Vendas.id == id_venda.value).first()
        if not venda:
            dlg_erros.content = ft.Text("Venda não encontrada", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        
        feedback.id_venda_veiculos = id_venda.value
        feedback.comentario = comentario.value
        session.commit()
        
        dlg_sucesso.content = ft.Text("Feedback alterado com sucesso!", color="green", size=20)
        page.open(dlg_sucesso)
        dlg_sucesso.open = True

    botao_alterar = criar_botao("Alterar", ft.Icons.EDIT, alterar_feedback, ft.Colors.TEAL_700)
    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Alterar Feedback", size=30, weight=ft.FontWeight.BOLD, color="white"),
                id_feedback,
                id_venda,
                comentario,
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


        


