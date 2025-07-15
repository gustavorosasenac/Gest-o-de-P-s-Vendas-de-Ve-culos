from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()

usuario = os.getenv("USUARIO")
senha = os.getenv("SENHA")

#engine = create_engine(f"mysql+pymysql://{usuario}:{senha}@localhost:3306/veiculos")


BASE_DIR = Path(__file__).parent
DATABASE_URL = f"sqlite:///{BASE_DIR}/veiculos.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

