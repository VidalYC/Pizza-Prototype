# infrastructure/repositories/menu_repository.py
"""
Implementación concreta del repositorio de menú.

SOLID:
- SRP: Solo gestiona el menú de pizzas
- DIP: Implementa la interfaz MenuRepository
- LSP: Puede sustituir a MenuRepository sin problemas
"""

from typing import Dict, List
from domain.interfaces import MenuRepository
from domain.entities import Pizza
from domain.exceptions import PizzaNotFoundException
from infrastructure.templates.pizza_templates import PizzaTemplateFactory

class InMemoryMenuRepository(MenuRepository):
    """Repositorio de menú en memoria"""
    
    def __init__(self):
        self._templates: Dict[str, Pizza] = {}
        self._initialize_menu()
    
    def _initialize_menu(self) -> None:
        """Inicializar con templates por defecto"""
        factory = PizzaTemplateFactory()
        
        self.register("margarita", factory.create_margarita())
        self.register("pepperoni", factory.create_pepperoni())
        self.register("hawaiana", factory.create_hawaiana())
        self.register("4quesos", factory.create_four_cheese())
    
    def register(self, name: str, pizza: Pizza) -> None:
        """Registrar un template"""
        self._templates[name.lower()] = pizza
    
    def get(self, name: str) -> Pizza:
        """Obtener una copia de la pizza"""
        name = name.lower()
        if name not in self._templates:
            raise PizzaNotFoundException(f"Pizza '{name}' no encontrada")
        
        # Retornar copia (Prototype Pattern)
        return self._templates[name].clone()
    
    def list_all(self) -> List[Pizza]:
        """Listar todas las pizzas (copias)"""
        return [template.clone() for template in self._templates.values()]