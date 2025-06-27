from DB.Database import Base
from sqlalchemy import Column, Integer, String, Date, Float, Boolean,ForeignKey

class Chamado(Base):
    __tablename__ = 'chamado'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_venda_veiculo = Column(Integer, ForeignKey('vendas_veiculos.id'))
    descricao = Column(String(500))

class Diagnostico(Base):
    __tablename__ = 'diagnostico'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_chamado = Column(Integer, ForeignKey('chamado.id'))
    categoria = Column(String(100))
    sintoma = Column(String(100), nullable=False)
    manutencao = Column(Boolean, default=False)

class Orcamento(Base):
    __tablename__ = 'orcamento'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_diagnostico = Column(Integer, ForeignKey('diagnostico.id'))
    id_item = Column(Integer, ForeignKey('itens.id'))
    custo_total = Column(Float, nullable=False)
    id_venda_veiculo = Column(Integer, ForeignKey('vendas_veiculos.id'))

class Itens(Base):
    __tablename__ = 'itens'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    preco = Column(Float, nullable=False)
    quantidade = Column(Integer, nullable=False)