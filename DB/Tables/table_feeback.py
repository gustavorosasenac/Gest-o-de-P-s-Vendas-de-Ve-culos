from DB.Database import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class Feedback(Base):
    __tablename__ = 'feedback'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_venda_veiculo = Column(Integer, ForeignKey('vendas_veiculos.id'))
    comentario = Column(String(500), nullable=True)
