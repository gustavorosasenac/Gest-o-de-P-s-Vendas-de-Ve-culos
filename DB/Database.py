from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("mysql+pymysql://root:root@localhost:3306/veiculos")

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()