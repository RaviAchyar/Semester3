from flask import Flask, jsonify
import json

app = Flask(__name__)

def load_data():
    with open('data-makanan.json', 'r') as f:
        makanan = json.load(f)

    with open('data-minuman.json', 'r') as f:
        minuman = json.load(f)

    return makanan + minuman
    
@app.route('/', methods=['GET'])
def get_all_produk():
    data = load_data()
    return jsonify(data)

@app.route('/<string:produk_id>', methods=['GET'])
def get_produk_by_id(produk_id):
    data = load_data()
    produk = next((item for item in data if item["id"] == produk_id), None)
    if produk:
        return jsonify(produk)
    else:
        return jsonify({"message": "barang tidak ada/habis"}), 404
    
if __name__ == '__main__':
    app.run(debug=True)
