import datetime
from src.app import app
from src.models import session, Base 
from sqlalchemy import Column, Integer, String, Enum, DateTime
from src.models.enums.tipo_documento import TipoDocumento
from src.models.enums.rol import Rol
from src.models.enums.estadoUsuario import EstadoUsuario

class User(Base): 
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True) 
    username = Column(String(64), unique=True) 
    password = Column(String(100), unique=True, nullable=False)
    first_name = Column(String(20), nullable=False)
    second_name = Column(String(20))
    first_apellido = Column(String(20), nullable=False)
    second_apellido = Column(String(20))
    tipo_documento = Column(Enum(TipoDocumento), nullable=False)
    documento = Column(String(30), unique=True, nullable=False)
    email = Column(String(64), unique=True, nullable=False)
    phone = Column(String(40), unique=True, nullable=False)
    address = Column(String(60), nullable=False)
    city = Column(String(50), nullable=False)
    country = Column(String(50), nullable=False)
    rol = Column(Enum(Rol), nullable=False)
    status = Column(Enum(EstadoUsuario), nullable=False)
    fecha_documento = Column(DateTime, default=datetime.datetime.now())

    def __init__(self, username, password, first_name, second_name, first_apellido, second_apellido, tipo_documento, documento, email, phone, address, city, country, rol, status):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.second_name = second_name
        self.first_apellido = first_apellido
        self.second_apellido = second_apellido
        self.tipo_documento = tipo_documento
        self.documento = documento
        self.email = email
        self.phone = phone
        self.address = address
        self.city = city
        self.country = country   
        self.rol = rol
        self.status = status

    def __repr__(self):
        return f'<User {self.username}>'
    
    def save(self):
        session.add(self)
        session.commit()

    def delete(self):
        session.delete(self)
        session.commit()

    def update(self):
        session.commit()

    @staticmethod
    def get_all():
        return session.query(User).all()
    
    @staticmethod
    def get_by_id(id):
        return session.query(User).get(id)
    
    @staticmethod
    def get_by_username(username):
        return session.query(User).filter_by(username=username).first()
    
    @staticmethod
    def get_by_documento(documento):
        return session.query(User).filter_by(documento=documento).first()
    
    @staticmethod
    def get_by_email(email):
        return session.query(User).filter_by(email=email).first()
    
    @staticmethod
    def get_by_phone(phone):
        return session.query(User).filter_by(phone=phone).first()
    
    @staticmethod
    def get_by_address(address):
        return session.query(User).filter_by(address=address).first()
    
    @staticmethod
    def get_by_city(city):
        return session.query(User).filter_by(city=city).first()
    
    @staticmethod
    def get_by_country(country):
        return session.query(User).filter_by(country=country).first()
    
    @staticmethod
    def delete_all():
        session.query(User).delete()
        session.commit()

    @staticmethod
    def count():
        return session.query(User).count()
    
    