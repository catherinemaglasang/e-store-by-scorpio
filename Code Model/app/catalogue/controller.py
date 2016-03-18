import json
import datetime
from app import app
from flask import request
from flask import jsonify
from app.models import DBconn

# Instance of our sqlalchemy engine
db_con = DBconn()


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
    is_active = True  # Default

    response = db_con.call_procedure('new_product', (
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
        is_active), 'product')

    return jsonify(response), 201


@app.route('/api/v1/products/', methods=['GET'])
def get_all_products():
    response = db_con.call_procedure('get_product', (), 'product')
    return jsonify(response)


@app.route('/api/v1/products/<product_id>/', methods=['GET'])
def get_product(product_id):
    response = db_con.call_procedure('get_product_id', (product_id,), 'product')
    return jsonify(response)


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

    response = db_con.call_procedure('update_product_id', (
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
        is_active), 'product')
    return jsonify(response)
