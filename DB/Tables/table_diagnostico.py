from DB.Database import Base
from sqlalchemy import Column, Integer, String, Boolean,ForeignKey

class Diagnostico(Base):
    __tablename__ = 'diagnostico'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_chamado = Column(Integer, ForeignKey('chamado.id'))
    categoria = Column(String(100))
    sintoma = Column(String(100), nullable=False)
    manutencao = Column(Boolean, default=False)