import json
import datetime
from flask import current_app
from flask import request, Blueprint
from flask import jsonify, render_template
from app.models import spcall
from app import api
from .utils import build_json


# -----------------
# Routes for POST & UPDATE
# -----------------
@api.route('/api/v1/products/', methods=['POST'])
@api.route('/api/v1/products/<product_id>/', methods=['PUT'])
def product_upsert(product_id=None):
    data = json.loads(request.data)

    response = spcall('products_upsert', (
        product_id,
        data['title'],
        data['description'],
        data['supplier_id'],
        data['category_id'],
        data['site_id'],
        data['product_type_id'],
        data['on_hand'],
        data['re_order_level'],), True)

    json_dict = build_json(response)

    status_code = 200
    if not product_id:
        status_code = 201

    return jsonify(json_dict), status_code


@api.route('/api/v1/producttypes/', methods=['POST'])
@api.route('/api/v1/producttypes/<product_type_id>/', methods=['PUT'])
def product_type_upsert(product_type_id=None):
    data = json.loads(request.data)

    response = spcall('product_types_upsert', (
        product_type_id,
        data['name'],
        data['description']), True)

    json_dict = build_json(response)

    status_code = 200
    if not product_type_id:
        status_code = 201

    return jsonify(json_dict), status_code


@api.route('/api/v1/categories/', methods=['POST'])
@api.route('/api/v1/categories/<category_id>/', methods=['PUT'])
def category_upsert(category_id=None):
    data = json.loads(request.data)

    response = spcall('categories_upsert', (
        category_id,
        data['name'],
        data['description'],
        data['image']), True)

    json_dict = build_json(response)

    status_code = 200
    if not category_id:
        status_code = 201

    return jsonify(json_dict), status_code


@api.route('/api/v1/producttypes/<product_type_id>/attributes/', methods=['POST'])
@api.route('/api/v1/producttypes/<product_type_id>/attributes/<product_attribute_id>/', methods=['PUT'])
def product_attribute_upsert(product_type_id,product_attribute_id=None):
    data = json.loads(request.data)

    response = spcall('product_attributes_upsert', (
        product_type_id,
        product_attribute_id,
        data['name'],
        data['code'],
        data['type'],
        data['is_required']), True)

    json_dict = build_json(response)

    status_code = 200
    if not product_attribute_id:
        status_code = 201

    return jsonify(json_dict), status_code


# -----------------
# Routes for GET
# -----------------

@api.route('/api/v1/products/', methods=['GET'])
@api.route('/api/v1/products/<product_id>/', methods=['GET'])
def products_get(product_id=None):
    response = spcall('products_get', (product_id,), )

    json_dict = build_json(response)

    return jsonify(json_dict)


@api.route('/api/v1/producttypes/', methods=['GET'])
@api.route('/api/v1/producttypes/<product_type_id>/', methods=['GET'])
def product_types_get(product_type_id=None):
    response = spcall('product_types_get', (product_type_id,))

    json_dict = build_json(response)

    return jsonify(json_dict)


@api.route('/api/v1/categories/', methods=['GET'])
@api.route('/api/v1/categories/<category_id>/', methods=['GET'])
def categories_get(category_id=None):
    response = spcall('categories_get', (category_id,))

    json_dict = build_json(response)

    return jsonify(json_dict)


@api.route('/api/v1/producttypes/<int:product_type_id>/attributes/', methods=['GET'])
@api.route('/api/v1/producttypes/<int:product_type_id>/attributes/<int:product_attribute_id>/', methods=['GET'])
def product_attributes_get(product_type_id, product_attribute_id=None):
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

