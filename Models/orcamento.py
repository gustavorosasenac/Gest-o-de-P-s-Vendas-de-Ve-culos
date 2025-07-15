import flet as ft
from DB.Database import session
from DB.Tables.table_orcamento import Orcamento
from DB.Tables.table_vendas import VendaVeiculo
from DB.Tables.table_chamado import Chamado
from DB.Tables.table_item import Itens
from DB.Tables.table_diagnostico import Diagnostico
from sqlalchemy import select
from sqlalchemy.orm import aliased



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
        
        verificar_diagnostico = session.query(Diagnostico).filter(Diagnostico.id == int(id_diagnostico.value)).first()
        
        if not verificar_diagnostico:
            dlg_erros.content = ft.Text("Diagnostico não encontrado", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        
        verificar_item = session.query(Itens).filter(Itens.id == int(id_item.value)).first()

        if not verificar_item:
            dlg_erros.content = ft.Text("Item não encontrado", color="red", size=20)
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
            ft.Text("Novo Orçamento", size=30, weight=ft.FontWeight.BOLD, color="white"),
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
        page.update()
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
    id_orcamento = ft.TextField(label="ID do Orçamento", width=400)
    id_diagnostico = ft.TextField(label="ID do Diagnóstico", width=400)
    id_item  = ft.TextField(label="ID do Item", width=400)
    quantidade = ft.TextField(label="Quantidade do Item", width=400)
    id_venda_veiculo = ft.TextField(label="ID da Venda", width=400)


    def buscar_orcamentos(e):
        if not all([id_orcamento, id_diagnostico, id_item, quantidade, id_venda_veiculo]):
            dlg_erros.content = ft.Text("Preencha todos os campos!", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        
        if not id_orcamento.value.isdigit():
            dlg_erros.content = ft.Text("ID deve ser um número inteiro", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        
        orcamento = session.query(Orcamento).filter(Orcamento.id == int(id_orcamento.value)).first()
        
        if not orcamento:
            dlg_erros.content = ft.Text("Orçamento não encontrado.", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        else:
            orcamento.id_diagnostico = id_diagnostico.value
            orcamento.id_item = id_item.value
            orcamento.quantidade_item = quantidade.value
            orcamento.id_venda_veiculo = id_venda_veiculo.value
            session.commit()

            dlg_sucesso.content = ft.Text("Orçamento alterado com sucesso!", color="green", size=20)
            page.open(dlg_sucesso)
            dlg_sucesso.open = True
        
    botao_alterar = criar_botao("Alterar", ft.Icons.ADD, buscar_orcamentos, ft.Colors.TEAL_700)

    return ft.Container(
        content =ft.Column(
            [
            ft.Text("Alterar Orçamento", size=30, weight=ft.FontWeight.BOLD, color="white"),
            id_orcamento,
            id_diagnostico,
            id_item,
            quantidade,
            id_venda_veiculo,
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

def listar_orcamento_por_venda(page: ft.Page, session):
    
    # Componentes da UI
    id_venda = ft.TextField(label="Digite o ID da Venda", width=300, border_color=ft.Colors.AMBER)

    lista_orcamento = ft.ListView(
        expand=True,
        spacing=5,
        padding=10)

    def buscar_orcamentos(e):
        if not id_venda.value:
            dlg_erros.content = ft.Text("Digite um ID", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        if not id_venda.value.isdigit():
            dlg_erros.content = ft.Text("ID deve ser um número inteiro", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        
        orcamentos = session.query(Orcamento).filter(Orcamento.id_venda_veiculo == int(id_venda.value)).all()
        
        lista_orcamento.controls.clear()
        
        if not orcamentos:
            lista_orcamento.controls.append(
                ft.Container(
                    content=ft.Text(f"Nenhum orçamento encontrado para venda ID {id_venda}", size=16),
                    padding=15,
                    border=ft.border.all(1, ft.Colors.RED_400)
                )
            )
        else:
            # Agrupa os dados
            dados_agrupados = {
                'id_venda': id_venda.value,
                'id_diagnostico': orcamentos[0].id_diagnostico,
                'itens': [],
                'custo_total': 0.0
            }
            
            for o in orcamentos:
                dados_agrupados['itens'].append({
                    'id_item': o.id_item,
                    'quantidade': o.quantidade_item,
                    'custo': o.custo_total
                })
                dados_agrupados['custo_total'] += o.custo_total
            
            # Cabeçalho
            lista_orcamento.controls.append(
                ft.Container(
                    content=ft.Column([
                        ft.Text(f"Venda Veículo: #{dados_agrupados['id_venda']}", 
                                size=20, 
                                weight=ft.FontWeight.BOLD),
                        ft.Text(f"Diagnóstico: #{dados_agrupados['id_diagnostico']}", 
                                size=16)
                    ]),
                    padding=15,
                    border=ft.border.all(1, ft.Colors.AMBER)
                )
            )
            
            # Itens
            for item in dados_agrupados['itens']:
                lista_orcamento.controls.append(
                    ft.Container(
                        content=ft.Column([
                            ft.Text(f"Item: #{item['id_item']}", size=16),
                            ft.Text(f"Quantidade: {item['quantidade']}", size=14),
                            ft.Text(f"R$ {item['custo']:.2f}", 
                                    size=14, 
                                    color=ft.Colors.GREEN_300)
                        ]),
                        padding=15,
                        margin=ft.margin.only(left=20),
                        border=ft.border.all(1, ft.Colors.GREY_700)
                    )
                )
            
            # Total
            lista_orcamento.controls.append(
                ft.Container(
                    content=ft.Text(
                        f"TOTAL: R$ {dados_agrupados['custo_total']:.2f}",
                        size=18,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.AMBER
                    ),
                    padding=15,
                    border=ft.border.all(2, ft.Colors.AMBER),
                    margin=ft.margin.only(top=10)
                )
            )
        
        page.update()

    # Layout principal
    return ft.Container(
        content=ft.Column([
            ft.Row([
                ft.Icon(ft.Icons.RECEIPT_LONG, color=ft.Colors.AMBER),
                ft.Text("Orçamentos por Venda", 
                        size=24, 
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.WHITE)
            ]),
            ft.Divider(height=20),
            ft.Row([
                id_venda,
                ft.ElevatedButton(
                    "Buscar",
                    icon=ft.Icons.SEARCH,
                    on_click=buscar_orcamentos,
                    bgcolor=ft.Colors.AMBER,
                    color=ft.Colors.BLACK
                )
            ]),
            ft.Divider(height=20),
            lista_orcamento
        ],
        scroll=ft.ScrollMode.AUTO,
        expand=True
        ),
        bgcolor=ft.Colors.with_opacity(0.95, ft.Colors.BLACK),
        border_radius=15,
        padding=20,
        width=900,
        margin=ft.margin.symmetric(horizontal=20),
        alignment=ft.alignment.top_left
    )

def relatorio_orcamento(page: ft.Page):
    from DB.Tables.table_veiculos import Veiculos

    # Container que receberá o resultado
    container_resultado = ft.Container(visible=False)

    dropdown_marca = ft.Dropdown(label="Selecione a marca", width=400)
    dropdown_modelo = ft.Dropdown(label="Selecione o modelo", width=400, disabled=True)

    def carregar_marcas():
        marcas = session.query(Veiculos.fabricante).distinct().all()
        for marca in marcas:
            dropdown_marca.options.append(ft.dropdown.Option(marca[0]))
        page.update()

    def atualizar_modelos(e):
        dropdown_modelo.disabled = False
        dropdown_modelo.options = []
        dropdown_modelo.value = None

        if dropdown_marca.value:
            modelos = session.query(Veiculos.modelo).filter(
                Veiculos.fabricante == dropdown_marca.value
            ).distinct().all()

            for modelo in modelos:
                dropdown_modelo.options.append(ft.dropdown.Option(modelo[0]))

        page.update()

    dropdown_marca.on_change = atualizar_modelos
    carregar_marcas()

    def bucar_orcamento(e):
        resultados = (
            session.query(Orcamento, Veiculos, Diagnostico, Itens)
            .select_from(Orcamento)
            .join(VendaVeiculo, Orcamento.id_venda_veiculo == VendaVeiculo.id)
            .join(Veiculos, VendaVeiculo.id_veiculo == Veiculos.id)
            .join(Diagnostico, Orcamento.id_diagnostico == Diagnostico.id)
            .join(Itens, Orcamento.id_item == Itens.id)
            .filter(Veiculos.fabricante == dropdown_marca.value, Veiculos.modelo == dropdown_modelo.value)
            .order_by(Orcamento.custo_total.desc())
            .all()
        )

        if not resultados:
            dlg_erros.content = ft.Text("Nenhum orçamento encontrado", color="red", size=20)
            dlg_erros.open = True
            page.dialog = dlg_erros
            page.update()
            return

        listar_orcamento = ft.ListView(
            controls=[
                ft.Container(
                    content=ft.Text(
                        f"Categoria: {diagnostico.categoria}\n"
                        f"Item: {item.nome}\n"
                        f"Quantidade do Item: {orcamento.quantidade_item}\n"
                        f"Custo Total: {orcamento.custo_total}\n"
                        f"ID da Venda: {orcamento.id_venda_veiculo}\n"
                        f"Modelo do Veículo: {veiculos.modelo}\n"
                        f"Ano do veiculo: {veiculos.ano}\n"
                        f"Motor do veiculo: {veiculos.motorizacao}",
                        size=16,
                        color=ft.Colors.WHITE
                    ),
                    padding=10,
                    border=ft.border.all(1, ft.Colors.GREY_800),
                    margin=ft.margin.only(bottom=5)
                )
                for orcamento, veiculos, diagnostico, item in resultados
            ],
            width=900,
            spacing=5,
            padding=10,
            expand=True
        
        )

        container_resultado.content = ft.Container(
            content=ft.Column([
                ft.Text("Orçamentos do Veiculo Cadastrados", size=30, weight=ft.FontWeight.BOLD, color="white"),
                ft.Divider(height=20),
                ft.Container(
                    content=listar_orcamento,
                    height=650,)
            ],
            expand=True),
            bgcolor=ft.Colors.with_opacity(0.95, ft.Colors.BLACK),
            border_radius=20,
            padding=20,
            width=900,

            expand=True
        )
        container_resultado.visible = True
        page.update()

    # Botão que dispara a busca
    botao_buscar = criar_botao("Buscar", ft.Icons.SEARCH, bucar_orcamento, ft.Colors.TEAL_700)

    # Formulário de filtros (base do Stack)
    container_filtro = ft.Container(
        content=ft.Column(
            [
                ft.Text("Relatório de Orçamentos", size=30, weight=ft.FontWeight.BOLD, color="white"),
                ft.Row([dropdown_marca], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([dropdown_modelo], alignment=ft.MainAxisAlignment.CENTER),
                ft.Divider(height=40, color=ft.Colors.TRANSPARENT),
                botao_buscar,
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

    # Camada final com sobreposição
    return ft.Stack([
        container_filtro,
        ft.Container(
            content=container_resultado,
            alignment=ft.alignment.center,
            bgcolor=ft.Colors.with_opacity(1, ft.Colors.BLACK)
              # Pode ajustar se quiser mover mais pra cima
            )
    ])


        
