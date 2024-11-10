# app.py
from flask import Flask
from api import get_items, get_item, add_sale, get_sales
from flask_cors import CORS 

app = Flask(__name__)
CORS(app) 
# Rutas de la API
app.add_url_rule('/api/items', 'get_items', get_items, methods=['GET'])
app.add_url_rule('/api/items/<int:item_id>', 'get_item', get_item, methods=['GET'])
app.add_url_rule('/api/addSale', 'add_sale', add_sale, methods=['POST'])
app.add_url_rule('/api/sales', 'get_sales', get_sales, methods=['GET'])

if __name__ == '__main__':
    app.run(debug=True, port=8080)
