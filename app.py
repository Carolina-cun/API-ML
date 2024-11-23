from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Definir la URL base de la API de Mercado Libre
MERCADO_LIBRE_BASE_URL = "https://api.mercadolibre.com"

# Función para hacer la petición a Mercado Libre
def get_from_mercadolibre(endpoint): #metodo 
    url = f"{MERCADO_LIBRE_BASE_URL}{endpoint}" #armar url el servidor + el endpoint
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Error {response.status_code}: {response.text}"}

# 1. Endpoint para obtener ítems por categoría
@app.route('/api/items_by_category', methods=['GET'])
def items_by_category():
    category_id = request.args.get('category_id')
    if not category_id:
        return jsonify({"error": "category_id es obligatorio"}), 400

    endpoint = f"/sites/MCO/search?category={category_id}"
    data = get_from_mercadolibre(endpoint)
    return jsonify(data)

# 2. Endpoint para buscar productos por palabra clave
@app.route('/api/search', methods=['GET'])
def search_products():
    query = request.args.get('query')
    if not query:
        return jsonify({"error": "query es obligatorio"}), 400

    endpoint = f"/sites/MCO/search?q={query}"
    data = get_from_mercadolibre(endpoint)
    return jsonify(data)

# 3. Endpoint para obtener detalles de un producto específico
@app.route('/api/product_details', methods=['GET'])
def product_details():
    product_id = request.args.get('product_id')
    if not product_id:
        return jsonify({"error": "product_id es obligatorio"}), 400

    endpoint = f"/items/{product_id}"
    data = get_from_mercadolibre(endpoint)
    return jsonify(data)

# 4. Endpoint para obtener precios por categoría
@app.route('/api/category_prices', methods=['GET'])
def category_prices():
    category_id = request.args.get('category_id')
    if not category_id:
        return jsonify({"error": "category_id es obligatorio"}), 400

    endpoint = f"/sites/MCO/search?category={category_id}"
    data = get_from_mercadolibre(endpoint)
    # Puedes filtrar solo los precios aquí si lo deseas
    prices = [{"price": item["price"]} for item in data.get("results", [])]
    return jsonify(prices)

# 5. Endpoint para consultar información sobre un vendedor
@app.route('/api/seller_info', methods=['GET'])
def seller_info():
    seller_id = request.args.get('seller_id')
    if not seller_id:
        return jsonify({"error": "seller_id es obligatorio"}), 400

    endpoint = f"/users/{seller_id}"
    data = get_from_mercadolibre(endpoint)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
