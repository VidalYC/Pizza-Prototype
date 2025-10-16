# application/services/order_service.py
"""
Servicio de pedidos (lógica de aplicación).

SOLID:
- SRP: Solo gestiona operaciones con pedidos
- DIP: Depende de interfaces
"""

from typing import Dict, Any, Optional
from domain.interfaces import OrderRepository
from domain.entities import Order, Pizza
from domain.exceptions import OrderNotFoundException
import uuid
from datetime import datetime

class OrderService:
    """Servicio para operaciones con pedidos"""
    
    def __init__(self, order_repository: OrderRepository):
        """Inyección de dependencias"""
        self._order_repo = order_repository
    
    def create_order(self, customer_name: str, pizza: Pizza) -> Order:
        """Crear un nuevo pedido"""
        # Generar nuevo ID para la pizza del pedido
        pizza.id = str(uuid.uuid4())[:8]
        
        # Crear entidad Order
        order = Order(
            order_id=str(uuid.uuid4())[:8],
            customer_name=customer_name,
            pizza=pizza,
            status="preparando",
            ordered_at=datetime.now()
        )
        
        # Guardar en el repositorio
        self._order_repo.save(order)
        
        return order
    
    def get_order(self, order_id: str) -> Order:
        """Obtener un pedido por ID"""
        order = self._order_repo.get_by_id(order_id)
        if order is None:
            raise OrderNotFoundException(f"Pedido '{order_id}' no encontrado")
        return order
    
    def order_to_dict(self, order: Order) -> Dict[str, Any]:
        """Convertir orden a diccionario"""
        return {
            'order_id': order.order_id,
            'customer_name': order.customer_name,
            'pizza': {
                'id': order.pizza.id,
                'name': order.pizza.name,
                'size': order.pizza.size,
                'toppings': order.pizza.toppings,
                'price': order.pizza.price,
                'cooking_time': order.pizza.cooking_time
            },
            'status': order.status,
            'ordered_at': order.ordered_at.isoformat()
        }