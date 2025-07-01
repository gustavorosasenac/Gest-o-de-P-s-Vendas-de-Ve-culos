from DB.Database import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Boolean, Float

class Vendas(Base):
    __tablename__ = "vendas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    data_venda = Column(Date, nullable=False)
    comprador = Column(String(100), nullable=False)
    valor = Column(String(100), nullable=False)

class Vendaveiculo(Base):
    __tablename__ = 'vendas_veiculos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_veiculo = Column(Integer, ForeignKey('veiculos.id'))
    id_vendas = Column(Integer, ForeignKey('vendas.id'))