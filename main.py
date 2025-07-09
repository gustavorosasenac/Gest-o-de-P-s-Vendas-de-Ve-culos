import flet as ft
from DB.Database import Base, engine
from Models.login import Login
from DB.Tables.table_veiculos import Veiculos
from DB.Tables.table_vendas import Vendas
from DB.Tables.table_vendas import VendaVeiculo
from DB.Tables.table_feeback import Feedback
from DB.Tables.table_item import Itens
from DB.Tables.table_chamado import Chamado
from DB.Tables.table_diagnostico import Diagnostico
from DB.Tables.table_orcamento import Orcamento
from DB.Tables.table_usuario import Usuario
from Models.visual import Menu_principal


#cria o BD
Base.metadata.create_all(engine)

#Chama o menu principal
def main(page: ft.Page):
    Menu_principal(page)
    page.update()
    
#Inicia a aplicação chamando o main
if __name__ == "__main__":
    ft.app(target=main)
