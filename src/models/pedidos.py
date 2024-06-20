from src.app import app
from src.models import Base, session
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float

class Pedido(Base):
    __tablename__ = 'pedidos'
    id = Column(Integer, primary_key=True)
    orden_compra = Column(String(50))
    fecha_pedido = Column(Date)
    fecha_recibido = Column(Date)
    fecha_despacho = Column(Date)
    cliente_id = Column(Integer, ForeignKey('clientes.id'))
    articulo = Column(String(50))
    descripcion = Column(String(50))
    cantidad = Column(Integer)
    precio = Column(Float)
    total = Column(Float)
    comentarios = Column(String(80))

    def __init__(self, orden_compra, fecha_pedido, fecha_recibido, fecha_despacho, cliente_id, articulo, descripcion, cantidad, precio, comentarios):
        self.orden_compra = orden_compra
        self.fecha_pedido = fecha_pedido
        self.fecha_recibido = fecha_recibido
        self.fecha_despacho = fecha_despacho
        self.cliente_id = cliente_id
        self.articulo = articulo
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio = precio
        self.total = self.cantidad * self.precio
        self.comentarios = comentarios

    def __str__(self):
        return f'Pedido(articulo={self.articulo}, descripcion={self.descripcion})'

    def agregar_pedido(pedido):
        session.add(pedido)
        session.commit()

    def obtener_pedidos():
        return session.query(Pedido).all()
    
    def eliminar_pedido(pedido):
        session.delete(pedido)
        session.commit()
