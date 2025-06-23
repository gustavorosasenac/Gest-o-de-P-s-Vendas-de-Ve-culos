from DB.Database import Base
from sqlalchemy import Column, Integer, String, Date

class Vendas(Base):
    __tablename__ = "vendas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    data_venda = Column(Date, nullable=False)
    comprador = Column(String(100), nullable=False)
    valor = Column(String(100), nullable=False)