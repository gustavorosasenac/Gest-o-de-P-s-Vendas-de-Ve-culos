from DB.Database import Base
from sqlalchemy import Column, Integer, String,ForeignKey

class Chamado(Base):
    __tablename__ = 'chamado'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_venda_veiculo = Column(Integer, ForeignKey('vendas_veiculos.id'))
    descricao = Column(String(500))