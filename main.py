import flet as ft
from DB import session, Base, engine
from veiculos import Veiculos

Base.metadata.create_all(engine)

def main(page: ft.Page):
    menu_principal(page)

def menu_principal(page: ft.Page):
    page.title = "Menu Principal"
    page.theme_mode = ft.ThemeMode.DARK

    def fechar_app(e):
        session.close()
        page.clean()
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.add(ft.Text("Aplicação fechada."))
        page.update()
        
    def mostrar_cadastros(e):
        page.clean()
        menu_cadastros(page)

    def mostrar_consultas(e):
        page.clean()
        menu_consultas(page)

    titulo = ft.Text("🚘 Sistema de Veículos", size=40, weight=ft.FontWeight.BOLD, color="white")

    botao_cadastros = ft.ElevatedButton(
        text="Cadastros",
        icon=ft.Icons.ASSIGNMENT,
        width=400,
        on_click=mostrar_cadastros)
    
    botao_consultas = ft.ElevatedButton(
        text="Consultas",
        icon=ft.Icons.SEARCH,
        width=400,
        on_click=mostrar_consultas)
    
    botao_fechar_app = ft.ElevatedButton(
        text="Fechar Aplicação",
        icon=ft.Icons.CLOSE,
        width=400,
        on_click=fechar_app)
        
    conteudo = ft.Column(
        [titulo, botao_cadastros, botao_consultas, botao_fechar_app],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    
    page.add(
        ft.Stack(
            controls=[
                ft.Image(
                    src="https://img.odcdn.com.br/wp-content/uploads/2024/03/shutterstock_1082263868-1.jpg",
                    fit=ft.ImageFit.COVER,
                    width=page.width,
                    height=page.height
                ),
                ft.Container(
                    content=conteudo,
                    alignment=ft.alignment.center,
                    padding=40,
                    bgcolor="#00000088",
                    border_radius=10
                )
            ],
            expand=True
        )
    )

def menu_cadastros(page: ft.Page):
    page.title = "Menu de Cadastros"
    page.theme_mode = ft.ThemeMode.DARK
    
    def voltar_menu(e):
        page.clean()
        menu_principal(page)
        
    def cadastrar_veiculo(e):
        page.clean()
        cadastros_de_veiculo(page)
        
    def veiculos_cadastrados(e):
        page.clean()
        listar_veiculos(page)
        
    def alterar_cadastro_veiculo(e):
        page.clean()
        pass
        
    def excluir_cadastro_veiculo(e):
        page.clean()
        pass

    titulo = ft.Text("Cadastros", size=40, weight=ft.FontWeight.BOLD, color="white")

    botoes = [
        ft.ElevatedButton(
            text="Cadastrar Veículo",
            icon=ft.Icons.ADD,
            width=400,
            on_click=cadastrar_veiculo),
        ft.ElevatedButton(
            text="Mostrar Veículos Cadastrados",
            icon=ft.Icons.LIST,
            width=400,
            on_click=veiculos_cadastrados),
        ft.ElevatedButton(
            text="Alterar Cadastro de Veículo",
            icon=ft.Icons.EDIT,
            width=400,
            on_click=alterar_cadastro_veiculo),
        ft.ElevatedButton(
            text="Excluir Cadastro de Veículo",
            icon=ft.Icons.DELETE,
            width=400,
            on_click=excluir_cadastro_veiculo),
        ft.ElevatedButton(
            text="Voltar ao Menu Principal",
            icon=ft.Icons.ARROW_BACK,
            width=400,
            on_click=voltar_menu)
    ]
        
    conteudo = ft.Column(
        [titulo, *botoes],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    
    page.add(
        ft.Stack(
            controls=[
                ft.Image(
                    src="https://img.odcdn.com.br/wp-content/uploads/2024/03/shutterstock_1082263868-1.jpg",
                    fit=ft.ImageFit.COVER,
                    width=page.width,
                    height=page.height
                ),
                ft.Container(
                    content=conteudo,
                    alignment=ft.alignment.center,
                    padding=40,
                    bgcolor="#00000088",
                    border_radius=10
                )
            ],
            expand=True
        )
    )

def menu_consultas(page: ft.Page):
    page.title = "Menu de Consultas"
    page.theme_mode = ft.ThemeMode.DARK
    
    def voltar_menu(e):
        page.clean()
        menu_principal(page)
        
    titulo = ft.Text("Cadastros", size=40, weight=ft.FontWeight.BOLD, color="white")

    botoes = [
        ft.ElevatedButton(
            text="Voltar ao Menu Principal",
            icon=ft.Icons.ARROW_BACK,
            width=400,
            on_click=voltar_menu)
    ]
        
    conteudo = ft.Column(
        [titulo, *botoes],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    
    page.add(
        ft.Stack(
            controls=[
                ft.Image(
                    src="https://img.odcdn.com.br/wp-content/uploads/2024/03/shutterstock_1082263868-1.jpg",
                    fit=ft.ImageFit.COVER,
                    width=page.width,
                    height=page.height
                ),
                ft.Container(
                    content=conteudo,
                    alignment=ft.alignment.center,
                    padding=40,
                    bgcolor="#00000088",
                    border_radius=10
                )
            ],
            expand=True
        )
    )

def cadastros_de_veiculo(page: ft.Page):
    def voltar_menu(e):
        page.clean()
        menu_cadastros(page)
    
    fabricante = ft.TextField(label="Fabricante", width=400)
    modelo = ft.TextField(label="Modelo", width=400)    
    ano = ft.TextField(label="Ano", width=400)
    motorizacao = ft.TextField(label="Motorização", width=400)
    cambio = ft.TextField(label="Câmbio", width=400)
    
    dlg_erro_campos = ft.AlertDialog(
        title=ft.Text("Erro!", color="red"),
        content=ft.Text("Preencha todos os campos!", color="red", size=20),
        on_dismiss=lambda e: print("Dialogo de erro fechado"))
    
    dlg_sucesso = ft.AlertDialog(
        title=ft.Text("Sucesso!", color="green"),
        content=ft.Text("Veículo cadastrado com sucesso!", color="green", size=20),
        on_dismiss=lambda e: voltar_menu(e))
    
    dlg_ja_cadastrado = ft.AlertDialog(
        title=ft.Text("Erro!", color="red"),
        content=ft.Text("Veículo já cadastrado", color="red", size=20),
        on_dismiss=lambda e: print("Dialogo de veículo existente fechado"))

    def cadastrar_veiculo(e):
        if not all([fabricante.value, modelo.value, ano.value, motorizacao.value, cambio.value]):
            dlg_erro_campos.content = ft.Text("Preencha todos os campos!", color="red", size=20)
            page.dialog = dlg_erro_campos
            dlg_erro_campos.open = True
        elif not ano.value.isdigit():
            dlg_erro_campos.content = ft.Text("Ano deve ser um número inteiro", color="red", size=20)
            page.dialog = dlg_erro_campos
            dlg_erro_campos.open = True
        else: 
            verificar_cadastro = session.query(Veiculos).filter(
                Veiculos.fabricante == fabricante.value,
                Veiculos.modelo == modelo.value,
                Veiculos.ano == int(ano.value)
            ).first()
            
            if verificar_cadastro:
                page.dialog = dlg_ja_cadastrado
                dlg_ja_cadastrado.open = True
            else:
                novo_veiculo = Veiculos(
                    fabricante=fabricante.value,
                    modelo=modelo.value,
                    ano=int(ano.value),
                    motorizacao=motorizacao.value,
                    cambio=cambio.value)
                
                session.add(novo_veiculo)
                session.commit()
                page.dialog = dlg_sucesso
                dlg_sucesso.open = True
        
        page.update()

    page.title = "Tela de Cadastros"
    page.clean()
    page.add(
        ft.Column([
            ft.Text("Cadastros", size=50, weight=ft.FontWeight.BOLD, color="white"),
            fabricante,
            modelo,
            ano,
            motorizacao,
            cambio,
            ft.ElevatedButton(
                text="Cadastrar Veículo",
                icon=ft.Icons.ADD,
                width=400,
                on_click=cadastrar_veiculo),
            ft.ElevatedButton(
                text="Voltar ao Menu",
                icon=ft.Icons.ARROW_BACK,
                width=400,
                on_click=voltar_menu)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

def listar_veiculos(page: ft.Page):
    page.title = "Veículos Cadastrados"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    def voltar_menu(e):
        page.clean()
        menu_cadastros(page)
    
    veiculos = session.query(Veiculos).all()
    
    if not veiculos:
        page.add(ft.Text("Nenhum veículo cadastrado.", size=20, color="red"))
        return
    
    lista_veiculos = ft.ListView(
        controls=[
            ft.ListTile(
                title=ft.Text(f"{v.fabricante} {v.modelo} ({v.ano}) - {v.motorizacao} - {v.cambio}")
            ) for v in veiculos
        ],
        width=600,
        height=400,
        padding=10
    )
    
    page.clean()
    page.add(
        ft.Column([
            ft.Text("Veículos Cadastrados", size=24, weight=ft.FontWeight.BOLD),
            lista_veiculos,
            ft.ElevatedButton(
                text="Voltar",
                icon=ft.Icons.ARROW_BACK,
                on_click=voltar_menu)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

    

if __name__ == "__main__":
    ft.app(target=main)



def procurar_veiculo(page: ft.Page):
    page.title = "Catálogo de Veículos"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    titulo = ft.Text("Catálogo de Veículos", size=24, weight=ft.FontWeight.BOLD)
    
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
                dropdown_ano.options.append(ft.dropdown.Option(str(ano[0])))
        
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
    
    def voltar_menu(e):
        page.clean()
        menu_cadastros(page)
    
    page.clean()
    page.add(
        ft.Column([
            titulo,
            ft.Row([dropdown_marca], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([dropdown_modelo], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([dropdown_ano], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([dropdown_motor], alignment=ft.MainAxisAlignment.CENTER),
            ft.ElevatedButton(
                text="Voltar",
                icon=ft.Icons.ARROW_BACK,
                on_click=voltar_menu)
        ],
        spacing=20,
        alignment=ft.MainAxisAlignment.CENTER)
    )
    
    carregar_marcas()






