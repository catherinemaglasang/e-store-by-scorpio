import json
import datetime
from flask import request
from flask import jsonify
from app import app
from app.models import spcall

@app.route('/api/v1/products/', methods=['POST'])
def new_product():
    jsn = json.loads(request.data)
    product_id = jsn['product_id']
    title = jsn['title']
    description = jsn['description']
    date_added = datetime.datetime.now()  # Default
    ordering = 0  # Default
    supplier_id = jsn['supplier_id']
    category_id = jsn['category_id']
    site_id = jsn['site_id']
    product_type_id = jsn['product_type_id']
    # product_attributes = request.json['product_attributes']
    on_hand = jsn['on_hand']
    re_order_level = jsn['re_order_level']
    is_active = True                    # Default

    response = spcall('new_product', (
        product_id,
        title,
        description,
        date_added,
        ordering,
        supplier_id,
        category_id,
        site_id,
        product_type_id,
        on_hand,
        re_order_level,
        is_active), True)

    if 'Error' in response[0][0]:
        return jsonify({'status': 'error', 'message': response[0][0]})

    return jsonify({'status': 'ok', 'message': response[0][0]}), 201


@app.route('/api/v1/products/', methods=['GET'])
def get_all_products():
    response = spcall('get_product', ())
    entries = []

    if len(response) == 0:
        return jsonify({"status": "ok", "message": "No entries found", "entries": [], "count": "0"})
    elif 'Error' in str(response[0][0]):
        return jsonify({'status': 'error', 'message': response[0][0]})
    else:
        for row in response:
            entries.append({"product_id": row[0],
                        "title": row[1],
                        "description": row[2],
                        "date_added": row[3],
                        "ordering": row[4],
                        "supplier_id": row[5],
                        "category_id": row[6],
                        "site_id": row[7],
                        "product_type_id": row[8],
                        "on_hand": row[9],
                        "re_order_level": row[10],
                        "is_active": row[11]})
        return jsonify({'status': 'ok', 'message': 'ok', 'entries': entries, 'count': len(entries)})

@app.route('/api/v1/products/<product_id>/', methods=['GET'])
def get_product(product_id):
    response = spcall('get_product_id', (product_id,))
    entries = []
    if len(response) == 0:
        return jsonify({"status": "ok", "message": "No entries found", "entries": [], "count": "0"})
    else:
        row = response[0]
        entries.append({"product_id": row[0],
                        "title": row[1],
                        "description": row[2],
                        "date_added": row[3],
                        "ordering": row[4],
                        "supplier_id": row[5],
                        "category_id": row[6],
                        "site_id": row[7],
                        "product_type_id": row[8],
                        "on_hand": row[9],
                        "re_order_level": row[10],
                        "is_active": row[11]})
        return jsonify({"status": "ok", "message": "ok", "entries": entries, "count": len(entries)})

@app.route('/api/v1/products/<product_id>/', methods=['PUT'])
def update_product(product_id):
    jsn = json.loads(request.data)
    product_id = jsn.get('product_id', '')
    title = jsn.get('title', ''),
    description = jsn.get('description', ''),
    date_added = datetime.datetime.now()  # Default
    ordering = 0  # Default
    supplier_id = jsn.get('supplier_id', ''),
    category_id = jsn.get('category_id', ''),
    site_id = jsn.get('site_id', ''),
    product_type_id = jsn.get('product_type_id', ''),
    # product_attributes = request.json['product_attributes']
    on_hand = jsn.get('on_hand', ''),
    re_order_level = jsn.get('re_order_level', ''),
    is_active = True

    response = spcall('update_product_id', (
        product_id,
        title,
        description,
        date_added,
        ordering,
        supplier_id,
        category_id,
        site_id,
        product_type_id,
        on_hand,
        re_order_level,
        is_active), True)
    return jsonify({"status": "ok"})