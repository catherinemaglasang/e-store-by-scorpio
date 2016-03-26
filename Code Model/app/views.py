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
ORDER = {}
CART_DETAILS = {}
CARTS = {}
ORDER_DETAILS = {}


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
    res = spcall('get_product', ())

    if 'Error' in str(res[0][0]):
        return jsonify({'status': 'error', 'message': res[0][0]})

    recs = []

    for r in res:
        recs.append(
            {"id": str(r[0]), "sku": str(r[1]), "supplier_id": str(r[2]), "title": str(r[3]), "description": str(r[4]),
             "category_id": str(r[5]), "unit_price": str([6]), "on_hand": str(r[7]), "re_order_level": str(r[8]),
             "is_active": str(r[9])})
    return jsonify({'status': 'ok', 'entries': recs, 'count': len(recs)})

    if len(res) > 0:
        for r in res:
            recs.append({"id": str(r[0]), "sku": str(r[1]), "supplier_id": str(r[2]), "title": str(r[3]),
                         "description": str(r[4]), "category_id": str(r[5]), "unit_price": str([6]),
                         "on_hand": str(r[7]), "re_order_level": str(r[8]), "is_active": str(r[9])})
            return jsonify({'status': 'ok', 'entries': recs, 'count': len(recs)})
    else:
        return jsonify({'status': 'no entries in database'})

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


@app.route('/api/v1/product_categories', methods=['GET'])
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


@app.route('/api/v1/product_categories/<product_category_id>', methods=['GET'])
def get_product_category(product_category_id):
    res = spcall('get_product_category_id', (product_category_id))

    if 'Error' in res[0][0]:
        return jsonify({'status': 'error', 'message': res[0][0]})

    r = res[0]
    return jsonify(
        {"id": str(product_category_id), "name": str(r[0]), "description": str(r[1]), "main_image": str(r[2]),
         "parent_category_id": str(r[3]), "is_active": str(r[4])})


@app.route('/api/v1/product_categories/<product_category_id>/', methods=['PUT'])
def update_product_category(product_category_id):
    jsn = json.loads(request.data)
    id = jsn.get('id', '')
    name = jsn.get('name', ''),
    description = jsn.get('description', ''),
    main_image = jsn.get('main_image', ''),
    parent_category_id = jsn.get('parent_category_id', ''),
    is_active = True

    response = spcall('update_product_id', (
        id,
        name,
        description,
        main_image,
        parent_category_id,
        is_active), True)
    return jsonify({"status": "ok"})


@app.route('/api/v1/product_categories/<int:id>/', methods=['DELETE'])
def delete_product_category(id):
    res = spcall("delete_product_category", (id,), True)
    if 'Error' in res[0][0]:
        return jsonify({'status': 'error', 'message': res[0][0]})

    return jsonify({'status': 'ok', 'message': res[0][0]})

    """ Todo: This route should be protected """


"""  USER  """


@app.route('/api/v1/users/', methods=['GET'])
def get_all_users():
    res = spcall('get_users', ())

    if 'Error' in str(res[0][0]):
        return jsonify({'status': 'error', 'message': res[0][0]})

    recs = []
    for r in res:
        recs.append({"id": r[0],
                     "username": r[1],
                     "password": r[2],
                     "email": r[3],
                     "is_admin": r[4]})

        return jsonify({'status': 'ok', 'entries': recs, 'count': len(recs)})


@app.route('/api/v1/users/<user_id>/', methods=['GET'])
def get_user(user_id):
    res = spcall('get_user', (user_id))

    if len(res) == 0:
        return jsonify({"status": "ok", "message": "No entries found", "entries": [], "count": "0"})
    else:
        recs = []
        for r in res:
            recs.append({"id": user_id,
                         "username": r[0],
                         "password": r[1],
                         "email": r[2],
                         "is_admin": r[3]})

            return jsonify({'status': 'ok', 'entries': recs, 'count': len(recs)})


@app.route('/api/v1/users/', methods=['POST'])
def new_user():
    print "STARTING ADD"
    id = request.form['inputID']
    username = request.form['inputUsername']
    password = request.form['inputPassword']
    email = request.form['inputEmail']
    is_admin = request.form['inputIsAdmin']

    res = spcall('new_user', (id, username, password, email, is_admin), True)

    if 'Error' in res[0][0]:
        return jsonify({'status': 'error', 'message': res[0][0]})

    return jsonify({'status': 'ok', 'message': res[0][0]})

    jsn = json.loads(request.data)
    id = jsn['id']
    username = jsn['username']
    password = jsn['password']
    email = jsn['email']
    is_admin = jsn['is_admin']

    response = spcall('new_user', (
        id,
        username,
        password,
        email,
        is_admin), True)

    if 'Error' in response[0][0]:
        return jsonify({'status': 'error', 'message': response[0][0]})

    return jsonify({'status': 'ok', 'message': response[0][0]}), 201


"""  End USER  """
""" SUPPLIER """


@app.route('/api/v1/suppliers/', methods=['POST'])
def new_supplier():
    data = json.loads(request.data)

    response = spcall('new_supplier', (
        data['id'],
        data['name'],
        data['address'],
        data['phone'],
        data['fax'],
        data['email'],
        data['is_active'],), True)

    if 'Error' in response[0][0]:
        return jsonify({'status': 'error', 'message': response[0][0]})

    return jsonify({'status': 'ok', 'message': response[0][0]}), 200


@app.route('/api/v1/suppliers/<supplier_id>/', methods=['GET'])
def get_supplier(supplier_id):
    response = spcall('get_supplier', (supplier_id,))
    entries = []
    if len(response) == 0:
        return jsonify({"status": "ok", "message": "No entries found", "entries": [], "count": "0"})
    else:
        row = response[0]
        entries.append({"id": row[0],
                        "name": row[1],
                        "address": row[2],
                        "phone": row[3],
                        "fax": row[4],
                        "email": row[5]})
        return jsonify({"status": "ok", "message": "ok", "entries": entries, "count": len(entries)})


@app.route('/api/v1/suppliers/<supplier_id>/', methods=['PUT'])
def update_supplier(supplier_id):
    jsn = json.loads(request.data)
    id = jsn.get('id', '')
    name = jsn.get('name', ''),
    address = jsn.get('address', ''),
    phone = jsn.get('phone', ''),
    fax = jsn.get('fax', ''),
    email = jsn.get('email', ''),
    is_active = True
    response = spcall('update_supplier_id', (
        id,
        name,
        address,
        phone,
        fax,
        email,
        is_active), True)

    return jsonify({"status": "ok"})


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


""" END OF SUPPLIER """

""" CART ITEM """


@app.route('/api/v1/cart_items/', methods=['POST'])
def new_cart_item():
    data = json.loads(request.data)

    response = spcall('new_cart_item', (
        data['id'],
        data['cart_id'],
        data['product_id'],
        data['quantity'],
        data['time_stamp'],), True)

    if 'Error' in response[0][0]:
        return jsonify({'status': 'error', 'message': response[0][0]})

    return jsonify({'status': 'ok', 'message': response[0][0]}), 200


@app.route('/api/v1/cart_items/', methods=['GET'])
def get_cart_items():
    res = spcall('get_cart_items', ())

    if 'Error' in str(res[0][0]):
        return jsonify({'status': 'error', 'message': res[0][0]})

    recs = []
    for r in res:
        recs.append({"id": r[0],
                     "cart_id": r[1],
                     "product_id": r[2],
                     "quantity": r[3],
                     "time_stamp": r[4]})

        return jsonify({'status': 'ok', 'entries': recs, 'count': len(recs)})


@app.route('/api/v1/cart_items/<cart_item_id>/', methods=['GET'])
def get_cart_item(cart_item_id):
    res = spcall('get_cart_item', (cart_item_id,))

    if len(res) == 0:
        return jsonify({"status": "ok", "message": "No entries found", "entries": [], "count": "0"})
    else:
        recs = []
        for r in res:
            recs.append({"cart_id": r[0],
                         "product_id": r[1],
                         "quantity": r[2],
                         "time_stamp": str(r[3])})

            return jsonify({'status': 'ok', 'entries': recs, 'count': len(recs)})


""" END CART ITEM """

""" CART """


@app.route('/api/v1/carts/', methods=['POST'])
def new_cart():
    data = json.loads(request.data)

    response = spcall('new_cart', (
        data['id'],
        data['session_id'],
        data['date_created'],
        data['customer_id'],
        data['is_active'],), True)

    if 'Error' in response[0][0]:
        return jsonify({'status': 'error', 'message': response[0][0]})

    return jsonify({'status': 'ok', 'message': response[0][0]}), 200


@app.route('/api/v1/carts/<cart_id>/', methods=['GET'])
def get_cart(cart_id):
    res = spcall('get_cart', (cart_id,))

    if len(res) == 0:
        return jsonify({"status": "ok", "message": "No entries found", "entries": [], "count": "0"})
    else:
        recs = []
        for r in res:
            recs.append({"session_id": r[0],
                         "date_created": str(r[1]),
                         "customer_id": r[2],
                         "is_active": r[3]})

            return jsonify({'status': 'ok', 'entries': recs, 'count': len(recs)})


""" END OF CART """

""" ORDER """


@app.route('/api/v1/orders/', methods=['POST'])
def new_order():
    data = json.loads(request.data)

    response = spcall('new_order', (
        data['id'],
        data['customer_id'],
        data['payment_id'],
        data['transaction_date'],
        data['shipping_date'],
        data['time_stamp'],
        data['transaction_status'],
        data['total'],), True)

    if 'Error' in response[0][0]:
        return jsonify({'status': 'error', 'message': response[0][0]})

    return jsonify({'status': 'ok', 'message': response[0][0]}), 200


@app.route('/api/v1/orders/<order_id>/', methods=['GET'])
def get_order(order_id):
    response = spcall('get_order_id', (order_id,))
    entries = []
    if len(response) == 0:
        return jsonify({"status": "ok", "message": "No entries found", "entries": [], "count": "0"})
    else:
        r = response[0]
        entries.append({"customer_id": r[0],
                        "payment_id": r[1],
                        "transaction_date": str(r[2]),
                        "shipping_date": str(r[3]),
                        "time_stamp": str(r[4]),
                        "transaction_status": str(r[5]),
                        "total": r[6]})
        return jsonify({"status": "ok", "message": "ok", "entries": entries, "count": len(entries)})


# @app.route('/api/v1/orders/', methods=['GET'])
# def get_all_orders():
#     """
#     Retrieve All Orders
#     """
#
#     res = spcall('get_orders', ())
#
#     if 'Error' in str(res[0][0]):
#         return jsonify({'status': 'error', 'message': res[0][0]})
#
#     recs = []
#     for r in res:
#         recs.append({"id": str(r[0]), "customer_id": str(r[1]), "payment_id": str(r[2]), "transaction_date": str(r[3]),
#                      "shipping_date": str(r[4]),
#                      "time_stamp": str(r[5]), "transaction_status": str(r[6]), "total": str(r[7])})
#     return jsonify({'status': 'ok', 'entries': recs, 'count': len(recs)})
#


""" ORDER ITEM """


# @app.route('/api/v1/order_details', methods=['GET'])
# def get_all_order_details():
#     """
#     Retrieve All Order_Details
#     """
#
#     res = spcall('get_order_details', ())
#
#     if 'Error' in str(res[0][0]):
#         return jsonify({'status': 'error', 'message': res[0][0]})
#
#     recs = []
#     for r in res:
#         recs.append({"id": str(r[0]), "order_id": str(r[1]), "product_id": str(r[2]), "unit_price": str(r[3]),
#                      "discount": str(r[4]),
#                      "quantity": str(r[5])})
#     return jsonify({'status': 'ok', 'entries': recs, 'count': len(recs)})


@app.route('/api/v1/order_items/<order_item_id>/', methods=['GET'])
def get_order_item(order_item_id):
    """
    Retrieve Single Order_Detail
    """
    res = spcall('get_order_item_id', order_item_id)
    if len(res) == 0:
        return jsonify({"status": "ok", "message": "No entries found", "entries": [], "count": "0"})
    else:
        recs = []
        for r in res:
            recs.append({"order_id": r[0],
                         "product_id": r[1],
                         "unit_price": r[2],
                         "discount": r[3],
                         "quantity": r[4]})

            return jsonify({'status': 'ok', 'entries': recs, 'count': len(recs)})


@app.route('/api/v1/order_items/', methods=['POST'])
def new_order_item():
    data = json.loads(request.data)

    response = spcall('new_order_item', (
        data['id'],
        data['order_id'],
        data['product_id'],
        data['unit_price'],
        data['discount'],
        data['quantity'],), True)

    if 'Error' in response[0][0]:
        return jsonify({'status': 'error', 'message': response[0][0]})

    return jsonify({'status': 'ok', 'message': response[0][0]}), 200

""" END OF ORDER"""


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
    print "STARTING ADD"
    id = request.form['inputID']

    res = spcall('new_wishlist', (id), True)

    if 'Error' in res[0][0]:
        return jsonify({'status': 'error', 'message': res[0][0]})

    return jsonify({'status': 'ok', 'message': res[0][0]})

    jsn = json.loads(request.data)
    id = jsn['id']

    response = spcall('new_wishlist', (
        id), True)

    if 'Error' in response[0][0]:
        return jsonify({'status': 'error', 'message': response[0][0]})

    return jsonify({'status': 'ok', 'message': response[0][0]}), 201


@app.route('/api/v1/wishlist', methods=['GET'])
def get_all_wishlists():
    res = spcall('get_wishlist', ())

    if 'Error' in str(res[0][0]):
        return jsonify({'status': 'error', 'message': res[0][0]})

    recs = []

    for r in res:
        recs.append({"id": str(r[0])})

    return jsonify({'status': 'ok', 'entries': recs, 'count': len(recs)})

    if len(res) > 0:
        for r in res:
            recs.append({"id": str(r[0])})
            return jsonify({'status': 'ok', 'entries': recs, 'count': len(recs)})
    else:
        return jsonify({'status': 'no entries in database'})


@app.route('/api/v1/wishlist/<wishlist_id>/', methods=['GET'])
def get_wishlist(wishlist_id):
    res = spcall('get_wishlist', wishlist_id)

    if 'Error' in str(res[0][0]):
        return jsonify({'status': 'error', 'message': res[0][0]})

    r = res[0]
    return jsonify({"id": str(wishlist_id)})


@app.route('/api/v1/wishlist/<int:id>/', methods=['DELETE'])
def delete_wishlist(id):
    res = spcall("delete_wishlist", (id,), True)
    if 'Error' in res[0][0]:
        return jsonify({'status': 'error', 'message': res[0][0]})

    return jsonify({'status': 'ok', 'message': res[0][0]})


"""  CUSTOMER   """


@app.route('/api/v1/customers/', methods=['POST'])
def new_customer():
    print "STARTING ADD"
    id = request.form['inputID']
    first_name = request.form['inputFirstName']
    last_name = request.form['inputLastName']
    address = request.form['inputAddress']
    city = request.form['inputCity']
    state = request.form['inputState']
    postal_code = request.form['inputPostalCode']
    country = request.form['inputCountry']
    phone = request.form['inputPhone']
    email = request.form['inputEmail']
    user_id = request.form['inputUserId']
    billing_address = request.form['inputBillingAddress']
    shipping_address = request.form['inputShippingAddress']
    date_created = request.form['inputDateCreated']

    res = spcall('new_customer', (
        id, first_name, last_name, address, city, state, postal_code, country, phone, email, user_id, billing_address,
        shipping_address, date_created), True)

    if 'Error' in res[0][0]:
        return jsonify({'status': 'error', 'message': res[0][0]})
    return jsonify({'status': 'ok', 'message': res[0][0]})

    jsn = json.loads(request.data)
    id = jsn['id']
    first_name = jsn['first_name']
    last_name = jsn['last_name']
    address = jsn['address']
    city = jsn['city']
    state = jsn['state']
    postal_code = jsn['postal_code']
    country = jsn['country']
    phone = jsn['phone']
    email = jsn['email']
    user_id = jsn['user_id']
    billing_address = jsn['billing_address']
    shipping_address = jsn['shipping_address']
    date_created = jsn['date_created']

    response = spcall('new_customer', (
        id,
        first_name,
        last_name,
        address,
        city,
        state,
        postal_code,
        country,
        phone,
        email,
        user_id,
        billing_address,
        shipping_address,
        date_created
    ), True)

    if 'Error' in response[0][0]:
        return jsonify({'status': 'error', 'message': response[0][0]})
    return jsonify({'status': 'ok', 'message': response[0][0]}), 201


@app.route('/api/v1/customers/', methods=['GET'])
def get_all_customers():
    res = spcall('get_all_customers', ())

    if 'Error' in str(res[0][0]):
        return jsonify({'status': 'error', 'message': res[0][0]})

    recs = []
    for r in res:
        recs.append({
            "id": r[0],
            "first_name": r[1],
            "last_name": r[2],
            "address": r[3],
            "city": r[4],
            "state": r[5],
            "postal_code": r[6],
            "country": r[7],
            "phone": r[8],
            "email": r[9],
            "user_id": r[10],
            "billing_address": r[11],
            "shipping_address": r[12],
            "date_created": r[13]
        })
        return jsonify({'status': 'ok', 'entries': recs, 'count': len(recs)})


@app.route('/api/v1/customers/<customer_id>/', methods=['GET'])
def get_customer(customer_id):
    res = spcall('get_single_customer', (customer_id))

    if len(res) == 0:
        return jsonify({'status': 'ok', 'message': 'No entries found', 'entries': [], 'count': '0'})
    else:
        recs = []
        for r in res:
            recs.append({
                "id": customer_id,
                "first_name": r[0],
                "last_name": r[1],
                "address": r[2],
                "city": r[3],
                "state": r[4],
                "postal_code": r[5],
                "country": r[6],
                "phone": r[7],
                "email": r[8],
                "user_id": r[9],
                "billing_address": r[10],
                "shipping_address": r[11],
                "date_created": r[12]
            })
            return jsonify({'status': 'ok', 'entries': recs, 'count': len(recs)})


"""  END CUSTOMER   """


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
