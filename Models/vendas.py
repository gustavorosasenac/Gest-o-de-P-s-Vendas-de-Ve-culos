import flet as ft
from DB.DB import session
from Models.table_vendas import Vendas

def cadastrar_venda(page: ft.Page):
    page.title = "Cadastrar Venda"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    def voltar_menu(e):
        page.clean()
        from Models.visual import MenuVendas
        MenuVendas.menu_vendas(page)

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
    
    data_venda = ft.TextField(label="Data da Venda (YYYY-MM-DD)", width=400)
    comprador = ft.TextField(label="Comprador", width=400)
    valor = ft.TextField(label="Valor da Venda", width=400)

    def cadastrar_venda(e):
        if not all([data_venda.value, comprador.value, valor.value]):
            print("Algum campo está vazio")
            dlg_erros.content = ft.Text("Preencha todos os campos!", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        verificar_cadastro = session.query(Vendas).filter(
            Vendas.data_venda == data_venda.value,
            Vendas.comprador == comprador.value,
            Vendas.valor == valor.value).first()
        if verificar_cadastro:
            dlg_ja_cadastrado.content = ft.Text("Venda já cadastrada", color="red", size=20)
            page.open(dlg_ja_cadastrado)
            dlg_ja_cadastrado.open = True
            return
        else:
            nova_venda = Vendas(
                data_venda=data_venda.value,
                comprador=comprador.value,
                valor=valor.value)

            session.add(nova_venda)
            session.commit()
            dlg_sucesso.content = ft.Text("Venda cadastrada com sucesso!", color="green", size=20)
            page.open(dlg_sucesso)
            dlg_sucesso.open = True

        page.update()

    page.clean()
    page.add(
        ft.Column([
            ft.Text("Cadastrar Venda", size=24, weight=ft.FontWeight.BOLD),
            data_venda,
            comprador,
            valor,
            ft.ElevatedButton(
                text="Cadastrar Venda",
                icon=ft.Icons.ADD,
                width=400,
                on_click=cadastrar_venda),
            ft.ElevatedButton(
                text="Voltar ao Menu",
                icon=ft.Icons.ARROW_BACK,
                width=400,
                on_click=voltar_menu)
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )
    
def listar_vendas(page: ft.Page):
    page.title = "Listar Vendas"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    def voltar_menu(e):
        page.clean()
        from Models.visual import MenuVendas
        MenuVendas.menu_vendas(page)

    vendas = session.query(Vendas).all()
    if not vendas:
        page.add(ft.Text("Nenhuma venda cadastrada.", size=20, color="red"),
        ft.ElevatedButton(
            text="Voltar",
            icon=ft.Icons.ARROW_BACK,
            on_click=voltar_menu))
        return
    lista_vendas = ft.ListView(
        controls=[
            ft.ListTile(
                title=ft.Text(f"ID: {v.id} Data: {v.data_venda} Comprador: {v.comprador} Valor: R$ {v.valor}")
            ) for v in vendas
        ],
        width=1200,
        height=800,
        padding=10,
        spacing=10,
        auto_scroll=True,
        expand=True,)

    page.add(
        ft.Column([
            ft.Text("Vendas Cadastradas", size=24, weight=ft.FontWeight.BOLD),
            ft.ElevatedButton(
                text="Voltar ao Menu",
                icon=ft.Icons.ARROW_BACK,
                on_click=voltar_menu),
            lista_vendas],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER))

def alterar_venda(page: ft.Page):
    page.title = "Alterar Venda"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    def voltar_menu(e):
        page.clean()
        from Models.visual import MenuVendas
        MenuVendas.menu_vendas(page)

    id_venda = ft.TextField(label="ID da Venda", width=400)
    data_venda = ft.TextField(label="Data da Venda (YYYY-MM-DD)", width=400)
    comprador = ft.TextField(label="Comprador", width=400)
    valor = ft.TextField(label="Valor da Venda", width=400)

    dlg_erros = ft.AlertDialog(
        title=ft.Text("Erro!", color="red", text_align=ft.TextAlign.CENTER),
        content=ft.Text("", color="red", size=20),
        on_dismiss=lambda e: print("Dialogo de erro fechado"),
        alignment=ft.alignment.center,
        title_padding = ft.padding.all(25))
    dlg_sucesso = ft.AlertDialog(
        title=ft.Text("Sucesso!", color="green", text_align=ft.TextAlign.CENTER),
        content=ft.Text("Venda alterada com sucesso!", color="green", size=20),
        on_dismiss=lambda e: voltar_menu(e),
        alignment=ft.alignment.center,
        title_padding = ft.padding.all(25))
    dlg_ja_cadastrado = ft.AlertDialog(
        title=ft.Text("Erro!", color="red"),
        content=ft.Text("Venda já cadastrada", color="red", size=20),
        on_dismiss=lambda e: print("Dialogo de venda existente fechado"),
        alignment=ft.alignment.center,
        title_padding = ft.padding.all(25)) 

    def buscar_venda(e):
        if not all([id_venda.value, data_venda.value, comprador.value, valor.value]):
            print("Algum campo está vazio")
            dlg_erros.content = ft.Text("Preencha todos os campos!", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        
        if not id_venda.value.isdigit():
            dlg_erros.content = ft.Text("ID deve ser um número inteiro", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        if not data_venda.value or len(data_venda.value) != 10 or data_venda.value[4] != '-' or data_venda.value[7] != '-':
            dlg_erros.content = ft.Text("A data precisa ser (YYYY-MM-DD)", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
            return
        
        venda = session.query(Vendas).filter(Vendas.id == int(id_venda.value)).first()
        
        if not venda:
            dlg_erros.content = ft.Text("Venda não encontrada.", color="red", size=20)
            page.open(dlg_erros)
            dlg_erros.open = True
        else:
            venda.data_venda = data_venda.value
            venda.comprador = comprador.value
            venda.valor = valor.value
            session.commit()

            dlg_sucesso.content = ft.Text("Venda alterada com sucesso!", color="green", size=20)
            page.open(dlg_sucesso)
            dlg_sucesso.open = True

        page.update()

    page.clean()
    page.add(
        ft.Column([
            ft.Text("Alterar Venda", size=24, weight=ft.FontWeight.BOLD),
            id_venda,
            data_venda,
            comprador,
            valor,
            ft.ElevatedButton(
                text="Alterar Venda",
                icon=ft.Icons.EDIT,
                on_click=buscar_venda),
            ft.ElevatedButton(
                text="Voltar ao Menu",
                icon=ft.Icons.ARROW_BACK,
                on_click=voltar_menu)],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER))

def excluir_venda(page: ft.Page):
    page.title = "Excluir Venda"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    def voltar_menu(e):
        page.clean()
        from Models.visual import MenuVendas
        MenuVendas.menu_vendas(page)

    dlg_erros = ft.AlertDialog(
        title=ft.Text("Erro!", color="red", text_align=ft.TextAlign.CENTER),
        content=ft.Text("", color="red", size=20),
        on_dismiss=lambda e: print("Dialogo de erro fechado"),
        alignment=ft.alignment.center,
        title_padding = ft.padding.all(25))
    dlg_sucesso = ft.AlertDialog(
        title=ft.Text("Sucesso!", color="green", text_align=ft.TextAlign.CENTER),
        content=ft.Text("Venda excluída com sucesso!", color="green", size=20),
        on_dismiss=lambda e: voltar_menu(e),
        alignment=ft.alignment.center,
        title_padding = ft.padding.all(25))
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

    page.clean()
    page.add(
        ft.Column([
            ft.Text("Excluir Venda", size=25, weight=ft.FontWeight.BOLD),
            id_venda,
            ft.ElevatedButton(
                text="Excluir Venda",
                icon=ft.Icons.DELETE,
                on_click=excluir_venda),
            ft.ElevatedButton(
                text="Voltar ao Menu",
                icon=ft.Icons.ARROW_BACK,
                on_click=voltar_menu)],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER))