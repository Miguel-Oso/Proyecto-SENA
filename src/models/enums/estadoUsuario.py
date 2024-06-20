from enum import Enum

class EstadoUsuario(Enum):
    ACTIVO = 'Activo'
    INACTIVO = 'Inactivo'
    BLOQUEADO = 'Bloqueado'
    ELIMINADO = 'Eliminado'
    PENDIENTE = 'Pendiente'

 