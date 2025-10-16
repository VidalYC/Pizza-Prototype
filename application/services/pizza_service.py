# application/services/pizza_service.py
"""
Servicio de pizzas (lógica de aplicación).

SOLID:
- SRP: Solo gestiona operaciones relacionadas con pizzas
- DIP: Depende de interfaces, no de implementaciones
"""

from typing import List, Dict, Any
from domain.interfaces import MenuRepository
from domain.entities import Pizza

class PizzaService:
    """Servicio para operaciones con pizzas"""
    
    def __init__(self, menu_repository: MenuRepository):
        """
        Inyección de dependencias (DIP)
        
        No dependemos de InMemoryMenuRepository específicamente,
        sino de la interfaz MenuRepository
        """
        self._menu_repo = menu_repository
    
    def get_menu(self) -> List[Dict[str, Any]]:
        """Obtener menú completo"""
        pizzas = self._menu_repo.list_all()
        return [self._pizza_to_dict(pizza) for pizza in pizzas]
    
    def get_pizza(self, name: str) -> Pizza:
        """Obtener una pizza específica (copia del prototipo)"""
        return self._menu_repo.get(name)
    
    def customize_pizza(
        self,
        pizza: Pizza,
        size: str,
        extra_toppings: List[str]
    ) -> Pizza:
        """Personalizar una pizza"""
        # Cambiar tamaño
        if size:
            self._adjust_size(pizza, size)

        # Agregar ingredientes extra
        if extra_toppings:
            for topping in extra_toppings:
                pizza.add_topping(topping)

        return pizza
    
    def _adjust_size(self, pizza: Pizza, size: str) -> None:
        """Ajustar tamaño y precio"""
        pizza.size = size
        if size == "large":
            pizza.price *= 1.5
        elif size == "small":
            pizza.price *= 0.75
    
    def _pizza_to_dict(self, pizza: Pizza) -> Dict[str, Any]:
        """Convertir pizza a diccionario"""
        return {
            'id': pizza.id,
            'name': pizza.name,
            'size': pizza.size,
            'toppings': pizza.toppings,
            'price': pizza.price,
            'cooking_time': pizza.cooking_time
        }