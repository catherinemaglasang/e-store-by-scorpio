import json
from flask import render_template, flash, redirect, request, session
from flask import jsonify
from app import app
from app import db
from .models import *


@app.route('/')
def index():
	return render_template('index.html', title='Home')

@app.route('/api/login/', methods=['POST'])
def login():
	json_data = request.json
	user = User.query.filter_by(email=json_data['email']).first()
	if user and bcrypt.check_password_hash(user.password, json_data['password']):
		session['logged_in'] = True
		status = True
	else:
		status = False
	return jsonify({'result': status})
