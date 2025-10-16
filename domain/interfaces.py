# domain/interfaces.py
"""
Interfaces abstractas (contratos).
Define CÓMO deben comportarse las implementaciones.

SOLID:
- DIP: Dependemos de abstracciones, no de implementaciones
- ISP: Interfaces específicas y cohesivas
"""

from abc import ABC, abstractmethod
from typing import List, Optional
from domain.entities import Pizza, Order

class PizzaPrototype(ABC):
    """Interfaz para prototipos de pizza"""
    
    @abstractmethod
    def clone(self) -> Pizza:
        """Clonar el prototipo"""
        pass


class MenuRepository(ABC):
    """Interfaz para el repositorio de menú"""
    
    @abstractmethod
    def register(self, name: str, pizza: Pizza) -> None:
        """Registrar una pizza en el menú"""
        pass
    
    @abstractmethod
    def get(self, name: str) -> Pizza:
        """Obtener una pizza del menú (copia)"""
        pass
    
    @abstractmethod
    def list_all(self) -> List[Pizza]:
        """Listar todas las pizzas"""
        pass


class OrderRepository(ABC):
    """Interfaz para el repositorio de pedidos"""
    
    @abstractmethod
    def save(self, order: Order) -> None:
        """Guardar un pedido"""
        pass
    
    @abstractmethod
    def get_by_id(self, order_id: str) -> Optional[Order]:
        """Obtener un pedido por ID"""
        pass
    
    @abstractmethod
    def get_all(self) -> List[Order]:
        """Obtener todos los pedidos"""
        pass