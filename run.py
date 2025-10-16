# run.py (Script de ejecución)
"""
Script para ejecutar la API.
"""

from api.main import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)