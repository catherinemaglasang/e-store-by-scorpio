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