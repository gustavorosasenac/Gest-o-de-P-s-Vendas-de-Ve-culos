import flet as ft
from DB.Database import session
from DB.Tables.table_diagnostico import Diagnostico
from DB.Tables.table_chamado import Chamado


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

def cadastro_de_diagnostico(page: ft.Page):
    id_chamado = ft.TextField(label="ID do Chamado", width=400)
    categoria = ft.TextField(label="Categoria", width=400, on_change=maiusculo)
    sintoma = ft.TextField(label="Sintoma", width=400, on_change=maiusculo)
    
    # Variável para armazenar a seleção de manutenção
    manutencao_selecionada = ft.Ref[bool]()
    
    # Funções para definir a seleção
    def selecionar_sim(e):
        manutencao_selecionada.current = True
        botao_sim.bgcolor = ft.Colors.GREEN
        botao_nao.bgcolor = ft.Colors.GREY
        page.update()
    
    def selecionar_nao(e):
        manutencao_selecionada.current = False
        botao_sim.bgcolor = ft.Colors.GREY
        botao_nao.bgcolor = ft.Colors.RED
        page.update()
    
    # Botões de seleção
    botao_sim = ft.ElevatedButton(
        "Sim",
        on_click=selecionar_sim,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            padding=20,
            bgcolor=ft.Colors.GREY,  # Começa cinza (não selecionado)
            color=ft.Colors.WHITE
        ),
        width=150
    )
    
    botao_nao = ft.ElevatedButton(
        "Não",
        on_click=selecionar_nao,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            padding=20,
            bgcolor=ft.Colors.GREY,  # Começa cinza (não selecionado)
            color=ft.Colors.WHITE
        ),
        width=150
    )
    
    # Container para os botões
    container_manutencao = ft.Container(
        content=ft.Column([
            ft.Text("Preciso de manutenção?", size=16),
            ft.Row([botao_sim, botao_nao], spacing=10)
        ], spacing=5),
        width=400
    )

    def cadastrar_diagnostico(e):
        if not all([id_chamado.value, categoria.value, sintoma.value]) or manutencao_selecionada.current is None:
            dlg_erros.content = ft.Text("Preencha todos os campos!", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        
        if not id_chamado.value.isdigit():
            dlg_erros.content = ft.Text("ID deve ser um número inteiro", color="red", size=20)
            page.open = (dlg_erros)
            dlg_erros.open = True
            return
        
        verificar_diagnostico = session.query(Diagnostico).filter(
            Diagnostico.id_chamado == int(id_chamado.value),
            Diagnostico.categoria == categoria.value).first()
        
        if verificar_diagnostico:
            dlg_ja_cadastrado.content = ft.Text("Diagnostico já cadastrado", color="red", size=20)
            page.open(dlg_ja_cadastrado)
            dlg_ja_cadastrado.open = True
            return
        
        verificar_chamado = session.query(Chamado).filter(Chamado.id == int(id_chamado.value)).first()
        
        if not verificar_chamado:
            dlg_erros.content = ft.Text("Chamado não encontrado", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        
        else:
            novo_diagnostico = Diagnostico(
            id_chamado=id_chamado.value,
            categoria=categoria.value,
            sintoma=sintoma.value,
            manutencao=manutencao_selecionada.current)
            
            session.add(novo_diagnostico)
            session.commit()

        dlg_sucesso.content = ft.Text("Diagnostico cadastrado com sucesso!", color="green", size=20)
        page.open(dlg_sucesso)
        dlg_sucesso.open = True
        return

    botao_cadastrar = criar_botao("Cadastrar", ft.Icons.ADD, cadastrar_diagnostico, ft.Colors.TEAL_700)

    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Novo Diagnostico", size=30, weight=ft.FontWeight.BOLD, color="white"),
                id_chamado,
                categoria,
                sintoma,
                container_manutencao,  # Substitui o TextField pelo container com os botões
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

def listar_diagnostico(page: ft.Page):
    diagnostico = session.query(Diagnostico).all()
    
    if not diagnostico:
        dlg_erros.content = ft.Text("Nenhum diagnostico encontrado", color="red", size=20)
        page.open(dlg_erros)
        dlg_erros.open = True
        return
    
    lista_diagnostico = ft.ListView(
        controls=[
            ft.Container(
                content=ft.Text(f"ID do Chamado: {d.id_chamado}\n"
                              f"Categoria: {d.categoria}\n"
                              f"Sintoma: {d.sintoma}\n"
                              f"Manutenção: {'Sim' if d.manutencao else 'Não'}",
                              size=16,
                              color=ft.Colors.WHITE),
                padding=10,
                border=ft.border.all(1, ft.Colors.GREY_800),
                margin=ft.margin.only(bottom=5))
            for d in diagnostico
        ],
        width=900,
        height=700,
        spacing=5,
        padding=10,
        auto_scroll=False)
    
    return ft.Container(
        content=ft.Column([
            ft.Text("Diagnosticos Cadastrados", 
                   size=40, 
                   weight=ft.FontWeight.BOLD, 
                   color="white",
                   text_align=ft.TextAlign.LEFT),
            ft.Divider(height=20),
            lista_diagnostico
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.START,
        expand=True
        ),
        bgcolor=ft.Colors.with_opacity(0.90, ft.Colors.BLACK),
        border_radius=20,
        width=1000,
        height=800,
        padding=ft.padding.all(20),
        margin=ft.margin.only(left=20),
        alignment=ft.alignment.top_left
    )

def alterar_diagnostico(page: ft.Page):
    id_diagnostico = ft.TextField(label="ID do Diagnostico", width=400)
    id_chamado = ft.TextField(label="ID do Chamado", width=400)
    categoria = ft.TextField(label="Categoria", width=400, on_change=maiusculo)
    sintoma = ft.TextField(label="Sintoma", width=400, on_change=maiusculo)
    
    # Variável para armazenar a seleção de manutenção
    manutencao_selecionada = ft.Ref[bool]()
    
    # Funções para definir a seleção
    def selecionar_sim(e):
        manutencao_selecionada.current = True
        botao_sim.bgcolor = ft.Colors.GREEN
        botao_nao.bgcolor = ft.Colors.GREY
        page.update()
    
    def selecionar_nao(e):
        manutencao_selecionada.current = False
        botao_sim.bgcolor = ft.Colors.GREY
        botao_nao.bgcolor = ft.Colors.RED
        page.update()
    
    # Botões de seleção
    botao_sim = ft.ElevatedButton(
        "Sim",
        on_click=selecionar_sim,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            padding=20,
            bgcolor=ft.Colors.GREY,  # Começa cinza (não selecionado)
            color=ft.Colors.WHITE
        ),
        width=150)
    
    botao_nao = ft.ElevatedButton(
        "Não",
        on_click=selecionar_nao,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            padding=20,
            bgcolor=ft.Colors.GREY,  # Começa cinza (não selecionado)
            color=ft.Colors.WHITE
        ),
        width=150)
    
    # Container para os botões
    container_manutencao = ft.Container(
        content=ft.Column([
            ft.Text("Preciso de manutenção?", size=16),
            ft.Row([botao_sim, botao_nao], spacing=10)
        ], spacing=5),
        width=400)

    def alterar_diagnostico(e):
        if not all([id_diagnostico.value, id_chamado.value, categoria.value, sintoma.value]) or manutencao_selecionada.current is None:
            dlg_erros.content = ft.Text("Preencha todos os campos!", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        
        if not id_diagnostico.value.isdigit():
            dlg_erros.content = ft.Text("ID deve ser um número inteiro", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        
        if not id_chamado.value.isdigit():
            dlg_erros.content = ft.Text("ID deve ser um número inteiro", color="red", size=20)
            page.open = (dlg_erros)
            dlg_erros.open = True
            return
        
        diagnostico = session.query(Diagnostico).filter(Diagnostico.id == int(id_diagnostico.value)).first()
        
        if not diagnostico:
            dlg_erros.content = ft.Text("Diagostico não encontrado", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        
        verificar_chamado = session.query(Chamado).filter(Chamado.id == int(id_chamado.value)).first()
        
        if not verificar_chamado:
            dlg_erros.content = ft.Text("Chamado não encontrado", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        else:
            diagnostico.id_chamado = id_chamado.value
            diagnostico.categoria = categoria.value
            diagnostico.sintoma = sintoma.value
            diagnostico.manutencao = manutencao_selecionada.current
            session.commit()


        dlg_sucesso.content = ft.Text("Diagnostico alterado com sucesso!", color="green", size=20)
        page.open(dlg_sucesso)
        dlg_sucesso.open = True
        return

    botao_alterar = criar_botao("Alterar", ft.Icons.ADD, alterar_diagnostico, ft.Colors.TEAL_700)

    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Alterar Diagnostico", size=30, weight=ft.FontWeight.BOLD, color="white"),
                id_diagnostico,
                id_chamado,
                categoria,
                sintoma,
                container_manutencao,  # Substitui o TextField pelo container com os botões
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
