from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

# Simular base de datos con archivos JSON (para simplicidad, en producción usar SQL)
DB_FILE = 'db.json'

def load_db():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r') as f:
            return json.load(f)
    return {
        'productos': [],
        'ventas': [],
        'compras': [],
        'pedidos': [],
        'rifas': [],
        'facturas': [],
        'reportes': []
    }

def save_db(db):
    with open(DB_FILE, 'w') as f:
        json.dump(db, f, indent=4)

@app.route('/')
def index():
    return "Backend de Gestión de Inventario - Accesorios García"

# CRUD para Productos
@app.route('/productos', methods=['GET'])
def get_productos():
    db = load_db()
    return jsonify(db['productos'])

@app.route('/productos', methods=['POST'])
def add_producto():
    db = load_db()
    producto = request.json
    db['productos'].append(producto)
    save_db(db)
    return jsonify({'message': 'Producto agregado'}), 201

@app.route('/productos/<int:id>', methods=['PUT'])
def update_producto(id):
    db = load_db()
    if id < len(db['productos']):
        db['productos'][id] = request.json
        save_db(db)
        return jsonify({'message': 'Producto actualizado'})
    return jsonify({'error': 'Producto no encontrado'}), 404

@app.route('/productos/<int:id>', methods=['DELETE'])
def delete_producto(id):
    db = load_db()
    if id < len(db['productos']):
        db['productos'].pop(id)
        save_db(db)
        return jsonify({'message': 'Producto eliminado'})
    return jsonify({'error': 'Producto no encontrado'}), 404

# CRUD para Ventas
@app.route('/ventas', methods=['GET'])
def get_ventas():
    db = load_db()
    return jsonify(db['ventas'])

@app.route('/ventas', methods=['POST'])
def add_venta():
    db = load_db()
    venta = request.json
    db['ventas'].append(venta)
    save_db(db)
    return jsonify({'message': 'Venta agregada'}), 201

@app.route('/ventas/<int:id>', methods=['PUT'])
def update_venta(id):
    db = load_db()
    if id < len(db['ventas']):
        db['ventas'][id] = request.json
        save_db(db)
        return jsonify({'message': 'Venta actualizada'})
    return jsonify({'error': 'Venta no encontrada'}), 404

@app.route('/ventas/<int:id>', methods=['DELETE'])
def delete_venta(id):
    db = load_db()
    if id < len(db['ventas']):
        db['ventas'].pop(id)
        save_db(db)
        return jsonify({'message': 'Venta eliminada'})
    return jsonify({'error': 'Venta no encontrada'}), 404

# CRUD para Compras
@app.route('/compras', methods=['GET'])
def get_compras():
    db = load_db()
    return jsonify(db['compras'])

@app.route('/compras', methods=['POST'])
def add_compra():
    db = load_db()
    compra = request.json
    db['compras'].append(compra)
    save_db(db)
    return jsonify({'message': 'Compra agregada'}), 201

@app.route('/compras/<int:id>', methods=['PUT'])
def update_compra(id):
    db = load_db()
    if id < len(db['compras']):
        db['compras'][id] = request.json
        save_db(db)
        return jsonify({'message': 'Compra actualizada'})
    return jsonify({'error': 'Compra no encontrada'}), 404

@app.route('/compras/<int:id>', methods=['DELETE'])
def delete_compra(id):
    db = load_db()
    if id < len(db['compras']):
        db['compras'].pop(id)
        save_db(db)
        return jsonify({'message': 'Compra eliminada'})
    return jsonify({'error': 'Compra no encontrada'}), 404

# CRUD para Pedidos (ya existente, pero integrado)
@app.route('/pedidos', methods=['GET'])
def get_pedidos():
    db = load_db()
    return jsonify(db['pedidos'])

@app.route('/pedidos', methods=['POST'])
def add_pedido():
    db = load_db()
    pedido = request.json
    db['pedidos'].append(pedido)
    save_db(db)
    return jsonify({'message': 'Pedido agregado'}), 201

@app.route('/pedidos/<int:id>', methods=['PUT'])
def update_pedido(id):
    db = load_db()
    if id < len(db['pedidos']):
        db['pedidos'][id] = request.json
        save_db(db)
        return jsonify({'message': 'Pedido actualizado'})
    return jsonify({'error': 'Pedido no encontrado'}), 404

@app.route('/pedidos/<int:id>', methods=['DELETE'])
def delete_pedido(id):
    db = load_db()
    if id < len(db['pedidos']):
        db['pedidos'].pop(id)
        save_db(db)
        return jsonify({'message': 'Pedido eliminado'})
    return jsonify({'error': 'Pedido no encontrado'}), 404

# CRUD para Rifas
@app.route('/rifas', methods=['GET'])
def get_rifas():
    db = load_db()
    return jsonify(db['rifas'])

@app.route('/rifas', methods=['POST'])
def add_rifa():
    db = load_db()
    rifa = request.json
    db['rifas'].append(rifa)
    save_db(db)
    return jsonify({'message': 'Rifa agregada'}), 201

@app.route('/rifas/<int:id>', methods=['PUT'])
def update_rifa(id):
    db = load_db()
    if id < len(db['rifas']):
        db['rifas'][id] = request.json
        save_db(db)
        return jsonify({'message': 'Rifa actualizada'})
    return jsonify({'error': 'Rifa no encontrada'}), 404

@app.route('/rifas/<int:id>', methods=['DELETE'])
def delete_rifa(id):
    db = load_db()
    if id < len(db['rifas']):
        db['rifas'].pop(id)
        save_db(db)
        return jsonify({'message': 'Rifa eliminada'})
    return jsonify({'error': 'Rifa no encontrada'}), 404

# Facturación (generar facturas)
@app.route('/facturas', methods=['GET'])
def get_facturas():
    db = load_db()
    return jsonify(db['facturas'])

@app.route('/facturas', methods=['POST'])
def add_factura():
    db = load_db()
    factura = request.json
    db['facturas'].append(factura)
    save_db(db)
    return jsonify({'message': 'Factura generada'}), 201

# Reportes (datos para gráficos)
@app.route('/reportes', methods=['GET'])
def get_reportes():
    db = load_db()
    # Calcular datos para reportes
    ventas_total = sum(v.get('total', 0) for v in db['ventas'])
    compras_total = sum(c.get('total', 0) for c in db['compras'])
    pedidos_pendientes = sum(p.get('total', 0) - p.get('pagado', 0) for p in db['pedidos'])
    productos_stock = len([p for p in db['productos'] if p.get('tipo') == 'entrada'])
    return jsonify({
        'ventas_total': ventas_total,
        'compras_total': compras_total,
        'pedidos_pendientes': pedidos_pendientes,
        'productos_stock': productos_stock
    })

if __name__ == '__main__':
    app.run(debug=True)
