import json
from flask import render_template
from flask import jsonify
from app import app


@app.route('/')
def index():
	return render_template('index.html', title='Home')
