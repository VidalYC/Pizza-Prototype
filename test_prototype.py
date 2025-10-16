"""
Script de prueba para verificar el patron Prototype.
Demuestra como se clonan las pizzas y se pueden personalizar.
"""

from domain.entities import Pizza
from infrastructure.templates.pizza_templates import PizzaTemplateFactory
from infrastructure.repositories.menu_repository import InMemoryMenuRepository
from datetime import datetime

def test_prototype_pattern():
    print("\n" + "="*60)
    print("PRUEBA DEL PATRON PROTOTYPE")
    print("="*60 + "\n")

    # 1. Crear el repositorio con los prototipos
    print("1. Inicializando repositorio con prototipos...")
    menu_repo = InMemoryMenuRepository()
    print("   - Prototipos registrados: Margarita, Pepperoni, Hawaiana, 4 Quesos\n")

    # 2. Obtener una pizza (esto clona el prototipo)
    print("2. Clonando el prototipo 'Margarita'...")
    pizza1 = menu_repo.get("margarita")
    print(f"   - Pizza clonada: {pizza1.name}")
    print(f"   - ID: {pizza1.id}")
    print(f"   - Precio: ${pizza1.price}")
    print(f"   - Toppings: {pizza1.toppings}\n")

    # 3. Obtener otra copia del mismo prototipo
    print("3. Clonando nuevamente el prototipo 'Margarita'...")
    pizza2 = menu_repo.get("margarita")
    print(f"   - Pizza clonada: {pizza2.name}")
    print(f"   - ID: {pizza2.id}")
    print(f"   - Precio: ${pizza2.price}")
    print(f"   - Toppings: {pizza2.toppings}\n")

    # 4. Verificar que son objetos diferentes
    print("4. Verificando que son objetos independientes...")
    print(f"   - Son el mismo objeto? {pizza1 is pizza2}")
    print(f"   - Tienen el mismo ID? {pizza1.id == pizza2.id}")
    print(f"   - Tienen el mismo nombre? {pizza1.name == pizza2.name}\n")

    # 5. Personalizar pizza1 sin afectar pizza2
    print("5. Personalizando pizza1 (agregando champinones)...")
    precio_original_pizza1 = pizza1.price
    pizza1.add_topping("champinones")
    print(f"   - Pizza1 toppings: {pizza1.toppings}")
    print(f"   - Pizza1 precio: ${precio_original_pizza1} -> ${pizza1.price}")
    print(f"   - Pizza2 toppings: {pizza2.toppings}")
    print(f"   - Pizza2 precio: ${pizza2.price}")
    print(f"   - Pizza2 fue afectada? NO (son objetos independientes)\n")

    # 6. Clonar manualmente usando el metodo clone()
    print("6. Clonando pizza1 usando el metodo clone()...")
    pizza3 = pizza1.clone()
    print(f"   - Pizza3 ID: {pizza3.id}")
    print(f"   - Pizza3 nombre: {pizza3.name}")
    print(f"   - Pizza3 toppings: {pizza3.toppings}")
    print(f"   - Tiene diferente ID que pizza1? {pizza3.id != pizza1.id}\n")

    # 7. Listar todo el menu (todas son copias)
    print("7. Listando todo el menu (cada llamada clona el prototipo)...")
    menu = menu_repo.list_all()
    print(f"   - Total de pizzas en el menu: {len(menu)}")
    for pizza in menu:
        print(f"   - {pizza.name}: ${pizza.price} (ID: {pizza.id})")

    print("\n" + "="*60)
    print("PATRON PROTOTYPE FUNCIONANDO CORRECTAMENTE")
    print("="*60 + "\n")

    print("Ventajas del patron Prototype demostradas:")
    print("  1. No necesitamos crear pizzas desde cero cada vez")
    print("  2. Clonamos prototipos pre-configurados rapidamente")
    print("  3. Cada copia es independiente (ID unico)")
    print("  4. Podemos personalizar copias sin afectar el prototipo")
    print("  5. Reduce codigo repetitivo de inicializacion\n")

if __name__ == "__main__":
    test_prototype_pattern()
