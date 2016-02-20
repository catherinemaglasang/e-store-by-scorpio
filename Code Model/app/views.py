import os
from os import sys
import json
from flask import render_template
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

@app.route('/api/v1/users/<int:id>')
def get_user(id):
	res = spcall('get_user', (id), True)

	if 'Error' in res[0][0]:
		return jsonify({'status': 'error', 'message': res[0][0]})
	return jsonify({'status': 'ok', "id": r[0], "username": r[1], "password": r[2], "is_admin": str(r[3])})