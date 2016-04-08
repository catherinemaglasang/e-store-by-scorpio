import json
import decimal

from flask import jsonify
from flask import request

from app import api
from app.db import spcall
from app.utils import build_json


# -----------------
# Routes for POST & UPDATE
# -----------------
@api.route('/api/v1/wishlists/', methods=['POST'])
@api.route('/api/v1/wishlists/<wishlist_id>/', methods=['PUT'])
def wishlists_upsert(wishlist_id=None):
    data = json.loads(request.data)

    response = spcall('wishlists_upsert', (
        wishlist_id,
        data['wishlist_name'],), True)

    json_dict = build_json(response)

    status_code = 200
    if not wishlist_id:
        status_code = 201

    return jsonify(json_dict), status_code


@api.route('/api/v1/wishlists/<wishlist_id>/items/', methods=['POST'])
@api.route('/api/v1/wishlists/<wishlist_id>/items/<item_id>/', methods=['PUT'])
def wishlist_items_upsert(wishlist_id, item_id=None):
    data = json.loads(request.data)

    response = spcall('wishlist_items_upsert', (
        data['wishlist_id'],
        data['item_id'],
        data['time_stamp'],), True)

    json_dict = build_json(response)

    status_code = 200
    if not item_id:
        status_code = 201

    return jsonify(json_dict), status_code


# -----------------
# Routes for GET
# -----------------

@api.route('/api/v1/wishlists/', methods=['GET'])
@api.route('/api/v1/wishlists/<wishlist_id>/', methods=['GET'])
def wishlist_get(wishlist_id=None):
    response = spcall('wishlists_get', (wishlist_id,), )

    json_dict = build_json(response)

    return jsonify(json_dict)

@api.route('/api/v1/wishlists/<wishlist_id>/items/', methods=['GET'])
@api.route('/api/v1/wishlists/<wishlist_id>/items/<item_id>/', methods=['GET'])
def wishlist_items_get(wishlist_id, item_id=None):
    response = spcall('wishlist_items_get', (wishlist_id, item_id), )

    json_dict = build_json(response)

    return jsonify(json_dict)
