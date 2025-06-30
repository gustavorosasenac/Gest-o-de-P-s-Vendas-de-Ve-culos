import flet as ft
from DB.Database import Base, engine
from Models.visual import Menu_principal

#cria o BD
Base.metadata.create_all(engine)

#Chama o menu principal
def main(page: ft.Page):
    Menu_principal(page)
    
#Inicia a aplicação chamando o main
if __name__ == "__main__":
    ft.app(target=main)



