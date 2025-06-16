from DB import Base
from sqlalchemy import Column, Integer, String, Date, Float

class Veiculos(Base):
    __tablename__ = "veiculos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    fabricante = Column(String(100), nullable=False)
    modelo = Column(String(100), nullable=False)
    ano = Column(Integer, nullable=False)
    motorizacao = Column(String(100), nullable=False)
    cambio = Column(String(100), nullable=False)