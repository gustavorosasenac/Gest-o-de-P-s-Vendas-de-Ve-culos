import flet as ft
from DB.DB import session
from Models.table_veiculos import Veiculos

def cadastros_de_veiculo(page: ft.Page):
    page.title = "Tela de cadastros"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def voltar_menu(e):
        from Models.visual import MenuCarros
        page.clean()
        MenuCarros.menu_cadastros(page)

    fabricante = ft.TextField(label="Fabricante", width=400)
    modelo = ft.TextField(label="Modelo", width=400)    
    ano = ft.TextField(label="Ano  (YYYY-MM-DD)", width=400)
    motorizacao = ft.TextField(label="Motorização", width=400)
    cambio = ft.TextField(label="Câmbio", width=400)
    
    dlg_erros = ft.AlertDialog(
        title=ft.Text("Erro!", color="red", text_align=ft.TextAlign.CENTER),
        content=ft.Text("", color="red", size=20),
        on_dismiss=lambda e: print("Dialogo de erro fechado"),
        alignment=ft.alignment.center,
        title_padding = ft.padding.all(25))
    
    dlg_sucesso = ft.AlertDialog(
        title=ft.Text("Sucesso!", color="green", text_align=ft.TextAlign.CENTER),
        content=ft.Text("Veículo cadastrado com sucesso!", color="green", size=20),
        on_dismiss=lambda e: voltar_menu(e),
        alignment=ft.alignment.center,
        title_padding = ft.padding.all(25))
    
    dlg_ja_cadastrado = ft.AlertDialog(
        title=ft.Text("Erro!", color="red"),
        content=ft.Text("Veículo já cadastrado", color="red", size=20),
        on_dismiss=lambda e: print("Dialogo de veículo existente fechado"),
        alignment=ft.alignment.center,
        title_padding = ft.padding.all(25))

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
        
        page.update()

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
    botao_voltar = ft.ElevatedButton(
        text="Voltar ao Menu",
        icon=ft.Icons.ARROW_BACK,
        on_click=lambda e: voltar_menu(e),
        width=400
    )
    def voltar_menu(e):
        from Models.visual import MenuCarros
        page.clean()
        MenuCarros.menu_cadastros(page)
    
    veiculos = session.query(Veiculos).all()
    
    if not veiculos:
        page.add(ft.Text("Nenhum veículo cadastrado.", size=20, color="red"),
        ft.Column([
            ft.ElevatedButton(
                text="Voltar",
                icon=ft.Icons.ARROW_BACK,
                on_click=voltar_menu)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER))
        return
    
    lista_veiculos = ft.ListView(
        controls=[
            ft.ListTile(
                title=ft.Text(f"ID: {v.id} Fabricante: {v.fabricante} Modelo: {v.modelo} Ano: {v.ano} Motor: {v.motorizacao} Cambio: {v.cambio}")
            ) for v in veiculos
        ],
        width=1200,
        height=800,
        padding=10,
        spacing=10,
        auto_scroll=True,
        expand=True,)
    
    page.add(
        ft.Column([
            ft.Text("Veículos Cadastrados", size=24, weight=ft.FontWeight.BOLD),
        botao_voltar, lista_veiculos ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER))

def alterar_cadastro(page: ft.Page):
    page.title = "Alterar Cadastro de Veículo"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def voltar_menu(e):
        from Models.visual import MenuCarros
        page.clean()
        MenuCarros.menu_cadastros(page)
        
    id_veiculo = ft.TextField(label="ID do Veículo", width=400)
    fabricante = ft.TextField(label="Fabricante", width=400)
    modelo = ft.TextField(label="Modelo", width=400)
    ano = ft.TextField(label="Ano", width=400)
    motorizacao = ft.TextField(label="Motorização", width=400)
    cambio = ft.TextField(label="Câmbio", width=400)

    dlg_erros = ft.AlertDialog(
        title=ft.Text("Erro!", color="red", text_align=ft.TextAlign.CENTER),
        content=ft.Text("", color="red", size=20),
        on_dismiss=lambda e: print("Dialogo de erro fechado"),
        alignment=ft.alignment.center,
        title_padding = ft.padding.all(25))
    
    dlg_sucesso = ft.AlertDialog(
        title=ft.Text("Sucesso!", color="green", text_align=ft.TextAlign.CENTER),
        content=ft.Text("Veículo cadastrado com sucesso!", color="green", size=20),
        on_dismiss=lambda e: voltar_menu(e),
        alignment=ft.alignment.center,
        title_padding = ft.padding.all(25))
    
    dlg_ja_cadastrado = ft.AlertDialog(
        title=ft.Text("Erro!", color="red"),
        content=ft.Text("Veículo já cadastrado", color="red", size=20),
        on_dismiss=lambda e: print("Dialogo de veículo existente fechado"),
        alignment=ft.alignment.center,
        title_padding = ft.padding.all(25))

    def buscar_veiculo(e):

        if not all([id_veiculo, fabricante.value, modelo.value, ano.value, motorizacao.value, cambio.value]):
            print("Algum campo está vazio")
            dlg_erros.content = ft.Text("Preencha todos os campos!", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        
        if not ano.value.isdigit():
            dlg_erros.content = ft.Text("Ano deve ser um número inteiro", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        
        if not id_veiculo.value.isdigit():
            dlg_erros.content = ft.Text("ID deve ser um número inteiro", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        
        veiculo = session.query(Veiculos).filter(Veiculos.id == int(id_veiculo.value)).first()
        
        if not veiculo:
            page.add(ft.Text("Veículo não encontrado.", color="red"),
            ft.ElevatedButton(
                text="Voltar", 
                icon=ft.Icons.ARROW_BACK,
                on_click=voltar_menu))
            
        else:
            veiculo.fabricante = fabricante.value
            veiculo.modelo = modelo.value
            veiculo.ano = ano.value
            veiculo.motorizacao = motorizacao.value
            veiculo.cambio = cambio.value
            session.commit()

            dlg_sucesso.content = ft.Text("Veiculo cadastrado com sucesso!", color="green", size=20)
            page.open(dlg_sucesso)
            dlg_erros.open = True
            return
        page.update()

    page.clean()        
    page.add(
        ft.Column([
            ft.Text("Alterar Veiculo", size=24, weight=ft.FontWeight.BOLD),
            id_veiculo, fabricante, modelo, ano, motorizacao, cambio,
            ft.ElevatedButton(
                text="Alterar Veículo",
                icon=ft.Icons.ADD,
                on_click=buscar_veiculo),
            ft.ElevatedButton(
                text="Voltar",
                icon=ft.Icons.ARROW_BACK,
                on_click=voltar_menu)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )
 
def excluir_veiculo(page: ft.Page):
    page.title = "Excluir Veículo"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    def voltar_menu(e):
        from Models.visual import MenuCarros
        page.clean()
        MenuCarros.menu_cadastros(page)

    dlg_erros = ft.AlertDialog(
        title=ft.Text("Erro!", color="red", text_align=ft.TextAlign.CENTER),
        content=ft.Text("", color="red", size=20),
        on_dismiss=lambda e: print("Dialogo de erro fechado"),
        alignment=ft.alignment.center,
        title_padding = ft.padding.all(25))
    
    dlg_sucesso = ft.AlertDialog(
        title=ft.Text("Sucesso!", color="green", text_align=ft.TextAlign.CENTER),
        content=ft.Text("Veículo cadastrado com sucesso!", color="green", size=20),
        on_dismiss=lambda e: voltar_menu(e),
        alignment=ft.alignment.center,
        title_padding = ft.padding.all(25))
    
    dlg_ja_cadastrado = ft.AlertDialog(
        title=ft.Text("Erro!", color="red"),
        content=ft.Text("Veículo já cadastrado", color="red", size=20),
        on_dismiss=lambda e: print("Dialogo de veículo existente fechado"),
        alignment=ft.alignment.center,
        title_padding = ft.padding.all(25))
    
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

        id_veiculo.value = ""
        page.update()
    
    page.clean()
    page.add(
        ft.Column([
            ft.Text("Excluir Veículo", size=24, weight=ft.FontWeight.BOLD),
            id_veiculo,
            ft.ElevatedButton(
                text="Excluir Veículo",
                icon=ft.Icons.DELETE,
                on_click=excluir_veiculo),
            ft.ElevatedButton(
                text="Voltar",
                icon=ft.Icons.ARROW_BACK,
                on_click=voltar_menu)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )