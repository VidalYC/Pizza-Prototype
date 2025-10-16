# api/routes/menu_routes.py
"""
Rutas del menú.

SOLID:
- SRP: Solo maneja endpoints del menú
- DIP: Depende de servicios inyectados
"""

from flask import Blueprint, jsonify
from application.services.pizza_service import PizzaService

def create_menu_routes(pizza_service: PizzaService) -> Blueprint:
    """Factory de rutas del menú"""
    
    menu_bp = Blueprint('menu', __name__, url_prefix='/menu')
    
    @menu_bp.route('/', methods=['GET'])
    def get_menu():
        """GET /menu - Obtener menú completo"""
        try:
            menu = pizza_service.get_menu()
            return jsonify({
                'success': True,
                'menu': menu,
                'total': len(menu)
            }), 200
        except Exception as e:
            return jsonify({
                'success': False,
                'error': str(e)
            }), 500
    
    return menu_bp