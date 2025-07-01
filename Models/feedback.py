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
    comentario = ft.TextField(label="Comentário", width=400)

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
                 id_venda_veiculo=id_venda.value,
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
                ft.Text("Nova venda", size=30, weight=ft.FontWeight.BOLD, color="white"),
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
        margin=ft.margin.symmetric(vertical=100),
        padding=20
    )


        


