import flet as ft
from DB.Database import session
from DB.Tables.table_veiculos import Veiculos

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

#Inicia o cadastro de veiculos
def cadastros_de_veiculo(page: ft.Page):
    # Campos do formulário
    fabricante = ft.TextField(label="Fabricante", width=400)
    modelo = ft.TextField(label="Modelo", width=400)    
    ano = ft.TextField(label="Ano", width=400)
    motorizacao = ft.TextField(label="Motorização", width=400)
    cambio = ft.TextField(label="Câmbio", width=400)

    # Função para cadastrar veículo
    def cadastrar_veiculo(e):
        if not all([fabricante.value, modelo.value, ano.value, motorizacao.value, cambio.value]):
            dlg_erros.content = ft.Text("Preencha todos os campos!", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        if not ano.value.isdigit():
            dlg_erros.content = ft.Text("Ano deve ser um número inteiro", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        
        verificar_cadastro = session.query(Veiculos).filter(
            Veiculos.fabricante == fabricante.value,
            Veiculos.modelo == modelo.value,
            Veiculos.ano == int(ano.value),
            Veiculos.motorizacao == motorizacao.value,
        ).first()
            
        if verificar_cadastro:
            dlg_ja_cadastrado.content = ft.Text("Veículo já cadastrado", color="red", size=20)
            page.open(dlg_ja_cadastrado)
            dlg_ja_cadastrado.open = True
            return
        else:
            novo_veiculo = Veiculos(
                fabricante=fabricante.value,
                modelo=modelo.value,
                ano=int(ano.value),
                motorizacao=motorizacao.value,
                cambio=cambio.value)
                
            session.add(novo_veiculo)
            session.commit()

            dlg_sucesso.content = ft.Text("Veículo cadastrado com sucesso!", color="green", size=20)
            page.open(dlg_sucesso)
            dlg_sucesso.open = True
            
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
        
    botao_cadastrar = criar_botao("Cadastrar", ft.Icons.ADD, cadastrar_veiculo, ft.Colors.TEAL_700)

    # Retorna os controles do formulário
    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Novo veículo", size=50, weight=ft.FontWeight.BOLD, color="white"),
                fabricante,
                modelo,
                ano,
                motorizacao,
                cambio,
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

def listar_veiculos(page: ft.Page):
    
    veiculos = session.query(Veiculos).all()
    
    if not veiculos:
        dlg_erros.content = ft.Text("Nenhum veículo cadastrado", color="red", size=20)
        page.open(dlg_erros)
        dlg_erros.open = True

        
        return
    #ft.ListView vai exibir em formato de lista
    lista_veiculos = ft.ListView(
    controls=[
        ft.Container(
            content=ft.Text(f"ID: {v.id} | Fabricante: {v.fabricante} | Modelo: {v.modelo} | "
                          f"Ano: {v.ano} | Motor: {v.motorizacao} | Câmbio: {v.cambio}",
                          size=16,
                          color=ft.Colors.WHITE),
            padding=10,
            border=ft.border.all(1, ft.Colors.GREY_800),
            margin=ft.margin.only(bottom=5))
        for v in veiculos
    ],
    width=900,
    spacing=5,
    padding=10
)
    
    return ft.Container(
        content=ft.Column([
            ft.Text("  Veículos Cadastrados", 
                   size=40, 
                   weight=ft.FontWeight.BOLD, 
                   color="white",
                   text_align=ft.TextAlign.LEFT),  # Alinhamento do título à esquerda
            ft.Divider(height=20),
            lista_veiculos
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

def alterar_cadastro(page: ft.Page):
    id_veiculo = ft.TextField(label="ID do Veículo", width=400)
    fabricante = ft.TextField(label="Fabricante", width=400)
    modelo = ft.TextField(label="Modelo", width=400)
    ano = ft.TextField(label="Ano", width=400)
    motorizacao = ft.TextField(label="Motorização", width=400)
    cambio = ft.TextField(label="Câmbio", width=400)

    def buscar_veiculo(e):
        if not all([id_veiculo, fabricante.value, modelo.value, ano.value, motorizacao.value, cambio.value]):
            dlg_erros.content = ft.Text("Preencha todos os campos!", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        
        if not id_veiculo.value.isdigit():
            dlg_erros.content = ft.Text("ID deve ser um número inteiro", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        
        if not ano.value.isdigit():
            dlg_erros.content = ft.Text("Ano deve ser um número inteiro", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        
        veiculo = session.query(Veiculos).filter(Veiculos.id == int(id_veiculo.value)).first()
        
        if not veiculo:
            dlg_erros.content = ft.Text("Veículo não encontrado.", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        else:
            veiculo.fabricante = fabricante.value
            veiculo.modelo = modelo.value
            veiculo.ano = ano.value
            veiculo.motorizacao = motorizacao.value
            veiculo.cambio = cambio.value
            session.commit()

            dlg_sucesso.content = ft.Text("Veiculo alterado com sucesso!", color="green", size=20)
            page.open(dlg_sucesso)
            dlg_sucesso.open = True

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
        
    botao_alterar = criar_botao("Alterar", ft.Icons.ADD, buscar_veiculo, ft.Colors.TEAL_700)

    return ft.Container(
        content =ft.Column(
            [
            ft.Text("Alterar Veículo", size=50, weight=ft.FontWeight.BOLD, color="white"),
            id_veiculo,
            fabricante,
            modelo,
            ano,
            motorizacao,
            cambio,
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