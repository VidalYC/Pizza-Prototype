# domain/entities.py
"""
Entidades puras del dominio.
No dependen de nada externo.

SOLID:
- SRP: Cada entidad tiene una responsabilidad clara
- OCP: Abierto para extensión (herencia)
"""

from dataclasses import dataclass
from typing import List
from datetime import datetime
import uuid
import copy

@dataclass
class Pizza:
    """Entidad Pizza - Reglas de negocio puras"""
    id: str
    name: str
    size: str
    base: str
    sauce: str
    cheese: str
    toppings: List[str]
    price: float
    cooking_time: int
    created_at: datetime

    def __post_init__(self):
        if not self.id:
            self.id = str(uuid.uuid4())[:8]
        if not self.created_at:
            self.created_at = datetime.now()

    def clone(self) -> 'Pizza':
        """
        Método clone para el patrón Prototype.
        Crea una copia profunda de la pizza con un nuevo ID.
        """
        # Crear una copia profunda del objeto
        new_pizza = copy.deepcopy(self)
        # Generar un nuevo ID único para la copia
        new_pizza.id = str(uuid.uuid4())[:8]
        new_pizza.created_at = datetime.now()
        return new_pizza

    def add_topping(self, topping: str) -> None:
        """Regla de negocio: agregar ingrediente"""
        self.toppings.append(topping)
        self.price += 1.50  # Cada ingrediente cuesta $1.50


@dataclass
class Order:
    """Entidad Order - Representa un pedido"""
    order_id: str
    customer_name: str
    pizza: Pizza
    status: str
    ordered_at: datetime
    
    def __post_init__(self):
        if not self.order_id:
            self.order_id = str(uuid.uuid4())[:8]
        if not self.ordered_at:
            self.ordered_at = datetime.now()