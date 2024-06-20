from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import pymysql

engine = create_engine("mysql+pymysql://root@localhost/proyecto-sena")
connection = engine.connect()

Base = declarative_base()
Base.metadata.bind = engine

Session = sessionmaker(bind=engine)

session = Session()