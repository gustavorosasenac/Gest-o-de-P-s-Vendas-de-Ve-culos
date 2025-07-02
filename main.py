import flet as ft
from DB.Database import Base, engine
from Models.login import Login
from DB.Tables.table_veiculos import Veiculos
from DB.Tables.table_vendas import Vendas
from DB.Tables.table_vendas import VendaVeiculo
from DB.Tables.table_feeback import Feedback
from DB.Tables.table_item import Itens
from DB.Tables.table_chamado import Chamado
from DB.Tables.table_pos_venda import Diagnostico, Orcamento

#cria o BD
Base.metadata.create_all(engine)

#Chama o menu principal
def main(page: ft.Page):
    Login(page)
    
#Inicia a aplicação chamando o main
if __name__ == "__main__":
    ft.app(target=main)



