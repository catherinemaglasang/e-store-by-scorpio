import os
import datetime
from os import sys
import json, flask
from flask import render_template, request
from flask import jsonify
from app import app
from .models import spcall

SUPPLIERS = {}
USERS = {}
CATEGORIES = {}
WISHLISTS = {}
ORDER = {}
CART_DETAILS = {}
CARTS = {}
ORDER_DETAILS = {}


@app.route('/')
def index():
    return jsonify({"status": "ok"})

@app.route('/api/v1/product_categories/', methods=['POST'])
def new_product_category():
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


@app.route('/api/v1/product_categories/', methods=['GET'])
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


""" SUPPLIER """


@app.route('/api/v1/suppliers/', methods=['POST'])
def new_supplier():
    json = request.json
    id = json['id']
    name = json['name']
    address = json['address']
    phone = json['phone']
    fax = json['fax']
    email = json['email']
    is_active = json['is_active']
    res = spcall('new_supplier', (id, name, address, phone, fax, email, is_active), True)

    if 'Error' in str(res[0][0]):
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


""" END OF SUPPLIER """

""" CART DETAIL """

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


@app.route('/api/v1/cart_details/<cart_detail_id>/', methods=['GET'])
def get_cart_detail(cart_detail_id):
    res = spcall('get_cart_detail', cart_detail_id)

    if 'Error' in str(res[0][0]):
        return jsonify({'status': 'error', 'message': res[0][0]})

    r = res[0]
    return jsonify(
        {"cart_id": str(cart_detail_id), "product_id": str(r[0]), "quantity": str(r[1]), "time_stamp": str(r[3])})


""" END CART DETAIL """

""" CART """


@app.route('/api/v1/carts/', methods=['POST'])
def new_cart():
    json = request.json
    id = json['id']
    session_id = json['session_id']
    date_created = json['customer_id']
    customer_id = json['product_id']
    is_active = json['is_active']
    res = spcall('new_cart', (id, session_id, date_created, customer_id, is_active), True)

    if 'Error' in res[0][0]:
        return jsonify({'status': 'error', 'message': res[0][0]})
    return jsonify({'status': 'ok', 'message': res[0][0]})


@app.route('/api/v1/carts/<cart_id>/', methods=['GET'])
def get_cart(cart_id):
    res = spcall('get_cart', cart_id)

    if 'Error' in str(res[0][0]):
        return jsonify({'status': 'error', 'message': res[0][0]})

    r = res[0]
    return jsonify({"id": str(cart_id), "session_id": str(r[0]), "date_created": str(r[1]), "customer_id": str(r[2]),
                    "is_active": str(r[3])})


""" END OF CART """


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


@app.route('/api/v1/orders', methods=['GET'])
def get_all_orders():
    """
    Retrieve All Orders
    """

    res = spcall('get_orders', ())

    if 'Error' in str(res[0][0]):
        return jsonify({'status': 'error', 'message': res[0][0]})

    recs = []
    for r in res:
        recs.append({"id": str(r[0]), "customer_id": str(r[1]), "payment_id": str(r[2]), "transaction_date": str(r[3]),
                     "shipping_date": str(r[4]),
                     "time_stamp": str(r[5]), "transaction_status": str(r[6]), "total": str(r[7])})
    return jsonify({'status': 'ok', 'entries': recs, 'count': len(recs)})


@app.route('/api/v1/orders/<orders_id>/', methods=['GET'])
def get_orders(orders_id):
    """
    Retrieve Single Order
    """
    res = spcall('get_order_id', orders_id)

    if 'Error' in str(res[0][0]):
        return jsonify({'status': 'error', 'message': res[0][0]})

    r = res[0]
    return jsonify(
        {"id": str(orders_id), "customer_id": str(r[0]), "payment_id": str(r[1]), "transaction_date": str(r[2]),
         "shipping_date": str(r[3]),
         "time_stamp": str(r[4]), "transaction_status": str(r[5]), "total": str(r[6])})


@app.route('/api/v1/orders/', methods=['POST'])
def new_orders():
    """
    Create New Orders
    """
    json = request.json
    id = json['id']
    customer_id = json['customer_id']
    payment_id = json['payment_id']
    transaction_date = json['transaction_date']
    shipping_date = json['shipping_date']
    time_stamp = json['time_stamp']
    transaction_status = json['transaction_status']
    total = json['total']
    res = spcall('new_order',
                 (id, customer_id, payment_id, transaction_date, shipping_date, time_stamp, transaction_status, total),
                 True)

    if 'Error' in res[0][0]:
        return jsonify({'status': 'error', 'message': res[0][0]})
    return jsonify({'status': 'ok', 'message': res[0][0]})


@app.route('/api/v1/order_details', methods=['GET'])
def get_all_order_details():
    """
    Retrieve All Order_Details
    """

    res = spcall('get_order_details', ())

    if 'Error' in str(res[0][0]):
        return jsonify({'status': 'error', 'message': res[0][0]})

    recs = []
    for r in res:
        recs.append({"id": str(r[0]), "order_id": str(r[1]), "product_id": str(r[2]), "unit_price": str(r[3]),
                     "discount": str(r[4]),
                     "quantity": str(r[5])})
    return jsonify({'status': 'ok', 'entries': recs, 'count': len(recs)})


@app.route('/api/v1/order_details/<order_detail_id>/', methods=['GET'])
def get_order_detail(order_detail_id):
    """
    Retrieve Single Order_Detail
    """
    res = spcall('get_order_details_id', order_detail_id)

    if 'Error' in str(res[0][0]):
        return jsonify({'status': 'error', 'message': res[0][0]})

    r = res[0]
    return jsonify({"id": str(order_detail_id), "order_id": str(r[0]), "product_id": str(r[1]), "unit_price": str(r[2]),
                    "discount": str(r[3]),
                    "quantity": str(r[4])})


@app.route('/api/v1/order_details/', methods=['POST'])
def new_order_details():
    """
    Create New Order_Details
    """
    json = request.json
    id = json['id']
    order_id = json['order_id']
    product_id = json['product_id']
    unit_price = json['unit_price']
    discount = json['discount']
    quantity = json['quantity']
    res = spcall('new_order', (id, order_id, product_id, unit_price, discount, quantity), True)

    if 'Error' in res[0][0]:
        return jsonify({'status': 'error', 'message': res[0][0]})
    return jsonify({'status': 'ok', 'message': res[0][0]})


@app.after_request
def add_cors(resp):
    resp.headers['Access-Control-Allow-Origin'] = flask.request.headers.get('Origin', '*')
    resp.headers['Access-Control-Allow-Credentials'] = True
    resp.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS, GET, PUT, DELETE'
    resp.headers['Access-Control-Allow-Headers'] = flask.request.headers.get('Access-Control-Request-Headers',
                                                                             'Authorization')
    if app.debug:
        resp.headers["Access-Control-Max-Age"] = '1'
    return resp
