import json, flask
from flask import request
from flask import jsonify
from flask import current_app as app
from app.db import spcall
from app import api


@api.route('/api/v1/product_categories/', methods=['POST'])
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


@api.route('/api/v1/product_categories', methods=['GET'])
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


@api.route('/api/v1/product_categories/<product_category_id>', methods=['GET'])
def get_product_category(product_category_id):
    res = spcall('get_product_category_id', (product_category_id))

    if 'Error' in res[0][0]:
        return jsonify({'status': 'error', 'message': res[0][0]})

    r = res[0]
    return jsonify(
        {"id": str(product_category_id), "name": str(r[0]), "description": str(r[1]), "main_image": str(r[2]),
         "parent_category_id": str(r[3]), "is_active": str(r[4])})


@api.route('/api/v1/product_categories/<product_category_id>/', methods=['PUT'])
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


@api.route('/api/v1/product_categories/<int:id>/', methods=['DELETE'])
def delete_product_category(id):
    res = spcall("delete_product_category", (id,), True)
    if 'Error' in res[0][0]:
        return jsonify({'status': 'error', 'message': res[0][0]})

    return jsonify({'status': 'ok', 'message': res[0][0]})

    """ Todo: This route should be protected """


"""  USER  """


@api.route('/api/v1/users/', methods=['GET'])
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


@api.route('/api/v1/users/<user_id>/', methods=['GET'])
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


@api.route('/api/v1/users/', methods=['POST'])
def new_user():
    data = json.loads(request.data)
    response = spcall('new_user', (
        data['id'],
        data['username'],
        data['password'],
        data['email'],
        data['is_admin'],), True)

    if 'Error' in response[0][0]:
        return jsonify({'status': 'error', 'message': response[0][0]})

    return jsonify({'status': 'ok', 'message': response[0][0]}), 201


"""  End USER  """
""" SUPPLIER """
@api.route('/api/v1/suppliers/', methods=['POST'])
def new_supplier(supplier_id=None):
    data = json.loads(request.data)

    response = spcall('new_supplier', (
        supplier_id,
        data['name'],
        data['address'],
        data['phone'],
        data['fax'],
        data['email'],
        data['is_active'],), True)

    if 'Error' in response[0][0]:
        return jsonify({'status': 'error', 'message': response[0][0]})

    return jsonify({'status': 'ok', 'message': response[0][0]}), 200


@api.route('/api/v1/suppliers/<supplier_id>/', methods=['GET'])
def get_supplier(supplier_id):
    response = spcall('get_supplier', (supplier_id,))
    entries = []
    if len(response) == 0:
        return jsonify({"status": "ok", "message": "No entries found", "entries": [], "count": "0"})
    else:
        row = response[0]
        entries.append({"supplier_id": row[0],
                        "name": row[1],
                        "address": row[2],
                        "phone": row[3],
                        "fax": row[4],
                        "email": row[5]})
        return jsonify({"status": "ok", "message": "ok", "entries": entries, "count": len(entries)})


@api.route('/api/v1/suppliers/', methods=['GET'])
def get_all_suppliers():
    res = spcall('get_suppliers', ())

    if 'Error' in str(res[0][0]):
        return jsonify({'status': 'error', 'message': res[0][0]})

    recs = []
    for r in res:
        recs.append({"supplier_id": str(r[0]), "name": str(r[1]), "address": str(r[2]), "phone": str(r[3]), "fax": str(r[4]),
                     "email": str(r[5]), "is_active": str(r[6])})
    return jsonify({'status': 'ok', 'entries': recs, 'count': len(recs)})


""" END OF SUPPLIER """

""" CART ITEM """


@api.route('/api/v1/cart_items/', methods=['POST'])
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


@api.route('/api/v1/cart_items/', methods=['GET'])
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


@api.route('/api/v1/cart_items/<cart_item_id>/', methods=['GET'])
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


@api.route('/api/v1/carts/', methods=['POST'])
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


@api.route('/api/v1/carts/<cart_id>/', methods=['GET'])
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


@api.route('/api/v1/carts/', methods=['GET'])
def get_carts():
    """
    Retrieve All Orders
    """

    res = spcall('get_carts', ())

    if 'Error' in str(res[0][0]):
        return jsonify({'status': 'error', 'message': res[0][0]})

    recs = []
    for r in res:
        recs.append({"id": str(r[0]), "session_id": r[1], "date_created": str(r[2]), "customer_id": r[3], "is_active": r[4]})

    return jsonify({'status': 'ok', 'entries': recs, 'count': len(recs)})

""" END OF CART """

""" ORDER """


@api.route('/api/v1/orders/', methods=['POST'])
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

    if 'Error' in str(response[0][0]):
        return jsonify({'status': 'error', 'message': response[0][0]})

    return jsonify({'status': 'ok', 'message': response[0][0]}), 200


@api.route('/api/v1/orders/<order_id>/', methods=['GET'])
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


@api.route('/api/v1/orders/', methods=['GET'])
def get_orders():
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


""" ORDER ITEM """


@api.route('/api/v1/order_items/', methods=['GET'])
def get_order_items():
    """
    Retrieve All Order_Details
    """

    res = spcall('get_order_items', ())

    if 'Error' in str(res[0][0]):
        return jsonify({'status': 'error', 'message': res[0][0]})

    recs = []
    for r in res:
        recs.append({"id": str(r[0]), "order_id": str(r[1]), "product_id": str(r[2]), "unit_price": str(r[3]),
                     "discount": str(r[4]),
                     "quantity": str(r[5])})
    return jsonify({'status': 'ok', 'entries': recs, 'count': len(recs)})


@api.route('/api/v1/order_items/<order_item_id>/', methods=['GET'])
def get_order_item(order_item_id):
    """
    Retrieve Single Order_Detail
    """
    res = spcall('get_order_item_id', (order_item_id,))
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


@api.route('/api/v1/order_items/', methods=['POST'])
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


@api.route('/api/v1/wishlist_details/', methods=['POST'])
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


@api.route('/api/v1/wishlist_details/', methods=['GET'])
def get_wishlist_details():
    res = spcall('get_wishlist_details', ())

    if 'Error' in str(res[0][0]):
        return jsonify({'status': 'error', 'message': res[0][0]})

    recs = []
    for r in res:
        recs.append({"id": r[0], "cart_id": r[1], "product_id": r[2], "time_stamp": r[3]})
    return jsonify({'status': 'ok', 'entries': recs, 'count': len(recs)})


@api.route('/api/v1/wishlist/', methods=['POST'])
def new_wishlist():
    data = json.loads(request.data)

    response = spcall('new_wishlist', (
        data['id'],), True)
        
    if 'Error' in response[0][0]:
        return jsonify({'status': 'error', 'message': response[0][0]})

    return jsonify({'status': 'ok', 'message': response[0][0]}), 200


@api.route('/api/v1/wishlist/', methods=['GET'])
def get_all_wishlists():
    res = spcall('get_wishlists', ())

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


@api.route('/api/v1/wishlist/<wishlist_id>/', methods=['GET'])
def get_wishlist(wishlist_id):
    res = spcall('get_wishlist', (wishlist_id,))


    if len(res) == 0:
        return jsonify({'status': 'ok', 'message': 'No entries found', 'entries': [], 'count':'0'})
    else:
        recs = []
        for r in res:
            recs.append({"id": r[0]})

            return jsonify({'status': 'ok', 'entries': recs, 'count': len(recs)})

@api.route('/api/v1/wishlist/<int:id>/', methods=['DELETE'])
def delete_wishlist(id):
    res = spcall("delete_wishlist", (id,), True)
    if 'Error' in res[0][0]:
        return jsonify({'status': 'error', 'message': res[0][0]})

    return jsonify({'status': 'ok', 'message': res[0][0]})


"""  CUSTOMER   """


@api.route('/api/v1/customers/', methods=['POST'])
def new_customer():
    data = json.loads(request.data)

    response = spcall('new_customer', (
        data['id'],
        data['first_name'],
        data['last_name'],
        data['address'],
        data['city'],
        data['state'],
        data['postal_code'],
        data['country'],
        data['phone'],
        data['email'],
        data['user_id'],
        data['billing_address'],
        data['shipping_address'],
        data['date_created'],), True)

    if 'Error' in response[0][0]:
        return jsonify({'status': 'error', 'message': response[0][0]})
    return jsonify({'status': 'ok', 'message': response[0][0]}), 201


@api.route('/api/v1/customers/', methods=['GET'])
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


@api.route('/api/v1/customers/<customer_id>/', methods=['GET'])
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


@api.after_request
def add_cors(resp):
    resp.headers['Access-Control-Allow-Origin'] = flask.request.headers.get('Origin', '*')
    resp.headers['Access-Control-Allow-Credentials'] = True
    resp.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS, GET, PUT, DELETE'
    resp.headers['Access-Control-Allow-Headers'] = flask.request.headers.get('Access-Control-Request-Headers',
                                                                             'Authorization')
    if app.debug:
        resp.headers["Access-Control-Max-Age"] = '1'
    return resp
