# infrastructure/templates/pizza_templates.py
"""
Factory para crear prototipos de pizzas pre-configuradas.

SOLID:
- SRP: Cada método crea un tipo específico de pizza
- OCP: Fácil agregar nuevos templates sin modificar existentes

Patrón Prototype:
- Los objetos Pizza creados aquí actúan como prototipos
- Se clonarán usando pizza.clone() cuando se necesiten
"""

from domain.entities import Pizza
from datetime import datetime

class PizzaTemplateFactory:
    """
    Factory para crear prototipos de pizzas pre-configurados.

    Estos prototipos se almacenan en el repositorio y se clonan
    cada vez que un cliente pide una pizza.
    """

    @staticmethod
    def create_margarita() -> Pizza:
        """Crear prototipo de Margarita"""
        return Pizza(
            id="",
            name="Margarita",
            size="medium",
            base="masa tradicional",
            sauce="tomate",
            cheese="mozzarella",
            toppings=["tomate fresco", "albahaca"],
            price=8.99,
            cooking_time=12,
            created_at=datetime.now()
        )

    @staticmethod
    def create_pepperoni() -> Pizza:
        """Crear prototipo de Pepperoni"""
        return Pizza(
            id="",
            name="Pepperoni",
            size="medium",
            base="masa tradicional",
            sauce="tomate",
            cheese="mozzarella",
            toppings=["pepperoni", "orégano"],
            price=10.99,
            cooking_time=15,
            created_at=datetime.now()
        )

    @staticmethod
    def create_hawaiana() -> Pizza:
        """Crear prototipo de Hawaiana"""
        return Pizza(
            id="",
            name="Hawaiana",
            size="medium",
            base="masa tradicional",
            sauce="tomate",
            cheese="mozzarella",
            toppings=["jamón", "piña"],
            price=11.99,
            cooking_time=15,
            created_at=datetime.now()
        )

    @staticmethod
    def create_four_cheese() -> Pizza:
        """Crear prototipo de 4 Quesos"""
        return Pizza(
            id="",
            name="4 Quesos",
            size="medium",
            base="masa tradicional",
            sauce="tomate",
            cheese="mezcla de 4 quesos",
            toppings=["gorgonzola", "parmesano", "provolone"],
            price=13.99,
            cooking_time=14,
            created_at=datetime.now()
        )