from DB.Database import Base
from sqlalchemy import Column, Integer, String, Float

class Itens(Base):
    __tablename__ = 'itens'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    preco = Column(Float, nullable=False)
    quantidade = Column(Integer, nullable=False)