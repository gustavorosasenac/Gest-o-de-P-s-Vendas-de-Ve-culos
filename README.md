# Gestão de pós-venda de veiculos
Inteligência de manutenção corretiva e preventiva


Interface grafica: "flet"

Bibliotecas necessarias: pip install flet, mysql, pymysql, sqlalchemy, cryptography, werkzeug, dotenv




comando para compilar

pyinstaller --onefile --windowed --name "AppVeiculos" --add-data "DB;DB" --add-data "assets;assets"  --hidden-import "DB.Database" --hidden-import "sqlalchemy" --hidden-import "sqlite3" main.py

