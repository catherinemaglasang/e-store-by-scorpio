import os
from os import sys
import json, flask
from flask import render_template, request
from flask import jsonify
from app import app
from .models import DBconn
import datetime

PRODUCTS = {}
SUPPLIERS = {}
USERS = {}
CATEGORIES = {}
WISHLISTS = {}


def spcall(qry, param, commit=False):
    """
    Stored procedure util function
    :param qry:
    :param param:
    :param commit:
    :return: rows or response returned by database
    """
    try:
        dbo = DBconn()
        cursor = dbo.getcursor()
        cursor.callproc(qry, param)
        res = cursor.fetchall()
        if commit:
            dbo.dbcommit()
        return res
    except:
        res = [("Error: " + str(sys.exc_info()[0]) + " " + str(sys.exc_info()[1]),)]
    return res


@app.route('/')
def index():
    return jsonify({"status": "ok"})


@app.route('/api/v1/products/', methods=['POST'])
def new_product():
    """
    Example JSON request from client
    {
        'product_id': '1',
        'title': 'Product Name',
        'description': 'Product Description',
        'date_added': '1/1/1 1:1:1',
        'ordering': '0',
        'supplier_id': '1',
        'category_id': '1',
        'site_id': '1',
        'product_type_id': '1',
        'product_attributes': [
            {'isbn': 'isbn1'},
            {'author': 'author1'},
        ],
        'on_hand': '0',
        're_order_level': '0',
        'is_active': 'true',
    }
    :return: json response indicating status of POST request, 201 status code
    """

    product_id = request.json['product_id']
    title = request.json['title']
    description = request.json['description']
    date_added = datetime.datetime.now()  # Default
    ordering = 0  # Default
    supplier_id = request.json['supplier_id']
    category_id = request.json['category_id']
    site_id = request.json['site_id']
    product_type_id = request.json['product_type_id']
    # product_attributes = request.json['product_attributes']
    on_hand = request.json['on_hand']
    re_order_level = request.json['re_order_level']
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
    product_id = request.json.get('product_id', '')
    title = request.json.get('title', ''),
    description = request.json.get('description', ''),
    date_added = datetime.datetime.now()  # Default
    ordering = 0  # Default
    supplier_id = request.json.get('supplier_id', ''),
    category_id = request.json.get('category_id', ''),
    site_id = request.json.get('site_id', ''),
    product_type_id = request.json.get('product_type_id', ''),
    # product_attributes = request.json['product_attributes']
    on_hand = request.json.get('on_hand', ''),
    re_order_level = request.json.get('re_order_level', ''),
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

@app.route('/api/v1/product_categories/', methods=['POST'])
def new_product_category():
    print "STARTING ADD"
    id = request.form['inputID']
    name = request.form['inputName']
    description = request.form['inputDescription']
    main_image = request.form['inputMainImage']
    parent_category_id = request.form['inputParentCategoryId']
    is_active = False

    res = spcall('new_product_category', (
        id, name, description, main_image, parent_category_id, is_active), True)

    if 'Error' in res[0][0]:
        return jsonify({'status': 'error', 'message': res[0][0]})

    return jsonify({'status': 'ok', 'message': res[0][0]})


@app.route('/api/v1/products_category/', methods=['GET'])
def get_all_product_categories():
    res = spcall('get_product_category', ())

    if 'Error' in str(res[0][0]):
        return jsonify({'status': 'error', 'message': res[0][0]})

    recs = []

    for r in res:
        recs.append(
            {"id": str(r[0]), "name": str(r[1]), "description": str(r[2]), "main_image": str(r[3]),
             "parent_category_id": str(r[4]),
             "is_active": str(r[5])})
    return jsonify({'status': 'ok', 'entries': recs, 'count': len(recs)})

    if len(res) > 0:
        for r in res:
            recs.append({"id": str(r[0]), "name": str(r[1]), "description": str(r[2]), "main_image": str(r[3]),
                         "parent_category_id": str(r[4]), "is_active": str(r[5])})
            return jsonify({'status': 'ok', 'entries': recs, 'count': len(recs)})
    else:
        return jsonify({'status': 'no entries in database'})


@app.route('/api/v1/product_categories/<product_category_id>/', methods=['GET'])
def get_product_category(product_category_id):
    res = spcall('get_product_category_id', (product_category_id))

    if 'Error' in res[0][0]:
        return jsonify({'status': 'error', 'message': res[0][0]})

    r = res[0]
    return jsonify(
        {"id": str(product_category_id), "name": str(r[0]), "description": str(r[1]), "main_image": str(r[2]),
         "parent_category_id": str(r[3]), "is_active": str(r[4])})


@app.route('/api/v1/product_category/<int:id>/', methods=['DELETE'])
def delete_product_category(id):
    res = spcall("delete_product_category", (id,), True)
    if 'Error' in res[0][0]:
        return jsonify({'status': 'error', 'message': res[0][0]})

    return jsonify({'status': 'ok', 'message': res[0][0]})

    """ Todo: This route should be protected """


@app.route('/api/v1/users/', methods=['GET'])
def get_all_users():
    res = spcall('get_users', ())

    if 'Error' in str(res[0][0]):
        return jsonify({'status': 'error', 'message': res[0][0]})

    recs = []
    for r in res:
        recs.append({"id": str(r[0]), "username": str(r[1]), "password": str(r[2]), "is_admin": str(r[3])})
    return jsonify({'status': 'ok', 'entries': recs, 'count': len(recs)})


@app.route('/api/v1/users/<user_id>/', methods=['GET'])
def get_user(user_id):
    res = spcall('get_user', (user_id))

    if 'Error' in res[0][0]:
        return jsonify({'status': 'error', 'message': res[0][0]})

    rec = res[0]
    return jsonify({"id": str(user_id), "username": str(rec[0]), "password": str(rec[1]), "is_admin": str(rec[2])})


@app.route('/api/v1/users/', methods=['POST'])
def new_user():
    json = request.json
    user_id = json['id']
    username = json['username']
    password = json['password']
    is_admin = json['is_admin']
    res = spcall('new_user', (user_id, username, password, is_admin), True)

    if 'Error' in res[0][0]:
        return jsonify({'status': 'error', 'message': res[0][0]})
    return jsonify({'status': 'ok', 'message': res[0][0]})


@app.route('/api/v1/suppliers/', methods=['GET'])
def get_all_suppliers():
    res = spcall('get_suppliers', ())

    if 'Error' in str(res[0][0]):
        return jsonify({'status': 'error', 'message': res[0][0]})

    recs = []
    for r in res:
        recs.append({"id": str(r[0]), "name": str(r[1]), "address": str(r[2]), "phone": str(r[3]), "fax": str(r[4]),
                     "email": str(r[5]), "is_active": str(r[6])})
    return jsonify({'status': 'ok', 'entries': recs, 'count': len(recs)})


@app.route('/api/v1/suppliers/<supplier_id>/', methods=['GET'])
def get_supplier(supplier_id):
    res = spcall('get_supplier', supplier_id)

    if 'Error' in res[0][0]:
        return jsonify({'status': 'error', 'message': res[0][0]})

    r = res[0]
    return jsonify(
        {"id": str(supplier_id), "name": str(r[0]), "address": str(r[1]), "phone": str(r[2]), "fax": str(r[3]),
         "email": str(r[4]), "is_active": str(r[5])})


@app.route('/api/v1/cart_details/', methods=['POST'])
def new_cart_detail():
    json = request.json
    id = json['id']
    cart_id = json['cart_id']
    product_id = json['product_id']
    quantity = json['quantity']
    time_stamp = json['time_stamp']
    res = spcall('new_cart_detail', (id, cart_id, product_id, quantity, time_stamp), True)

    if 'Error' in res[0][0]:
        return jsonify({'status': 'error', 'message': res[0][0]})
    return jsonify({'status': 'ok', 'message': res[0][0]})


@app.route('/api/v1/cart_details/', methods=['GET'])
def get_cart_details():
    res = spcall('get_cart_details', ())

    if 'Error' in str(res[0][0]):
        return jsonify({'status': 'error', 'message': res[0][0]})

    recs = []
    for r in res:
        recs.append({"id": r[0], "cart_id": r[1], "product_id": r[2], "quantity": r[3], "time_stamp": r[4]})
    return jsonify({'status': 'ok', 'entries': recs, 'count': len(recs)})


# @app.route('/api/v1/cart_details/<cart_detail_id>/', methods=['GET'])
# def get_cart_detail(cart_detail_id):
#     res = spcall('get_cart_detail', (cart_detail_id))

#     if 'Error' in res[0][0]:
#         return jsonify({'status': 'error', 'message': res[0][0]})

#     r = res[0]
#     return jsonify({"cart_id": r[0], "product_id": r[1], "quantity":r[2], "time_stamp":str(r[3])})


@app.route('/api/v1/wishlist_details/', methods=['POST'])
def new_wishlist_detail():
    json = request.json
    id = json['id']
    wishlist_id = json['wishlist_id']
    product_id = json['product_id']
    time_stamp = json['time_stamp']
    res = spcall('new_wishlist_detail', (id, wishlist_id, product_id, time_stamp), True)

    if 'Error' in res[0][0]:
        return jsonify({'status': 'error', 'message': res[0][0]})
    return jsonify({'status': 'ok', 'message': res[0][0]})


@app.route('/api/v1/wishlist_details/', methods=['GET'])
def get_wishlist_details():
    res = spcall('get_wishlist_details', ())

    if 'Error' in str(res[0][0]):
        return jsonify({'status': 'error', 'message': res[0][0]})

    recs = []
    for r in res:
        recs.append({"id": r[0], "cart_id": r[1], "product_id": r[2], "time_stamp": r[3]})
    return jsonify({'status': 'ok', 'entries': recs, 'count': len(recs)})


@app.route('/api/v1/wishlist/', methods=['POST'])
def new_wishlist():
    json = request.json
    id = json['id']
    res = spcall('new_wishlist', (id), True)

    if 'Error' in res[0][0]:
        return jsonify({'status': 'error', 'message': res[0][0]})
    return jsonify({'status': 'ok', 'message': res[0][0]})


@app.route('/api/v1/wishlist/', methods=['GET'])
def get_wishlist():
    res = spcall('get_wishlist', ())

    if 'Error' in str(res[0][0]):
        return jsonify({'status': 'error', 'message': res[0][0]})

    recs = []
    for r in res:
        recs.append({"id": r[0]})
    return jsonify({'status': 'ok', 'entries': recs, 'count': len(recs)})

# @app.after_request
# def add_cors(resp):
#     resp.headers['Access-Control-Allow-Origin'] = flask.request.headers.get('Origin', '*')
#     resp.headers['Access-Control-Allow-Credentials'] = True
#     resp.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS, GET, PUT, DELETE'
#     resp.headers['Access-Control-Allow-Headers'] = flask.request.headers.get('Access-Control-Request-Headers',
#                                                                              'Authorization')
#     if app.debug:
#         resp.headers["Access-Control-Max-Age"] = '1'
#     return resp
