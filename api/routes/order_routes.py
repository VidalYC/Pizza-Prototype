# api/routes/order_routes.py
"""
Rutas de pedidos.

SOLID:
- SRP: Solo maneja endpoints de pedidos
- DIP: Depende de casos de uso inyectados
"""

from flask import Blueprint, request, jsonify
from application.use_cases.create_order import CreateOrderUseCase
from application.services.order_service import OrderService
from domain.exceptions import PizzaNotFoundException

def create_order_routes(
    create_order_use_case: CreateOrderUseCase,
    order_service: OrderService
) -> Blueprint:
    """Factory de rutas de pedidos"""
    
    order_bp = Blueprint('orders', __name__, url_prefix='/order')
    
    @order_bp.route('/', methods=['POST'])
    def create_order():
        """POST /order - Crear pedido"""
        try:
            data = request.get_json()
            
            # Validaciones
            if 'pizza' not in data:
                return jsonify({
                    'success': False,
                    'error': 'Pizza es requerida'
                }), 400
            
            if 'customer_name' not in data:
                return jsonify({
                    'success': False,
                    'error': 'Nombre del cliente es requerido'
                }), 400
            
            # Ejecutar caso de uso
            result = create_order_use_case.execute(
                pizza_name=data['pizza'],
                customer_name=data['customer_name'],
                size=data.get('size'),
                extra_toppings=data.get('extra_toppings')
            )
            
            return jsonify(result), 201
            
        except PizzaNotFoundException as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 404
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500
    
    @order_bp.route('/<order_id>', methods=['GET'])
    def get_order(order_id: str):
        """GET /order/<id> - Obtener pedido"""
        try:
            order = order_service.get_order(order_id)
            return jsonify({
                'success': True,
                'order': order_service.order_to_dict(order)
            }), 200
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 404
    
    return order_bp