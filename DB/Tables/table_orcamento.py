from DB.Database import Base
from sqlalchemy import Column, Integer, Float,ForeignKey

class Orcamento(Base):
    __tablename__ = 'orcamento'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_diagnostico = Column(Integer, ForeignKey('diagnostico.id'))
    id_item = Column(Integer, ForeignKey('itens.id'))
    custo_total = Column(Float, nullable=False)
    id_venda_veiculo = Column(Integer, ForeignKey('vendas_veiculos.id'))