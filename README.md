# 🍕 Sistema de Pizzería - Patrón Prototype

Este proyecto es una implementación completa del **Patrón de Diseño Prototype** usando una pizzería como ejemplo práctico. El sistema demuestra cómo clonar objetos complejos pre-configurados (prototipos de pizzas) en lugar de crearlos desde cero cada vez.

## 📋 Tabla de Contenidos

- [¿Qué es el Patrón Prototype?](#qué-es-el-patrón-prototype)
- [Problema que Resuelve](#problema-que-resuelve)
- [Solución con Prototype](#solución-con-prototype)
- [Arquitectura del Proyecto](#arquitectura-del-proyecto)
- [Diagramas UML](#diagramas-uml)
- [Implementación Detallada](#implementación-detallada)
- [Principios SOLID Aplicados](#principios-solid-aplicados)
- [Instalación y Ejecución](#instalación-y-ejecución)
- [Ejemplos de Uso](#ejemplos-de-uso)

---

## 🔍 ¿Qué es el Patrón Prototype?

El **Patrón Prototype** es un patrón de diseño creacional que permite **copiar objetos existentes sin hacer que el código dependa de sus clases**. En lugar de crear objetos nuevos llamando a constructores complejos, se clonan prototipos pre-configurados.

### Características Principales:

- **Creación por Clonación**: Los objetos se crean copiando un prototipo existente
- **Independencia de Clases**: El código cliente no necesita conocer las clases concretas
- **Configuración Compleja**: Útil cuando los objetos tienen muchos parámetros de configuración
- **Performance**: Más eficiente que crear objetos complejos desde cero

---

## ❌ Problema que Resuelve

### Escenario: Pizzería sin Prototype

Imagina que cada vez que un cliente pide una pizza, debes:

```python
# ❌ SIN PROTOTYPE: Crear desde cero cada vez
def crear_pizza_margarita():
    pizza = Pizza()
    pizza.name = "Margarita"
    pizza.size = "medium"
    pizza.base = "masa tradicional"
    pizza.sauce = "tomate"
    pizza.cheese = "mozzarella"
    pizza.toppings = ["tomate fresco", "albahaca"]
    pizza.price = 8.99
    pizza.cooking_time = 12
    pizza.created_at = datetime.now()
    return pizza

def crear_pizza_pepperoni():
    pizza = Pizza()
    pizza.name = "Pepperoni"
    pizza.size = "medium"
    pizza.base = "masa tradicional"
    pizza.sauce = "tomate"
    pizza.cheese = "mozzarella"
    pizza.toppings = ["pepperoni", "orégano"]
    pizza.price = 10.99
    pizza.cooking_time = 15
    pizza.created_at = datetime.now()
    return pizza

# Mucho código repetitivo...
```

### Problemas:

1. **Código Repetitivo**: Cada tipo de pizza requiere un método constructor largo
2. **Difícil de Mantener**: Cambiar una propiedad común requiere modificar múltiples lugares
3. **Ineficiente**: Crear objetos complejos desde cero es costoso
4. **Propenso a Errores**: Fácil olvidar configurar alguna propiedad

---

## ✅ Solución con Prototype

### Con el Patrón Prototype:

```python
# ✅ CON PROTOTYPE: Clonar prototipos pre-configurados

# 1. Crear prototipos una sola vez
factory = PizzaTemplateFactory()
prototipo_margarita = factory.create_margarita()
prototipo_pepperoni = factory.create_pepperoni()

# 2. Almacenar en un registro
menu_repo = InMemoryMenuRepository()
menu_repo.register("margarita", prototipo_margarita)
menu_repo.register("pepperoni", prototipo_pepperoni)

# 3. Clonar cuando se necesite
pizza1 = menu_repo.get("margarita")  # Clona el prototipo
pizza2 = menu_repo.get("margarita")  # Otra copia independiente

# 4. Personalizar cada copia sin afectar el prototipo
pizza1.add_topping("champiñones")
pizza2.add_topping("aceitunas")
```

### Ventajas:

1. **Sin Código Repetitivo**: Los prototipos se definen una sola vez
2. **Fácil Mantenimiento**: Cambios en el prototipo afectan todas las copias futuras
3. **Eficiente**: Clonar es más rápido que crear desde cero
4. **Personalización**: Cada copia se puede modificar independientemente

---

## 🏗️ Arquitectura del Proyecto

El proyecto sigue **Clean Architecture** con separación clara de responsabilidades:

```
Prototype-pizza/
│
├── domain/                          # Capa de Dominio (Reglas de Negocio)
│   ├── entities.py                  # Entidades: Pizza, Order
│   ├── interfaces.py                # Contratos abstractos
│   └── exceptions.py                # Excepciones del dominio
│
├── application/                     # Capa de Aplicación (Casos de Uso)
│   ├── services/
│   │   ├── pizza_service.py         # Lógica de pizzas
│   │   └── order_service.py         # Lógica de pedidos
│   └── use_cases/
│       └── create_order.py          # Caso de uso: Crear pedido
│
├── infrastructure/                  # Capa de Infraestructura (Detalles)
│   ├── repositories/
│   │   ├── menu_repository.py       # Almacenamiento de prototipos
│   │   └── order_repository.py      # Almacenamiento de pedidos
│   └── templates/
│       └── pizza_templates.py       # Factory de prototipos
│
├── api/                             # Capa de Presentación (API REST)
│   ├── main.py                      # Configuración Flask
│   └── routes/
│       ├── menu_routes.py           # Endpoints del menú
│       └── order_routes.py          # Endpoints de pedidos
│
├── run.py                           # Script de ejecución
├── test_prototype.py                # Script de prueba del patrón
└── requirements.txt                 # Dependencias
```

---

## 📊 Diagramas UML

### 1. Diagrama de Clases - Patrón Prototype

```
┌──────────────────────────────────────────────────────────────┐
│                    PATRÓN PROTOTYPE                         │
└──────────────────────────────────────────────────────────────┘

┌──────────────────────┐
│   <<interface>>      │
│   PizzaPrototype     │
├──────────────────────┤
│ + clone(): Pizza     │
└──────────────────────┘
          ▲
          │ implements
          │
┌─────────────────────┴────────────────────────┐
│       Pizza          │                       │ uses
├──────────────────────┤                       │
│ - id: str            │                       │
│ - name: str          │                       │
│ - size: str          │                       │
│ - base: str          │                       │
│ - sauce: str         │                       │
│ - cheese: str        │                       │
│ - toppings: List     │                       │
│ - price: float       │                       │
│ - cooking_time: int  │                       │
│ - created_at: date   │                       │
├──────────────────────┤                       │
│ + clone(): Pizza     │◄──────────────────────┘
│ + add_topping(str)   │
└──────────────────────┘
          ▲
          │ creates
          │
┌─────────────────────┴─────────────────────────┐
│      PizzaTemplateFactory                     │
├───────────────────────────────────────────────┤
│ + create_margarita(): Pizza                   │
│ + create_pepperoni(): Pizza                   │
│ + create_hawaiana(): Pizza                    │
│ + create_four_cheese(): Pizza                 │
└───────────────────────────────────────────────┘
          │ uses
          ▼
┌────────────────────────────────────────────────┐
│    InMemoryMenuRepository                      │
├────────────────────────────────────────────────┤
│ - _templates: Dict[str, Pizza]                 │
├────────────────────────────────────────────────┤
│ + register(name, pizza): void                  │
│ + get(name): Pizza      ◄──────clones──────────┤
│ + list_all(): List[Pizza]                      │
└────────────────────────────────────────────────┘
```

### 2. Diagrama de Secuencia - Clonación de Pizza

```
Cliente          MenuRepository          Prototipo          Copia
   │                    │                    │                │
   │ get("margarita")   │                    │                │
   ├────────────────────►                    │                │
   │                    │                    │                │
   │                    │ clone()            │                │
   │                    ├────────────────────►                │
   │                    │                    │                │
   │                    │                    │  deepcopy()    │
   │                    │                    ├────────────────►
   │                    │                    │                │
   │                    │                    │  new ID        │
   │                    │                    ├────────────────►
   │                    │                    │                │
   │                    │       Pizza        │                │
   │                    ◄────────────────────┤                │
   │                    │                    │                │
   │      Pizza         │                    │                │
   ◄────────────────────┤                    │                │
   │                    │                    │                │
   │ add_topping()      │                    │                │
   ├────────────────────────────────────────────────────────► │
   │                    │                    │                │
   │                    │         (Prototipo no afectado)     │
   │                    │                    │                │
```

### 3. Diagrama de Flujo - Crear Pedido con Prototype

```
                     ┌────────────────┐
                     │  Cliente pide  │
                     │  pizza         │
                     └────────┬───────┘
                              │
                              ▼
                     ┌────────────────┐
                     │ ¿Pizza existe  │
                     │ en el menú?    │
                     └────────┬───────┘
                              │
                    ┌─────────┴─────────┐
                   NO                   SÍ
                    │                   │
                    ▼                   ▼
         ┌──────────────────┐  ┌──────────────────┐
         │ Lanzar excepción │  │ Clonar prototipo │
         │ PizzaNotFound    │  │ pizza.clone()    │
         └──────────────────┘  └────────┬─────────┘
                                        │
                                        ▼
                              ┌──────────────────┐
                              │ Generar nuevo ID │
                              │ único            │
                              └────────┬─────────┘
                                       │
                                       ▼
                              ┌──────────────────┐
                              │ ¿Personalizar?   │
                              └────────┬─────────┘
                                       │
                             ┌─────────┴────────┐
                            NO                 SÍ
                             │                  │
                             │                  ▼
                             │        ┌──────────────────┐
                             │        │ Cambiar tamaño   │
                             │        │ Agregar toppings │
                             │        │ Actualizar precio│
                             │        └────────┬─────────┘
                             │                 │
                             └────────┬────────┘
                                      │
                                      ▼
                            ┌──────────────────┐
                            │ Crear Order      │
                            │ con la pizza     │
                            └────────┬─────────┘
                                     │
                                     ▼
                            ┌──────────────────┐
                            │ Guardar pedido   │
                            │ en repositorio   │
                            └────────┬─────────┘
                                     │
                                     ▼
                            ┌──────────────────┐
                            │ Retornar pedido  │
                            │ confirmado       │
                            └──────────────────┘
```

### 4. Diagrama de Arquitectura - Clean Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                         API LAYER                           │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐            │
│  │ Flask App  │  │Menu Routes │  │Order Routes│            │
│  └──────┬─────┘  └──────┬─────┘  └──────┬─────┘            │
└─────────┼────────────────┼────────────────┼──────────────────┘
          │                │                │
          ▼                ▼                ▼
┌─────────────────────────────────────────────────────────────┐
│                   APPLICATION LAYER                         │
│  ┌────────────────┐   ┌────────────────┐                   │
│  │ PizzaService   │   │ OrderService   │                   │
│  └────────┬───────┘   └────────┬───────┘                   │
│          │                     │                            │
│          │   ┌─────────────────┴──────────┐                 │
│          └───► CreateOrderUseCase         │                 │
│              └────────────────┬───────────┘                 │
└───────────────────────────────┼─────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────┐
│                      DOMAIN LAYER                           │
│  ┌──────────┐   ┌──────────┐   ┌──────────────────┐        │
│  │  Pizza   │   │  Order   │   │  Interfaces      │        │
│  │ +clone() │   │          │   │  - MenuRepo      │        │
│  └──────────┘   └──────────┘   │  - OrderRepo     │        │
│                                 └──────────────────┘        │
└─────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────┐
│                  INFRASTRUCTURE LAYER                       │
│  ┌──────────────────────┐   ┌──────────────────────┐       │
│  │ InMemoryMenuRepo     │   │ InMemoryOrderRepo    │       │
│  │ - Prototipos         │   │ - Pedidos            │       │
│  └──────────┬───────────┘   └──────────────────────┘       │
│             │                                               │
│  ┌──────────┴───────────┐                                  │
│  │ PizzaTemplateFactory │                                  │
│  │ - create_margarita() │                                  │
│  │ - create_pepperoni() │                                  │
│  └──────────────────────┘                                  │
└─────────────────────────────────────────────────────────────┘
```

---

## 💻 Implementación Detallada

### 1. Entidad Pizza con Método Clone

```python
# domain/entities.py
from dataclasses import dataclass
from typing import List
from datetime import datetime
import copy
import uuid

@dataclass
class Pizza:
    """Entidad Pizza - Implementa el patrón Prototype"""
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

    def clone(self) -> 'Pizza':
        """
        Método clave del patrón Prototype.
        Crea una copia profunda del objeto con un nuevo ID único.
        """
        # Crear copia profunda de todos los atributos
        new_pizza = copy.deepcopy(self)

        # Generar nuevo ID único para la copia
        new_pizza.id = str(uuid.uuid4())[:8]
        new_pizza.created_at = datetime.now()

        return new_pizza

    def add_topping(self, topping: str) -> None:
        """Agregar ingrediente adicional"""
        self.toppings.append(topping)
        self.price += 1.50  # Cada ingrediente cuesta $1.50
```

**Por qué `copy.deepcopy()`?**
- **Copia Superficial**: Solo copiaría las referencias (la lista `toppings` sería compartida)
- **Copia Profunda**: Copia todos los objetos anidados (cada pizza tiene su propia lista de toppings)

### 2. Factory de Prototipos

```python
# infrastructure/templates/pizza_templates.py
from domain.entities import Pizza
from datetime import datetime

class PizzaTemplateFactory:
    """
    Factory que crea prototipos de pizzas pre-configuradas.
    Estos prototipos se clonarán cada vez que se necesiten.
    """

    @staticmethod
    def create_margarita() -> Pizza:
        """Crear prototipo de pizza Margarita"""
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
        """Crear prototipo de pizza Pepperoni"""
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
```

### 3. Repositorio de Prototipos

```python
# infrastructure/repositories/menu_repository.py
from typing import Dict, List
from domain.entities import Pizza
from infrastructure.templates.pizza_templates import PizzaTemplateFactory

class InMemoryMenuRepository:
    """
    Repositorio que almacena y clona prototipos de pizzas.
    Implementación del Registro de Prototipos.
    """

    def __init__(self):
        self._templates: Dict[str, Pizza] = {}
        self._initialize_menu()

    def _initialize_menu(self) -> None:
        """Registrar prototipos pre-configurados"""
        factory = PizzaTemplateFactory()

        # Crear y registrar prototipos
        self.register("margarita", factory.create_margarita())
        self.register("pepperoni", factory.create_pepperoni())
        self.register("hawaiana", factory.create_hawaiana())
        self.register("4quesos", factory.create_four_cheese())

    def register(self, name: str, pizza: Pizza) -> None:
        """Registrar un prototipo en el repositorio"""
        self._templates[name.lower()] = pizza

    def get(self, name: str) -> Pizza:
        """
        Obtener una COPIA del prototipo.
        ⚡ AQUÍ OCURRE LA CLONACIÓN DEL PATRÓN PROTOTYPE
        """
        name = name.lower()
        if name not in self._templates:
            raise PizzaNotFoundException(f"Pizza '{name}' no encontrada")

        # 🔑 Clonar el prototipo (no retornar el original)
        return self._templates[name].clone()

    def list_all(self) -> List[Pizza]:
        """Listar todas las pizzas (retorna copias)"""
        return [template.clone() for template in self._templates.values()]
```

### 4. Flujo Completo del Patrón

```python
# application/use_cases/create_order.py
class CreateOrderUseCase:
    """Caso de uso que utiliza el patrón Prototype"""

    def execute(
        self,
        pizza_name: str,
        customer_name: str,
        size: Optional[str] = None,
        extra_toppings: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Flujo completo:
        1. Obtener prototipo del menú (clonación automática)
        2. Personalizar la copia según las preferencias
        3. Crear el pedido con la pizza personalizada
        """

        # 1. 🔍 PATRÓN PROTOTYPE EN ACCIÓN
        #    Obtener una COPIA del prototipo
        pizza = self._pizza_service.get_pizza(pizza_name)

        # 2. Personalizar la copia (el prototipo NO se modifica)
        if size or extra_toppings:
            pizza = self._pizza_service.customize_pizza(
                pizza=pizza,
                size=size if size else pizza.size,
                extra_toppings=extra_toppings if extra_toppings else []
            )

        # 3. Crear pedido con la pizza personalizada
        order = self._order_service.create_order(customer_name, pizza)

        return {
            'success': True,
            'message': f'¡Pedido recibido, {customer_name}!',
            'order': self._order_service.order_to_dict(order)
        }
```

---

## 🎯 Principios SOLID Aplicados

### 1. **S - Single Responsibility Principle**

Cada clase tiene una única responsabilidad:

- `Pizza`: Representa una entidad de pizza y sus reglas de negocio
- `PizzaTemplateFactory`: Solo crea prototipos de pizzas
- `InMemoryMenuRepository`: Solo almacena y clona prototipos
- `PizzaService`: Solo operaciones de lógica de pizzas
- `CreateOrderUseCase`: Solo el flujo de crear un pedido

### 2. **O - Open/Closed Principle**

El código está abierto para extensión, cerrado para modificación:

```python
# ✅ Agregar nueva pizza sin modificar código existente
class PizzaTemplateFactory:
    # Métodos existentes...

    @staticmethod
    def create_vegetariana() -> Pizza:  # ✅ Nueva pizza
        return Pizza(...)
```

### 3. **L - Liskov Substitution Principle**

Las implementaciones pueden sustituir a sus abstracciones:

```python
# Puedes cambiar la implementación sin romper el código
menu_repo: MenuRepository = InMemoryMenuRepository()
# O más tarde:
menu_repo: MenuRepository = DatabaseMenuRepository()
```

### 4. **I - Interface Segregation Principle**

Interfaces específicas y cohesivas:

```python
class MenuRepository(ABC):
    """Interfaz enfocada solo en operaciones del menú"""
    @abstractmethod
    def register(self, name: str, pizza: Pizza) -> None: pass

    @abstractmethod
    def get(self, name: str) -> Pizza: pass

class OrderRepository(ABC):
    """Interfaz separada para pedidos"""
    @abstractmethod
    def save(self, order: Order) -> None: pass
```

### 5. **D - Dependency Inversion Principle**

Dependemos de abstracciones, no de implementaciones concretas:

```python
class PizzaService:
    def __init__(self, menu_repository: MenuRepository):
        # ⚡ Depende de la abstracción MenuRepository
        #    NO de InMemoryMenuRepository
        self._menu_repo = menu_repository
```

---

## 🚀 Instalación y Ejecución

### Requisitos Previos

- Python 3.11+
- pip

### Instalación

```bash
# 1. Clonar o descargar el proyecto
cd Prototype-pizza

# 2. Instalar dependencias
pip install -r requirements.txt
```

### Ejecutar la API

```bash
# Opción 1: Usando run.py
python run.py

# Opción 2: Usando el módulo api
python -m api.main
```

La API estará disponible en: `http://localhost:5000`

### Ejecutar Script de Prueba

```bash
python test_prototype.py
```

---

## 📝 Ejemplos de Uso

### 1. Script de Prueba del Patrón

```python
from infrastructure.repositories.menu_repository import InMemoryMenuRepository

# Crear repositorio con prototipos
menu_repo = InMemoryMenuRepository()

# Clonar prototipo
pizza1 = menu_repo.get("margarita")
print(f"Pizza: {pizza1.name}, ID: {pizza1.id}")

# Clonar otra vez (diferente instancia)
pizza2 = menu_repo.get("margarita")
print(f"Pizza: {pizza2.name}, ID: {pizza2.id}")

# Verificar que son independientes
print(f"Mismo objeto? {pizza1 is pizza2}")  # False
print(f"Mismo ID? {pizza1.id == pizza2.id}")  # False

# Modificar una copia sin afectar la otra
pizza1.add_topping("champiñones")
print(f"Pizza1: {pizza1.toppings}")  # ['tomate fresco', 'albahaca', 'champiñones']
print(f"Pizza2: {pizza2.toppings}")  # ['tomate fresco', 'albahaca']
```

### 2. Usando la API REST

#### Ver el Menú

```bash
curl http://localhost:5000/menu
```

**Respuesta:**
```json
{
  "success": true,
  "pizzas": [
    {
      "id": "abc123",
      "name": "Margarita",
      "size": "medium",
      "toppings": ["tomate fresco", "albahaca"],
      "price": 8.99,
      "cooking_time": 12
    },
    {
      "id": "def456",
      "name": "Pepperoni",
      "size": "medium",
      "toppings": ["pepperoni", "orégano"],
      "price": 10.99,
      "cooking_time": 15
    }
  ]
}
```

#### Crear un Pedido

```bash
curl -X POST http://localhost:5000/order \
  -H "Content-Type: application/json" \
  -d '{
    "pizza_name": "margarita",
    "customer_name": "Juan Pérez",
    "size": "large",
    "extra_toppings": ["champiñones", "aceitunas"]
  }'
```

**Respuesta:**
```json
{
  "success": true,
  "message": "¡Pedido recibido, Juan Pérez!",
  "order": {
    "order_id": "xyz789",
    "customer_name": "Juan Pérez",
    "pizza": {
      "id": "new123",
      "name": "Margarita",
      "size": "large",
      "toppings": ["tomate fresco", "albahaca", "champiñones", "aceitunas"],
      "price": 16.49,
      "cooking_time": 12
    },
    "status": "preparando",
    "ordered_at": "2025-01-10T14:30:00"
  }
}
```

#### Ver un Pedido

```bash
curl http://localhost:5000/order/xyz789
```

---

## ⚖️ Comparación: Con vs Sin Prototype

### ❌ Sin Patrón Prototype

```python
# Crear pizza desde cero cada vez
def crear_pedido_margarita():
    pizza = Pizza()
    pizza.id = generar_id()
    pizza.name = "Margarita"
    pizza.size = "medium"
    pizza.base = "masa tradicional"
    pizza.sauce = "tomate"
    pizza.cheese = "mozzarella"
    pizza.toppings = ["tomate fresco", "albahaca"]
    pizza.price = 8.99
    pizza.cooking_time = 12
    pizza.created_at = datetime.now()
    return Order(pizza=pizza, ...)

# Problemas:
# - 13 líneas de código repetitivo
# - Fácil olvidar configurar algo
# - Difícil mantener consistencia
# - Ineficiente (crear desde cero)
```

### ✅ Con Patrón Prototype

```python
# Clonar prototipo pre-configurado
def crear_pedido_margarita():
    pizza = menu_repo.get("margarita")  # 1 línea, clona el prototipo
    return Order(pizza=pizza, ...)

# Ventajas:
# - 1 línea de código
# - Imposible olvidar configuración
# - Consistencia garantizada
# - Eficiente (clonar es rápido)
# - Fácil personalizar después
```

---

## 💡 Cuándo Usar el Patrón Prototype

### ✅ Úsalo Cuando:

1. **Objetos Complejos**: Tus objetos tienen muchas propiedades y configuración compleja
2. **Configuraciones Estándar**: Tienes variantes pre-definidas (como pizzas del menú)
3. **Clonación Frecuente**: Necesitas crear muchas instancias similares
4. **Performance**: Crear desde cero es costoso (ej: conexiones a BD, objetos complejos)
5. **Personalización**: Necesitas variantes de objetos base

### ❌ No lo Uses Cuando:

1. **Objetos Simples**: Si tu objeto tiene 2-3 propiedades, un constructor simple es mejor
2. **Objetos Únicos**: Si cada instancia es completamente diferente
3. **Sin Estado Base**: Si no hay una configuración "estándar" para clonar
4. **Referencias Compartidas**: Si necesitas que objetos compartan estado (entonces no clones)

---

## 🧪 Testing

El proyecto incluye un script de prueba completo:

```bash
python test_prototype.py
```

**Salida esperada:**
```
============================================================
PRUEBA DEL PATRON PROTOTYPE
============================================================

1. Inicializando repositorio con prototipos...
   - Prototipos registrados: Margarita, Pepperoni, Hawaiana, 4 Quesos

2. Clonando el prototipo 'Margarita'...
   - Pizza clonada: Margarita
   - ID: 0627937a
   - Precio: $8.99
   - Toppings: ['tomate fresco', 'albahaca']

3. Clonando nuevamente el prototipo 'Margarita'...
   - Pizza clonada: Margarita
   - ID: 5a44e486
   - Precio: $8.99
   - Toppings: ['tomate fresco', 'albahaca']

4. Verificando que son objetos independientes...
   - Son el mismo objeto? False
   - Tienen el mismo ID? False
   - Tienen el mismo nombre? True

5. Personalizando pizza1 (agregando champinones)...
   - Pizza1 toppings: ['tomate fresco', 'albahaca', 'champinones']
   - Pizza1 precio: $8.99 -> $10.49
   - Pizza2 toppings: ['tomate fresco', 'albahaca']
   - Pizza2 precio: $8.99
   - Pizza2 fue afectada? NO (son objetos independientes)

============================================================
PATRON PROTOTYPE FUNCIONANDO CORRECTAMENTE
============================================================
```

---

## 📚 Referencias

- **Libro**: "Design Patterns: Elements of Reusable Object-Oriented Software" (Gang of Four)
- **Patrón**: Prototype (Creational Pattern)
- **Arquitectura**: Clean Architecture by Robert C. Martin
- **Principios**: SOLID Principles

---

## 👨‍💻 Autor

Este proyecto fue creado como ejemplo educativo del **Patrón de Diseño Prototype** aplicando **Clean Architecture** y **Principios SOLID**.

---

## 📜 Licencia

Este proyecto es de código abierto y está disponible para fines educativos.

---

## 🎓 Conclusión

Este proyecto demuestra:

1. ✅ **Patrón Prototype**: Clonación eficiente de objetos complejos
2. ✅ **Clean Architecture**: Separación clara de responsabilidades
3. ✅ **SOLID**: Código mantenible y extensible
4. ✅ **Best Practices**: Código profesional y bien documentado

El patrón Prototype es especialmente útil cuando:
- Tienes objetos con configuración compleja
- Necesitas crear muchas variantes de objetos base
- Quieres evitar código repetitivo de inicialización
- La performance de creación de objetos es importante

**¡El código está listo para usar y aprender!** 🚀
