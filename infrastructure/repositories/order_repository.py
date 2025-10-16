# infrastructure/repositories/order_repository.py
"""
Implementación concreta del repositorio de pedidos.

SOLID:
- SRP: Solo gestiona pedidos
- DIP: Implementa la interfaz OrderRepository
"""

from typing import Dict, List, Optional
from domain.interfaces import OrderRepository
from domain.entities import Order
from domain.exceptions import OrderNotFoundException

class InMemoryOrderRepository(OrderRepository):
    """Repositorio de pedidos en memoria"""
    
    def __init__(self):
        self._orders: Dict[str, Order] = {}
    
    def save(self, order: Order) -> None:
        """Guardar un pedido"""
        self._orders[order.order_id] = order
    
    def get_by_id(self, order_id: str) -> Optional[Order]:
        """Obtener pedido por ID"""
        if order_id not in self._orders:
            raise OrderNotFoundException(f"Pedido '{order_id}' no encontrado")
        return self._orders[order_id]
    
    def get_all(self) -> List[Order]:
        """Obtener todos los pedidos"""
        return list(self._orders.values())