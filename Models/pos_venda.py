import flet as ft
from DB.Database import session
from DB.Tables.table_veiculos import Veiculos

#inicializa o sistema de registro de ocorrências
def registrar_ocorrencia(page: ft.Page):
    page.title = "Registrar Ocorrência"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    titulo = ft.Text("Registrar Ocorrência", size=24, weight=ft.FontWeight.BOLD)

#Função do botão de voltar ao menu
    def voltar_menu(e):
        from Models.visual import MenuPosvenda
        page.clean()
        MenuPosvenda.menu_pos(page)













    #função pronta mas sem uso até o momento
def procurar_veiculo(page: ft.Page):
    page.title = "Catálogo de Veículos"
    page.theme_mode = ft.ThemeMode.DARK
    
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
        from Models.visual import MenuPosvenda
        page.clean()
        MenuPosvenda.menu_pos(page)
    
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
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )
    
    carregar_marcas()
