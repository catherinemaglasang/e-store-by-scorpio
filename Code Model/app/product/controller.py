import json
import datetime
from flask import current_app
from flask import request, Blueprint
from flask import jsonify, render_template
from app.models import spcall
from app import api


@api.route('/api/v1/products/', methods=['POST'])
def add_product():
    data = json.loads(request.data)

    response = spcall('add_product', (
        data['title'],
        data['description'],
        data['supplier_id'],
        data['category_id'],
        data['site_id'],
        data['product_type_id'],
        data['on_hand'],
        data['re_order_level'],), True)

    if 'Error' in response[0][0]:
        return jsonify({'status': 'error', 'message': response[0][0]})

    return jsonify({'status': 'ok', 'message': response[0][0]}), 201

@api.route('/api/v1/producttypes/', methods=['POST'])
def add_product_type():
    data = json.loads(request.data)

    response = spcall('add_product_type', (
        data['name'],
        data['description']), True)

    if 'Error' in response[0][0]:
        return jsonify({'status': 'error', 'message': response[0][0]})

    return jsonify({'status': 'ok', 'message': response[0][0]}), 201


@api.route('/api/v1/products/', methods=['GET'])
def get_products():
    response = spcall('get_products', (), )

    entries = []

    if len(response) == 0:
        return jsonify({"status": "ok", "message": "No entries found", "entries": [], "count": "0"})

    if 'Error' in str(response[0][0]):
        return jsonify({'status': 'error', 'message': response[0][0]})

    for row in response:
        entries.append(dict(row))
    return jsonify({'status': 'ok', 'message': 'ok', 'entries': entries, 'count': len(entries)})

@api.route('/api/v1/producttypes/', methods=['GET'])
def get_product_types():
    response = spcall('get_product_types', (), )

    entries = []

    if len(response) == 0:
        return jsonify({"status": "ok", "message": "No entries found", "entries": [], "count": "0"})

    if 'Error' in str(response[0][0]):
        return jsonify({'status': 'error', 'message': response[0][0]})

    for row in response:
        entries.append(dict(row))
    return jsonify({'status': 'ok', 'message': 'ok', 'entries': entries, 'count': len(entries)})


@api.route('/api/v1/products/<product_id>/', methods=['GET'])
def get_product(product_id):
    response = spcall('get_product', (product_id,))
    entries = []

    if len(response) == 0:
        return jsonify({"status": "ok", "message": "No entries found", "entries": [], "count": "0"})

    entries.append(dict(response[0]))
    return jsonify({"status": "ok", "message": "ok", "entries": entries, "count": len(entries)})

@api.route('/api/v1/producttypes/<product_type_id>/', methods=['GET'])
def get_product_type(product_type_id):
    response = spcall('get_product_type', (product_type_id,))
    entries = []

    if len(response) == 0:
        return jsonify({"status": "ok", "message": "No entries found", "entries": [], "count": "0"})

    entries.append(dict(response[0]))
    return jsonify({"status": "ok", "message": "ok", "entries": entries, "count": len(entries)})


@api.route('/api/v1/products/<product_id>/', methods=['PUT'])
def update_product(product_id):
    # Process data from the client request
    data = json.loads(request.data)

    # Call stored proc for update
    response = spcall('update_product', (
        data['product_id'],
        data['title'],
        data['description'],
        data['supplier_id'],
        data['category_id'],
        data['site_id'],
        data['product_type_id'],
        data['on_hand'],
        data['re_order_level']), True)

    # Process stored proc response
    if 'Error' in str(response[0][0]):
        return jsonify({'status': 'error', 'message': response[0][0]})

    return jsonify({'status': 'ok', 'message': 'ok'})

@api.route('/api/v1/producttypes/<product_type_id>/', methods=['PUT'])
def update_product_type(product_type_id):
    # Process data from the client request
    data = json.loads(request.data)

    # Call stored proc for update
    response = spcall('update_product_type', (
        data['product_type_id'],
        data['name'],
        data['description'],), True)

    # Process stored proc response
    if 'Error' in str(response[0][0]):
        return jsonify({'status': 'error', 'message': response[0][0]})

    return jsonify({'status': 'ok', 'message': 'ok'})
