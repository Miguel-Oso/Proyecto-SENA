from src.app import app
from src.models import Base, session
from sqlalchemy import Column, Integer, String, Enum
from src.models.enums.tipo_documento import TipoDocumento

class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    tipo_documento = Column(Enum(TipoDocumento), nullable=False)
    documento = Column(String(20), unique=True, nullable=False)
    nombre = Column(String(50), nullable=False)
    ciudad = Column(String(45), nullable=False)
    direccion = Column(String(45), nullable=False)
    correo = Column(String(30), unique=True, nullable=False)
    telefono = Column(String(20), unique=True, nullable=False)

    def __init__(self, tipo_documento, documento, nombre, ciudad, direccion, correo, telefono):
        self.tipo_documento = tipo_documento
        self.documento = documento
        self.nombre = nombre
        self.ciudad = ciudad
        self.direccion = direccion
        self.correo = correo
        self.telefono = telefono

    def __str__(self):
        return f'Cliente(nombre={self.nombre}, documento={self.documento})'
    
    @staticmethod
    def get_all():
        return session.query(Cliente).all()
    
    @staticmethod
    def get_by_id(id):
        return session.query(Cliente).get(id)
    
    @staticmethod
    def get_by_documento(documento):
        return session.query(Cliente).filter(Cliente.documento == documento).all()
    
    
    def save(self):
        session.add(self)
        session.commit()
    
    def delete(self):
        session.delete(self)
        session.commit()