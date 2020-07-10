from enum import Enum

class OrderStatus(Enum):
    CREADO = 'CREADO'
    PAGADO = 'PAGADO'
    COMPLETADO = 'COMPLETADO'
    CANCELADO = 'CANCELADO'

choices = [ (tag, tag.value) for tag in OrderStatus]
