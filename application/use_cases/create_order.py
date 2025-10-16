# application/use_cases/create_order.py
"""
Caso de uso: Crear pedido.

SOLID:
- SRP: Una clase, una responsabilidad (crear pedido)
- DIP: Depende de servicios abstractos
"""

from application.services.pizza_service import PizzaService
from application.services.order_service import OrderService
from domain.entities import Order
from typing import Dict, Any, List, Optional

class CreateOrderUseCase:
    """Caso de uso: Crear un pedido de pizza"""
    
    def __init__(
        self,
        pizza_service: PizzaService,
        order_service: OrderService
    ):
        """Inyección de dependencias"""
        self._pizza_service = pizza_service
        self._order_service = order_service
    
    def execute(
        self,
        pizza_name: str,
        customer_name: str,
        size: Optional[str] = None,
        extra_toppings: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Ejecutar el caso de uso.
        
        1. Obtener pizza del menú (clonar prototipo)
        2. Personalizar si es necesario
        3. Crear el pedido
        4. Retornar resultado
        """
        # 1. Obtener pizza (Prototype Pattern en acción)
        pizza = self._pizza_service.get_pizza(pizza_name)

        # 2. Personalizar
        if size or extra_toppings:
            pizza = self._pizza_service.customize_pizza(
                pizza=pizza,
                size=size if size else pizza.size,
                extra_toppings=extra_toppings if extra_toppings else []
            )
        
        # 3. Crear pedido
        order = self._order_service.create_order(customer_name, pizza)
        
        # 4. Retornar resultado
        return {
            'success': True,
            'message': f'¡Pedido recibido, {customer_name}!',
            'order': self._order_service.order_to_dict(order)
        }