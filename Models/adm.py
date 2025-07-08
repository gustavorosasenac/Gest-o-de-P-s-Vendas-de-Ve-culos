import flet as ft
from DB.Database import session
from DB.Tables.table_chamado import Chamado
from DB.Tables.table_diagnostico import Diagnostico
from DB.Tables.table_item import Itens
from DB.Tables.table_orcamento import Orcamento
from DB.Tables.table_vendas import Vendas
from DB.Tables.table_veiculos import Veiculos
from DB.Tables.table_feeback import Feedback


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

def excluir_chamado(page: ft.Page):
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

def excluir_diagnostico(page: ft.Page):
    id_diagnostico = ft.TextField(label="ID do Diagnostico", width=400)

    def excluir_diagnostico(e):
        if not id_diagnostico.value.isdigit():
            dlg_erros.content = ft.Text("ID deve ser um número inteiro", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        
        diagnostico = session.query(Diagnostico).filter(Diagnostico.id == int(id_diagnostico.value)).first()
        
        if diagnostico:
            session.delete(diagnostico)
            session.commit()
            dlg_sucesso.content = ft.Text("Diagnostico excluído com sucesso!", color="green", size=20)
            page.open(dlg_sucesso)
            dlg_sucesso.open = True
        else:
            dlg_erros.content = ft.Text("Diagnostico não encontrado.", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
        
    botao_excluir= criar_botao("Excluir", ft.Icons.ADD, excluir_diagnostico, ft.Colors.RED_700)

    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Excluir Diagnostico", size=30, weight=ft.FontWeight.BOLD, color="white"),
                ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                id_diagnostico,
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

def excluir_feedback(page: ft.Page):
    id_feedback = ft.TextField(label="ID do Feedback", width=400)

    def excluir_feedback(e):
        if not id_feedback.value:
            dlg_erros.content = ft.Text("Preencha o ID do feedback!", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        
        if not id_feedback.value.isdigit():
            dlg_erros.content = ft.Text("ID deve ser um número inteiro", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        
        feedback = session.query(Feedback).filter(Feedback.id == id_feedback.value).first()
        
        if not feedback:
            dlg_erros.content = ft.Text("Feedback não encontrado", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        
        session.delete(feedback)
        session.commit()
        
        dlg_sucesso.content = ft.Text("Feedback excluído com sucesso!", color="green", size=20)
        page.open(dlg_sucesso)
        dlg_sucesso.open = True

    botao_excluir = criar_botao("Excluir", ft.Icons.DELETE, excluir_feedback, ft.Colors.RED_700)

    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Excluir Feedback", size=30, weight=ft.FontWeight.BOLD, color="white"),
                ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                id_feedback,
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

def excluir_item(page: ft.Page):
    id_itens = ft.TextField(label="ID do Item", width=400)

    def excluir_itens(e):
        if not id_itens.value.isdigit():
            dlg_erros.content = ft.Text("ID deve ser um número inteiro", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return

        itens = session.query(Itens).filter(Itens.id == int(id_itens.value)).first()

        if itens:
            session.delete(itens)
            session.commit()
            dlg_sucesso.content = ft.Text("Item excluído com sucesso!", color="green", size=20)
            page.open(dlg_sucesso)
            dlg_sucesso.open = True
        else:
            dlg_erros.content = ft.Text("Item não encontrado.", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True

    botao_excluir = criar_botao("Excluir", ft.Icons.ADD, excluir_itens, ft.Colors.RED_700)

    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Excluir Item", size=30, weight=ft.FontWeight.BOLD, color="white"),
                ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                id_itens,
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

def excluir_orcamento(page: ft.Page):
    id_orcamento = ft.TextField(label="ID do Orçamento", width=400)

    def excluir_orcamentos(e):
        if not id_orcamento.value.isdigit():
            dlg_erros.content = ft.Text("ID deve ser um número inteiro", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        
        orcamento = session.query(Orcamento).filter(Orcamento.id == int(id_orcamento.value)).first()
        
        if orcamento:
            session.delete(orcamento)
            session.commit()
            dlg_sucesso.content = ft.Text("Orçamento excluído com sucesso!", color="green", size=20)
            page.open(dlg_sucesso)
            dlg_sucesso.open = True
        else:
            dlg_erros.content = ft.Text("Orçamento não encontrado.", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
        
    botao_excluir= criar_botao("Excluir", ft.Icons.ADD, excluir_orcamentos, ft.Colors.RED_700)

    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Excluir Orçamento", size=30, weight=ft.FontWeight.BOLD, color="white"),
                ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                id_orcamento,
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

def excluir_veiculo(page: ft.Page):
    id_veiculo = ft.TextField(label="ID do Veículo", width=400)

    def excluir_veiculo(e):
        if not id_veiculo.value.isdigit():
            dlg_erros.content = ft.Text("ID deve ser um número inteiro", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        
        veiculo = session.query(Veiculos).filter(Veiculos.id == int(id_veiculo.value)).first()
        
        if veiculo:
            session.delete(veiculo)
            session.commit()
            dlg_sucesso.content = ft.Text("Veículo excluído com sucesso!", color="green", size=20)
            page.open(dlg_sucesso)
            dlg_sucesso.open = True
        else:
            dlg_erros.content = ft.Text("Veículo não encontrado.", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
        
    botao_excluir= criar_botao("Excluir", ft.Icons.ADD, excluir_veiculo, ft.Colors.RED_700)

    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Excluir Veiculo", size=30, weight=ft.FontWeight.BOLD, color="white"),
                ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                id_veiculo,
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
                ft.Text("Excluir Venda", size=30, weight=ft.FontWeight.BOLD, color="white"),
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


























































































































