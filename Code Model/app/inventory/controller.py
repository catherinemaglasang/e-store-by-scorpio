import json
import decimal

from flask import jsonify
from flask import request

from app import api
from app.db import spcall
from app.utils import build_json


@api.route('/', methods=['GET'])
def index():
    return jsonify({"status": "ok", "message": "ok"})


# -----------------
# Routes for POST & UPDATE
# -----------------
@api.route('/api/v1/items/', methods=['POST'])
@api.route('/api/v1/items/<item_id>/', methods=['PUT'])
def items_upsert(item_id=None):
    data = json.loads(request.data)

    response = spcall('items_upsert', (
        item_id,
        data['serial_no'],
        data['name'],
        data['description'],
        str(data['date_added']),
        str(data['date_updated']),
        data['is_active'],
        data['has_variations'],), True)

    json_dict = build_json(response)

    status_code = 200
    if not item_id:
        status_code = 201

    return jsonify(json_dict), status_code


@api.route('/api/v1/items/<item_id>/attributes/', methods=['POST'])
@api.route('/api/v1/items/<item_id>/attributes/<attribute_id>/', methods=['PUT'])
def item_attributes_upsert(item_id, attribute_id=None):
    data = json.loads(request.data)

    response = spcall('item_attributes_upsert', (
        data['attribute_id'],
        data['item_id'],
        data['attribute_value'],), True)

    json_dict = build_json(response)

    status_code = 200
    if not attribute_id:
        status_code = 201

    return jsonify(json_dict), status_code


@api.route('/api/v1/items/<item_id>/variations/', methods=['POST'])
@api.route('/api/v1/items/<item_id>/variations/<option_id>/', methods=['PUT'])
def item_variations_upsert(item_id, option_id=None):
    data = json.loads(request.data)

    response = spcall('item_variations_upsert', (
        data['item_id'],
        data['option_id'],
        data['stock_on_hand'],
        data['unit_cost'],
        data['re_order_level'],
        data['re_order_quantity'],
        data['is_active'],), True)

    json_dict = build_json(response)

    status_code = 200
    if not option_id:
        status_code = 201

    return jsonify(json_dict), status_code


@api.route('/api/v1/attributes/', methods=['POST'])
@api.route('/api/v1/attributes/<attribute_id>/', methods=['PUT'])
def attributes_upsert(attribute_id=None):
    data = json.loads(request.data)

    response = spcall('attributes_upsert', (
        attribute_id,
        data['attribute_name'],
        data['validation'],), True)

    json_dict = build_json(response)

    status_code = 200
    if not attribute_id:
        status_code = 201

    return jsonify(json_dict), status_code


@api.route('/api/v1/locations/', methods=['POST'])
@api.route('/api/v1/locations/<location_id>/', methods=['PUT'])
def locations_upsert(location_id=None):
    data = json.loads(request.data)

    response = spcall('locations_upsert', (
        location_id,
        data['location_name'],), True)

    json_dict = build_json(response)

    status_code = 200
    if not location_id:
        status_code = 201

    return jsonify(json_dict), status_code

@api.route('/api/v1/optiongroups/', methods=['POST'])
@api.route('/api/v1/optiongroups/<option_group_id>/', methods=['PUT'])
def option_groups_upsert(option_group_id=None):
    data = json.loads(request.data)

    response = spcall('option_groups_upsert', (
        option_group_id,
        data['option_group_name'],), True)

    json_dict = build_json(response)

    status_code = 200
    if not option_group_id:
        status_code = 201

    return jsonify(json_dict), status_code


@api.route('/api/v1/optiongroups/<option_group_id>/options/', methods=['POST'])
@api.route('/api/v1/optiongroups/<option_group_id>/options/<option_id>/', methods=['PUT'])
def options_upsert(option_group_id, option_id=None):
    data = json.loads(request.data)
    response = spcall('options_upsert', (
        option_id,
        option_group_id,
        data['option_value'],), True)
    json_dict = build_json(response)

    status_code = 200
    if not option_id:
        status_code = 201

    return jsonify(json_dict), status_code


# -----------------
# Routes for GET
# -----------------

@api.route('/api/v1/items/', methods=['GET'])
@api.route('/api/v1/items/<item_id>/', methods=['GET'])
def items_get(item_id=None):
    response = spcall('items_get', (item_id,), )

    json_dict = build_json(response)

    return jsonify(json_dict)


@api.route('/api/v1/items/<item_id>/attributes/', methods=['GET'])
@api.route('/api/v1/items/<item_id>/attributes/<attribute_id>/', methods=['GET'])
def item_attributes_get(item_id, attribute_id=None):
    response = spcall('item_attributes_get', (attribute_id, item_id,), )

    json_dict = build_json(response)

    return jsonify(json_dict)

@api.route('/api/v1/items/<item_id>/variations/', methods=['GET'])
@api.route('/api/v1/items/<item_id>/variations/<option_id>/', methods=['GET'])
def item_variations_get(item_id, option_id=None):
    response = spcall('item_variations_get', (item_id, option_id,), )

    json_dict = build_json(response)

    return jsonify(json_dict)


@api.route('/api/v1/attributes/', methods=['GET'])
@api.route('/api/v1/attributes/<attribute_id>/', methods=['GET'])
def attributes_get(attribute_id=None):
    response = spcall('attributes_get', (attribute_id,))

    json_dict = build_json(response)

    return jsonify(json_dict)


@api.route('/api/v1/locations/', methods=['GET'])
@api.route('/api/v1/locations/<location_id>/', methods=['GET'])
def locations_get(location_id=None):
    response = spcall('locations_get', (location_id,))

    json_dict = build_json(response)

    return jsonify(json_dict)

@api.route('/api/v1/optiongroups/', methods=['GET'])
@api.route('/api/v1/optiongroups/<option_group_id>/', methods=['GET'])
def option_groups_get(option_group_id=None):
    response = spcall('option_groups_get', (option_group_id,))

    json_dict = build_json(response)

    return jsonify(json_dict)


@api.route('/api/v1/optiongroups/<option_group_id>/options/', methods=['GET'])
@api.route('/api/v1/optiongroups/<option_group_id>/options/<option_id>/', methods=['GET'])
def options_get(option_group_id, option_id=None):
    response = spcall('options_get', (option_id, option_group_id,))

    json_dict = build_json(response)

    return jsonify(json_dict)
