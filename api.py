from flask import jsonify, request
from conection_db import get_db_connection


def get_items():
    query = request.args.get('q', '')
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM products WHERE title LIKE %s", ('%' + query + '%',))
    products = cursor.fetchall()

    cursor.close()
    connection.close()
    
    return jsonify(products)

def get_item(item_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("""
        SELECT *
        FROM products p
        LEFT JOIN product_images dp ON p.id = dp.product_id
        WHERE p.id = %s
    """, (item_id,))
    
    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    if rows:
        product = {
            "brand": rows[0]['brand'],
            "category": rows[0]['category'],
            "description": rows[0]['description'],
            "discountPercentage": rows[0]['discountPercentage'],
            "id": rows[0]['id'],
            "price": rows[0]['price'],
            "rating": rows[0]['rating'],
            "stock": rows[0]['stock'],
            "thumbnail": rows[0]['thumbnail'],
            "title": rows[0]['title'],
            'images': []
        }

        for row in rows:
            if row['image_url']:
                product['images'].append(row['image_url'])

        return jsonify(product)
    else:
        return jsonify({"error": "Product not found"}), 404


def add_sale():
    sale = request.json
    connection = get_db_connection()
    cursor = connection.cursor()
    
    cursor.execute(
        "INSERT INTO ventas (product_id, quantity, price, total) VALUES (%s, %s, %s, %s)", 
        (sale['product_id'], int(sale['quantity']), float(sale['price']), float(sale['total']))
    )
    connection.commit()
    
    cursor.close()
    connection.close()

    return jsonify({"success": True})

def get_sales():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM products p INNER JOIN ventas v ON p.id = v.product_id;")
    sales = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(sales)
