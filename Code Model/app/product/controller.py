import json
import datetime
from flask import current_app
from flask import request, Blueprint
from flask import jsonify, render_template
from app.models import spcall
from app import api
from .models import Product


@api.route('/api/v1/products/', methods=['POST'])
def new_product():
    product = Product()
    product.from_json(request.data)
    response = product.save()
    return jsonify(response), 201


@api.route('/api/v1/products/', methods=['GET'])
def get_all_products():
    response = Product.get()
    return jsonify(response)


@api.route('/api/v1/products/<product_id>/', methods=['GET'])
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


@api.route('/api/v1/products/<product_id>/', methods=['PUT'])
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
