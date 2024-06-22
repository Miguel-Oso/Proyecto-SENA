from src.app import app
from src.models import Base, session
from sqlalchemy import Column, Integer, DateTime, String, Date, Enum, Float
from datetime import datetime
from src.models.enums.unidadMedida import UnidadMedida

class Material(Base):
    __tablename__ = 'materiales'
    id = Column(Integer, primary_key=True)
    fecha_pedido = Column(Date)
    fecha_recibido = Column(DateTime, default=datetime.now())
    codigo = Column(String(50), unique=True, nullable=False) 
    nombre = Column(String(50), nullable=False)
    referencia = Column(String(50), nullable=False)
    proveedor = Column(String(50), nullable=False)
    descripcion = Column(String(50), nullable=False)
    producto_final = Column(String(50), nullable=False)
    unidad_medida = Column(Enum(UnidadMedida), nullable=False)
    cantidad = Column(Float, nullable=False)
    comentarios = Column(String(50), nullable=False)

    def __init__(self, fecha_pedido, fecha_recibido, codigo, nombre, referencia, proveedor, descripcion, producto_final, unidad_medida, cantidad, comentarios):
        self.fecha_pedido = fecha_pedido
        self.fecha_recibido = fecha_recibido
        self.codigo = codigo
        self.nombre = nombre
        self.referencia = referencia
        self.proveedor = proveedor
        self.descripcion = descripcion
        self.producto_final = producto_final
        self.unidad_medida = unidad_medida
        self.cantidad = cantidad
        self.comentarios = comentarios

    def __str__(self):
        return f'Material(nombre={self.nombre}, descripcion={self.descripcion})'
    
    def agregar_material(material):
        session.add(material)
        session.commit()

    def obtener_materiales():
        return session.query(Material).all()
    
    def eliminar_material(material):
        session.delete(material)
        session.commit()
