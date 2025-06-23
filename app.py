from flask import Flask, request, jsonify

app = Flask(__name__)

products = [{"id": 1, "name": "Shoe"}, {"id": 2, "name": "Bag"}]

@app.route('/health')
def health():
    return jsonify({"status": "ok"})

@app.route('/products')
def get_products():
    return jsonify(products)

@app.route('/products/search')
def search_products():
    q = request.args.get('q', '')
    result = [p for p in products if q.lower() in p["name"].lower()]
    return jsonify(result) if result else ({"error": "Not found"}, 404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
