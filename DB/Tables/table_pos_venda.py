from DB.Database import Base
from sqlalchemy import Column, Integer, String, Date, Float

class Ocorrencia(Base):
    __tablename__ = 'ocorrencias'
    id = Column(Integer, primary_key=True, autoincrement=True)
