import json
import datetime
from flask import current_app
from flask import request, Blueprint
from flask import jsonify, render_template
from app.models import spcall
from app import api
from .utils import build_json


# -----------------
# Routes for POST
# -----------------
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


@api.route('/api/v1/categories/', methods=['POST'])
def add_category():
    data = json.loads(request.data)

    response = spcall('add_category', (
        data['name'],
        data['description'],
        data['image']), True)

    if 'Error' in response[0][0]:
        return jsonify({'status': 'error', 'message': response[0][0]})

    return jsonify({'status': 'ok', 'message': response[0][0]}), 201


@api.route('/api/v1/producttypes/<product_type_id>/attributes/', methods=['POST'])
def add_product_type_attribute(product_type_id):
    data = json.loads(request.data)

    response = spcall('product_attributes_create', (
        product_type_id,
        data['name'],
        data['code'],
        data['type'],
        data['is_required']), True)

    print response
    if 'Error' in response[0][0]:
        return jsonify({'status': 'error', 'message': response[0][0]})

    return jsonify({'status': 'ok', 'message': response[0][0]}), 201


# -----------------
# Routes for GET
# -----------------

@api.route('/api/v1/products/', methods=['GET'])
@api.route('/api/v1/products/<product_id>/', methods=['GET'])
def get_products(product_id=None):
    if not product_id:
        response = spcall('get_products', (), )
    else:
        response = spcall('get_product', (product_id,), )

    json_dict = build_json(response)

    return jsonify(json_dict)


@api.route('/api/v1/producttypes/', methods=['GET'])
@api.route('/api/v1/producttypes/<product_type_id>/', methods=['GET'])
def get_product_types(product_type_id=None):
    if not product_type_id:
        response = spcall('get_product_types', (), )
    else:
        response = spcall('get_product_type', (product_type_id,))

    json_dict = build_json(response)

    return jsonify(json_dict)


@api.route('/api/v1/categories/', methods=['GET'])
@api.route('/api/v1/categories/<category_id>/', methods=['GET'])
def get_categories(category_id=None):
    if not category_id:
        response = spcall('get_categories', (), )
    else:
        response = spcall('get_category', (category_id,))

    json_dict = build_json(response)

    return jsonify(json_dict)


@api.route('/api/v1/producttypes/<int:product_type_id>/attributes/', methods=['GET'])
@api.route('/api/v1/producttypes/<int:product_type_id>/attributes/<int:product_attribute_id>/', methods=['GET'])
def product_attributes_get(product_type_id, product_attribute_id=None):
    if not product_attribute_id:
        response = spcall('product_attributes_get_all', (int(product_type_id),))
    else:
        response = spcall('product_attributes_get', (product_type_id, product_attribute_id,))

    json_dict = build_json(response)

    return jsonify(json_dict)


@api.route('/api/v1/products/<product_id>/categories/<product_category_id>/')
@api.route('/api/v1/products/<product_id>/categories/')
def product_categories_get(product_id, product_category_id=None):
    # Call stored procedure
    response = spcall('product_categories_get', (product_id, product_category_id,))

    # Build json response using util function
    json_dict = build_json(response)

    # Return api response
    return jsonify(json_dict)


@api.route('/api/v1/products/<product_id>/attributes/<product_attribute_value_id>/')
@api.route('/api/v1/products/<product_id>/attributes/')
def product_attribute_values_get(product_id, product_attribute_value_id=None):
    # Call stored procedure
    response = spcall('product_attribute_values_get', (product_id, product_attribute_value_id,))

    # Build json response using util function
    json_dict = build_json(response)

    # Return api response
    return jsonify(json_dict)


@api.route('/api/v1/products/<product_id>/images/<product_image_id>/')
@api.route('/api/v1/products/<product_id>/images/')
def product_images_get(product_id, product_image_id=None):
    # Call stored procedure
    response = spcall('product_images_get', (product_id, product_image_id,))

    # Build json response using util function
    json_dict = build_json(response)

    # Return api response
    return jsonify(json_dict)

# -----------------
# Routes for UPDATE
# -----------------

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


@api.route('/api/v1/producttypes/<product_type_id>/attributes/<product_attribute_id>/', methods=['PUT'])
def update_product_attributes(product_type_id, product_attribute_id):
    # Process data from the client request
    data = json.loads(request.data)

    # Call stored proc for update
    response = spcall('product_attributes_update', (
        product_attribute_id,
        product_type_id,
        data['name'],
        data['code'],
        data['type'],
        data['is_required'],), True)

    print "update"
    print response
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


@api.route('/api/v1/categories/<category_id>/', methods=['PUT'])
def update_category(category_id):
    # Process data from the client request
    data = json.loads(request.data)

    # Call stored proc for update
    response = spcall('update_category', (
        data['category_id'],
        data['name'],
        data['description'],
        data['image'],), True)

    # Process stored proc response
    if 'Error' in str(response[0][0]):
        return jsonify({'status': 'error', 'message': response[0][0]})

    return jsonify({'status': 'ok', 'message': 'ok'})
