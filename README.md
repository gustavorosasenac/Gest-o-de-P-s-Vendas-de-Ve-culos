# Gest-o-de-P-s-Vendas-de-Ve-culos
Inteligência de manutenção corretiva e preventiva


Interface grafico sera usada "flet"

Bibliotecas necessarias: pip install flet, mysql, pymysql, sqlachemy, cryptography, werkzeug


comando para compilar

pyinstaller --onefile --windowed --name "AppVeiculos" --add-data "DB;DB" --add-data "assets;assets"  --hidden-import "DB.Database" --hidden-import "sqlalchemy" --hidden-import "sqlite3" main.py

