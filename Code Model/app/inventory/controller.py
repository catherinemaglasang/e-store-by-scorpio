import json
from flask import request
from flask import jsonify
from app.db import spcall
from app import api
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
        data['site_id'],
        data['serial_no'],
        data['tax_class_id'],
        data['type_id'],
        data['name'],
        data['description'],
        data['date_added'],
        data['date_updated'],
        data['is_taxable'],
        data['unit_cost'],
        data['is_active'],
        data['has_variations'],), True)

    json_dict = build_json(response)

    status_code = 200
    if not item_id:
        status_code = 201

    return jsonify(json_dict), status_code


@api.route('/api/v1/types/', methods=['POST'])
@api.route('/api/v1/types/<type_id>/', methods=['PUT'])
def types_upsert(type_id=None):
    data = json.loads(request.data)

    response = spcall('types_upsert', (
        type_id,
        data['type_name'],
        data['type_description'],), True)

    json_dict = build_json(response)

    status_code = 200
    if not type_id:
        status_code = 201

    return jsonify(json_dict), status_code

@api.route('/api/v1/types/<type_id>/attributes/', methods=['POST'])
@api.route('/api/v1/types/<type_id>/attributes/<attribute_id>', methods=['PUT'])
def attributes_upsert(type_id, attribute_id=None):
    data = json.loads(request.data)

    response = spcall('attributes_upsert', (
        attribute_id,
        type_id,
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


# -----------------
# Routes for GET
# -----------------

@api.route('/api/v1/items/', methods=['GET'])
@api.route('/api/v1/items/<item_id>/', methods=['GET'])
def items_get(item_id=None):
    response = spcall('items_get', (item_id,), )

    json_dict = build_json(response)

    return jsonify(json_dict)


@api.route('/api/v1/types/', methods=['GET'])
@api.route('/api/v1/types/<type_id>/', methods=['GET'])
def types_get(type_id=None):
    response = spcall('types_get', (type_id,))

    entries = []
    out = {}

    if len(response) == 0:
        ret = {"status": "ok", "message": "No entries found", "entries": [], "count": 0}

    if 'Error' in str(response[0][0]):
        ret = {'status': 'error', 'message': response[0][0]}

    for row in response:
        r = dict(row)

        attributes = spcall('attributes_get', (None, r['type_id'], ))
        attribute_list = []
        for row in attributes:
            attribute_list.append(dict(row))
        r['attributes'] = attribute_list
        entries.append(r)

    ret = {'status': 'ok', 'message': 'ok', 'entries': entries, 'count': len(entries)}


    return jsonify(ret)

@api.route('/api/v1/types/<type_id>/attributes/', methods=['GET'])
@api.route('/api/v1/types/<type_id>/attributes/<attribute_id>/', methods=['GET'])
def attributes_get(type_id, attribute_id=None):
    response = spcall('attributes_get', (attribute_id, type_id,))

    json_dict = build_json(response)

    return jsonify(json_dict)


@api.route('/api/v1/locations/', methods=['GET'])
@api.route('/api/v1/locations/<location_id>/', methods=['GET'])
def locations_get(location_id=None):
    response = spcall('locations_get', (location_id,))

    json_dict = build_json(response)

    return jsonify(json_dict)