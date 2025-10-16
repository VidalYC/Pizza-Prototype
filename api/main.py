# api/main.py
"""
Punto de entrada de la API.
Configuración de dependencias (Dependency Injection Container).

SOLID:
- DIP: Inyección de dependencias manual (o usar un container)
- OCP: Fácil cambiar implementaciones sin tocar lógica de negocio
"""

from flask import Flask, jsonify
from flask_cors import CORS

# Repositories (Infraestructura)
from infrastructure.repositories.menu_repository import InMemoryMenuRepository
from infrastructure.repositories.order_repository import InMemoryOrderRepository

# Services (Aplicación)
from application.services.pizza_service import PizzaService
from application.services.order_service import OrderService

# Use Cases (Aplicación)
from application.use_cases.create_order import CreateOrderUseCase

# Routes (API)
from api.routes.menu_routes import create_menu_routes
from api.routes.order_routes import create_order_routes

def create_app() -> Flask:
    """
    Factory de la aplicación Flask.
    Aquí configuramos todas las dependencias (DI Container manual).
    """
    app = Flask(__name__)
    CORS(app)
    
    # ============================================
    # DEPENDENCY INJECTION CONTAINER
    # ============================================
    
    # 1. Crear repositorios (capa más baja)
    menu_repo = InMemoryMenuRepository()
    order_repo = InMemoryOrderRepository()
    
    # 2. Crear servicios (inyectar repositorios)
    pizza_service = PizzaService(menu_repo)
    order_service = OrderService(order_repo)
    
    # 3. Crear casos de uso (inyectar servicios)
    create_order_use_case = CreateOrderUseCase(pizza_service, order_service)
    
    # 4. Crear rutas (inyectar casos de uso y servicios)
    menu_bp = create_menu_routes(pizza_service)
    order_bp = create_order_routes(create_order_use_case, order_service)
    
    # 5. Registrar blueprints
    app.register_blueprint(menu_bp)
    app.register_blueprint(order_bp)
    
    # ============================================
    # RUTAS GENERALES
    # ============================================
    
    @app.route('/', methods=['GET'])
    def home():
        return jsonify({
            'message': '🍕 Pizzería API con SOLID',
            'endpoints': {
                'GET /menu': 'Ver menú',
                'POST /order': 'Crear pedido',
                'GET /order/<id>': 'Ver pedido'
            }
        })
    
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 'Endpoint no encontrado'
        }), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({
            'success': False,
            'error': 'Error interno del servidor'
        }), 500
    
    return app


if __name__ == '__main__':
    app = create_app()
    print("\n" + "="*60)
    print("🍕 PIZZERÍA API CON SOLID Y CLEAN ARCHITECTURE")
    print("="*60)
    print("\nServidor en: http://localhost:5000")
    print("="*60 + "\n")
    app.run(debug=True, port=5000)