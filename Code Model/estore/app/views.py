import flask
from flask import Flask, jsonify, render_template
from app import app, spcall


@app.route('/')
def index():
    return render_template('index.html', title='Home')


@app.route('/products', methods=['GET'])
def getallproducts():
    res = spcall('getproducts', ())

    if 'Error' in str(res[0][0]):
        return jsonify({'status': 'error', 'message': res[0][0]})

    recs = []
    for r in res:
        recs.append({"id": r[0], "title": r[1], "description": r[2], "unit_price": r[3], "is_active": str(r[4])})
    return jsonify({'status': 'ok', 'entries': recs, 'count': len(recs)})


@app.route('/products/<int:id>/<string:title>/<string:description>/<float:unit_price>/<string:is_active>')
def insertproduct(id, title, description, unit_price, is_active):
    res = spcall("newproduct", (id, title, description,unit_price, is_active == 'true'), True)

    if 'Error' in res[0][0]:
        return jsonify({'status': 'error', 'message': res[0][0]})

    return jsonify({'status': 'ok', 'message': res[0][0]})

#
# @app.after_request
# def add_cors(resp):
#     resp.headers['Access-Control-Allow-Origin'] = flask.request.headers.get('Origin', '*')
#     resp.headers['Access-Control-Allow-Credentials'] = True
#     resp.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS, GET, PUT, DELETE'
#     resp.headers['Access-Control-Allow-Headers'] = flask.request.headers.get('Access-Control-Request-Headers',
#                                                                              'Authorization')
#     # set low for debugging
#
#     if app.debug:
#         resp.headers["Access-Control-Max-Age"] = '1'
#     return resp
