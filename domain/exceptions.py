# domain/exceptions.py
"""
Excepciones del dominio.

SOLID:
- SRP: Cada excepción representa un error específico
"""

class DomainException(Exception):
    """Excepción base del dominio"""
    pass


class PizzaNotFoundException(DomainException):
    """Pizza no encontrada en el menú"""
    pass


class OrderNotFoundException(DomainException):
    """Pedido no encontrado"""
    pass


class InvalidSizeException(DomainException):
    """Tamaño de pizza inválido"""
    pass