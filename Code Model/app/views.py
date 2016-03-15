import os
from os import sys
import json, flask
from flask import render_template, request
from flask import jsonify
from app import app
from .models import DBconn

PRODUCTS = {}
SUPPLIERS = {}
USERS = {}
CATEGORIES = {}
WISHLISTS = {}
ORDER = {}
CART_DETAILS = {}


def spcall(qry, param, commit=False):
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
    # return app.send_static_file('index.html')
    # return render_template('index.html')
    return jsonify({"status": "ok"})


@app.route('/api/v1/products/', methods=['POST'])
def new_product():
    print "STARTING ADD"
    id = request.form['inputID']
    sku = request.form['inputSku']
    supplier_id = request.form['inputSupplierID']
    title = request.form['inputTitle']
    description = request.form['inputDescription']
    category_id = request.form['inputCategoryID']
    unit_price = request.form['inputUnitPrice']
    on_hand = request.form['inputOnHand']
    re_order_level = request.form['inputReorderLevel']
    is_active = False

    res = spcall('new_product', (
    id, sku, supplier_id, title, description, category_id, unit_price, on_hand, re_order_level, is_active), True)

    if 'Error' in res[0][0]:
        return jsonify({'status': 'error', 'message': res[0][0]})

    return jsonify({'status': 'ok', 'message': res[0][0]})


# END OF ADD PRODUCT


@app.route('/api/v1/products/', methods=['GET'])
def get_all_products():
    res = spcall('get_product', ())

    if 'Error' in str(res[0][0]):
        return jsonify({'status': 'error', 'message': res[0][0]})


    recs =[]

    for r in res:
        recs.append(
            {"id": str(r[0]), "sku": str(r[1]), "supplier_id": str(r[2]), "title": str(r[3]), "description": str(r[4]),
             "category_id": str(r[5]), "unit_price": str([6]), "on_hand": str(r[7]), "re_order_level": str(r[8]),
             "is_active": str(r[9])})
    return jsonify({'status': 'ok', 'entries': recs, 'count': len(recs)})


    if len(res) > 0:
        for r in res:
            recs.append({"id": str(r[0]), "sku": str(r[1]), "supplier_id": str(r[2]), "title": str(r[3]), "description": str(r[4]), "category_id": str(r[5]), "unit_price": str([6]), "on_hand": str(r[7]), "re_order_level": str(r[8]), "is_active": str(r[9])})
            return jsonify({'status': 'ok', 'entries': recs, 'count': len(recs)})
    else:
        return jsonify({'status': 'no entries in database'})



@app.route('/api/v1/products/<product_id>/', methods=['GET'])
def get_product(product_id):
    res = spcall('get_product_id', (product_id))

    if 'Error' in res[0][0]:
        return jsonify({'status': 'error', 'message': res[0][0]})

    r = res[0]
    return jsonify({"id": str(product_id), "sku": str(r[0]), "supplier_id": str(r[1]), "title": str(r[2]),
                    "description": str(r[3]), "category_id": str(r[4]), "unit_price": str(r[5]), "on_hand": str(r[6]),
                    "re_order_level": str(r[7]), "is_active": str(r[8])})


@app.route('/api/v1/products/<int:id>/', methods=['DELETE'])
def delete_product(id):
    res = spcall("delete_product", (id,), True)
    if 'Error' in res[0][0]:
        return jsonify({'status': 'error', 'message': res[0][0]})

    return jsonify({'status': 'ok', 'message': res[0][0]})


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



@app.route('/api/v1/product_categories/', methods=['GET'])
def get_all_product_categories():
    res = spcall('get_product_category', ())

    if 'Error' in str(res[0][0]):
        return jsonify({'status': 'error', 'message': res[0][0]})

    recs =[]

    for r in res:
        recs.append(
            {"id": str(r[0]), "name": str(r[1]), "description": str(r[2]), "main_image": str(r[3]), "parent_category_id": str(r[4]),
             "is_active": str(r[5])})
    return jsonify({'status': 'ok', 'entries': recs, 'count': len(recs)})

    if len(res) > 0:
        for r in res:
            recs.append({"id": str(r[0]), "name": str(r[1]), "description": str(r[2]), "main_image": str(r[3]), "parent_category_id": str(r[4]), "is_active": str(r[5])})
            return jsonify({'status': 'ok', 'entries': recs, 'count': len(recs)})
    else:
        return jsonify({'status': 'no entries in database'})


@app.route('/api/v1/product_categories/<product_category_id>/', methods=['GET'])
def get_product_category(product_category_id):
    res = spcall('get_product_category_id', (product_category_id))

    if 'Error' in res[0][0]:
        return jsonify({'status': 'error', 'message': res[0][0]})

    r = res[0]
    return jsonify({"id": str(product_category_id), "name": str(r[0]), "description": str(r[1]), "main_image": str(r[2]),
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


""" my task """
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
    return jsonify({"id": str(supplier_id), "name": str(r[0]), "address": str(r[1]), "phone": str(r[2]), "fax": str(r[3]),
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


@app.route('/api/v1/cart_details/<cart_detail_id>/', methods=['GET'])
def get_cart_detail(cart_detail_id):
    res = spcall('get_cart_detail', cart_detail_id)
    #
    # if 'Error' in res[0][0]:
    #     return jsonify({'status': 'error', 'message': res[0][0]})

    r = res[0]
    return jsonify({"cart_id": str(cart_detail_id), "product_id": str(r[0]), "quantity": str(r[1]), "time_stamp": str(r[3])})


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
        recs.append({"id": str(r[0]), "customer_id": str(r[1]), "payment_id": str(r[2]), "transaction_date": str(r[3]), "shipping_date": str(r[4]),
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
    return jsonify({"id": str(orders_id), "customer_id": str(r[0]), "payment_id": str(r[1]), "transaction_date": str(r[2]), "shipping_date": str(r[3]),
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
    res = spcall('new_order', (id, customer_id, payment_id, transaction_date, shipping_date, time_stamp, transaction_status, total), True)

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

