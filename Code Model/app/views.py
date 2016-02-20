import os
from os import sys
import json
from flask import render_template, request
from flask import jsonify
from app import app
from .models import DBconn


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
	return render_template('index.html', title='Home')


@app.route('/api/v1/products', methods=['GET'])
def get_all_products():
    res = spcall('get_product', ())

    if 'Error' in str(res[0][0]):
        return jsonify({'status': 'error', 'message': res[0][0]})

    recs = []
    for r in res:
        recs.append({"id": r[0], "sku": r[1], "supplier_id": r[2], "title": r[3], "description": r[4], "category_id": r[5], "unit_price": [6], "on_hand": r[7], "re_order_level": r[8], "is_active": str(r[9])})
    return jsonify({'status': 'ok', 'entries': recs, 'count': len(recs)})


@app.route('/api/v1/products/<product_id>',  methods=['GET'])
def get_product(product_id):
    res = spcall('get_product_id', (product_id))

    if 'Error' in res[0][0]:
        return jsonify({'status': 'error', 'message': res[0][0]})
    
    r = res[0]
    return jsonify({"sku": r[0], "supplier_id": r[1], "title": r[2], "description": r[3], "category_id": r[4], "unit_price": r[5], "on_hand": r[6], "re_order_level": r[7], "is_active": str(r[8])})


""" Todo: This route should be protected """
@app.route('/api/v1/users', methods=['GET'])
def get_all_users():
    res = spcall('get_users', ())

    if 'Error' in str(res[0][0]):
        return jsonify({'status': 'error', 'message': res[0][0]})

    recs = []
    for r in res:
        recs.append({"id": r[0], "username": r[1], "password": r[2], "is_admin": str(r[3])})
    return jsonify({'status': 'ok', 'entries': recs, 'count': len(recs)})

@app.route('/api/v1/users/<user_id>', methods=['GET'])
def get_user(user_id):
	res = spcall('get_user', (user_id))

	if 'Error' in res[0][0]:
		return jsonify({'status': 'error', 'message': res[0][0]})
	
	rec = res[0]
	return jsonify({"username": rec[0], "password": rec[1], "is_admin": str(rec[2])})

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
        recs.append({"id": r[0], "name": r[1], "phone": r[2],"fax":r[3], "email":r[4], "is_active": str(r[5])})
    return jsonify({'status': 'ok', 'entries': recs, 'count': len(recs)})


@app.route('/api/v1/suppliers/<supplier_id>', methods=['GET'])
def get_supplier(supplier_id):
    res = spcall('get_supplier', (supplier_id))

    if 'Error' in res[0][0]:
        return jsonify({'status': 'error', 'message': res[0][0]})
    
    r = res[0]
    return jsonify({"name": r[0], "phone": r[1],"fax":r[2], "email":r[3], "is_active": str(r[4])})



